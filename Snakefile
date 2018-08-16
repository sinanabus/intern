configfile : "config.json"

rule main:
    input:
        expand("{BAMOUTDIR}/{sample_id}.recal.bam", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = "LF2017_63_S8_L001_001"),

RG = '"@RG\tID:1121-L001\tSM:LF2017_63\tLB:171120_D00515_1121_AH3H2LBCX2\tPU:1121.L001.LF2017_63\tCN:USZ_MTP\tPL:ILLUMINA"'
rule bwa_map:
    input:
        expand("{REFINDIR}/{filename}", REFINDIR = config["directories"]["REFERENCE"], filename = "ucsc.hg19.fasta"),
        expand("{FASTQINDIR}/{samples}.fastq", FASTQINDIR = config["directories"]["SAMPLE"], samples = config["samples"].values())
    output:
        expand("{BAMOUTDIR}/{sample_id}_sorted.bam", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = "LF2017_63_S8_L001_001")
    shell:
        "{config[tools][bwa_mem][call]} -R {RG} {input} | {config[tools][PICARD][SortSam][call]} INPUT=/dev/stdin OUTPUT={output}" +
        " CREATE_INDEX=true VALIDATION_STRINGENCY=SILENT SORT_ORDER=coordinate MAX_RECORDS_IN_RAM=500000"

rule realign_target:
    input:
        expand("{REFINDIR}/{filename}", REFINDIR = config["directories"]["REFERENCE"], filename = "ucsc.hg19.fasta"),
        expand("{BAMOUTDIR}/{sample_id}_sorted.bam", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = "LF2017_63_S8_L001_001")
    output:
    # realign is created manually
        expand("{TEMPINDIR}/realign/{sample_id}_realign.intervals", TEMPINDIR = config["directories"]["TEMPDIR"],sample_id = "LF2017_63_S8_L001_001")
    shell:
        "{config[tools][GATK][RealignerTarget][call]} -R {input[0]} -I {input[1]} -o {output}"

rule realign:
    input:
        expand("{REFINDIR}/{filename}", REFINDIR = config["directories"]["REFERENCE"], filename = "ucsc.hg19.fasta"),
        expand("{BAMOUTDIR}/{sample_id}_sorted.bam", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = "LF2017_63_S8_L001_001"),
        expand("{TEMPINDIR}/realign/{sample_id}_realign.intervals", TEMPINDIR = config["directories"]["TEMPDIR"],sample_id = "LF2017_63_S8_L001_001")
    output:
        expand("{BAMOUTDIR}/{sample_id}_realigned.bam", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = "LF2017_63_S8_L001_001")
    shell:
        "{config[tools][GATK][IndelRealigner][call]} -R {input[0]} -I {input[1]} -targetIntervals {input[2]} -o {output}"

rule fix_mate:
    input:
        expand("{BAMOUTDIR}/{sample_id}_realigned.bam", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = "LF2017_63_S8_L001_001")
    output:
        expand("{BAMOUTDIR}/{sample_id}_matefixed.bam", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = "LF2017_63_S8_L001_001")
    shell:
        "{config[tools][PICARD][FixMateInformation][call]} VALIDATION_STRINGENCY=SILENT CREATE_INDEX=true SORT_ORDER=coordinate" +
        " MAX_RECORDS_IN_RAM=500000 INPUT={input} OUTPUT={output}"

dup_file_name = expand("{DUPINDIR}/{sample_id}.dup.metrics", DUPINDIR = config["directories"]["PIPDIR"]["dup_metrics"], sample_id = "LF2017_63_S8_L001_001")
#DUP_METRICS = open(dup_file_name, "w")
rule remove_duplicates:
    input:
        expand("{BAMOUTDIR}/{sample_id}_matefixed.bam", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = "LF2017_63_S8_L001_001")
    output:
        expand("{BAMOUTDIR}/{sample_id}.dup.bam", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = "LF2017_63_S8_L001_001")
    shell:
        "{config[tools][PICARD][MarkDuplicates][call]} REMOVE_DUPLICATES=true"
        + " CREATE_MD5_FILE=true VALIDATION_STRINGENCY=SILENT CREATE_INDEX=true INPUT={input} OUTPUT={output} METRICS_FILE={dup_file_name}"

rule recalibration_metrics:
    input:
        expand("{REFINDIR}/{filename}", REFINDIR = config["directories"]["REFERENCE"], filename = "ucsc.hg19.fasta"),
        expand("{BAMOUTDIR}/{sample_id}.dup.bam", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = "LF2017_63_S8_L001_001")
    output:
        expand("{BQSRDIR}/{sample_id}.grp", BQSRDIR = config["directories"]["PIPDIR"]["BQSR_metrics"], sample_id = "LF2017_63_S8_L001_001")
    shell:
        "{config[tools][GATK][BaseRecalibrator][call]} -R {input[0]} -I {input[1]} -o {output}"

rule recalibration:
    input:
        expand("{REFINDIR}/{filename}", REFINDIR = config["directories"]["REFERENCE"], filename = "ucsc.hg19.fasta"),
        expand("{BAMOUTDIR}/{sample_id}.dup.bam", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = "LF2017_63_S8_L001_001"),
        expand("{BQSRDIR}/{sample_id}.grp", BQSRDIR = config["directories"]["PIPDIR"]["BQSR_metrics"], sample_id = "LF2017_63_S8_L001_001")
    output:
        expand("{BAMOUTDIR}/{sample_id}.recal.bam", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = "LF2017_63_S8_L001_001"),
    shell:
        "{config[tools][GATK][PrintReads][call]} -R {input[0]} -I {input[1]} -BQSR {input[2]} -o {output}"
