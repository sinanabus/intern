configfile : "config.json"

SAMPLE_ID = 'LF2017_63'


rule all:
    input:
        #"LF2017_63_bcf.vcf",
        #"LF2017_63_mutect2.vcf",
        "LF2017_63_varscan.vcf",
        "temp/info_insertSize.txt",
        #expand("{fastqc_dir}/{sample_id}_fastqc.zip",fastqc_dir = config["directories"]["OUTDIR"]["fastqc"], sample_id = SAMPLE_ID),
        expand("{OUTDIR}/{sample_id}_metrics.insertSize.tsv", OUTDIR = config["directories"]["PIPDIR"]["metrics"], sample_id = SAMPLE_ID),
        expand("{OUTDIR}/{sample_id}_metrics.align.tsv", OUTDIR = config["directories"]["PIPDIR"]["metrics"], sample_id = SAMPLE_ID)



RG_L001 = '"@RG\tID:1121-L001\tSM:LF2017_63\tLB:171120_D00515_1121_AH3H2LBCX2\tPU:1121.L001.LF2017_63\tCN:USZ_MTP\tPL:ILLUMINA"'

rule bwa_map_lane1:
    input:
        ref = expand("{PATH_REF}", PATH_REF = config["req_file_paths"]["REFERENCE"]),
        #"{config[req_file_paths][REFERENCE]}"
        fastq =expand("{FASTQINDIR}/{samples}.fastq", FASTQINDIR = config["directories"]["SAMPLE"], samples = config["samples"]["LANE1"].values())
    output:
        bam = expand("{BAMOUTDIR}/{sample_id}_L001_sort.bam", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = SAMPLE_ID),
        bai = expand("{BAMOUTDIR}/{sample_id}_L001_sort.bai", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = SAMPLE_ID)
    shell:
        "{config[tools][bwa_mem][call]} -t 2 -R {RG_L001} {input.ref} {input.fastq} | {config[tools][PICARD][SortSam][call]} INPUT=/dev/stdin OUTPUT={output.bam}" +
        " CREATE_INDEX=true VALIDATION_STRINGENCY=SILENT SORT_ORDER=coordinate MAX_RECORDS_IN_RAM=500000"

RG_L002 = '"@RG\tID:1121-L002\tSM:LF2017_63\tLB:171120_D00515_1121_AH3H2LBCX2\tPU:1121.L002.LF2017_63\tCN:USZ_MTP\tPL:ILLUMINA"'

rule bwa_map_lane2:
    input:
        ref = expand("{PATH_REF}", PATH_REF = config["req_file_paths"]["REFERENCE"]),
        #"{config[req_file_paths][REFERENCE]}"
        fastq =expand("{FASTQINDIR}/{samples}.fastq.gz", FASTQINDIR = config["directories"]["SAMPLE"], samples = config["samples"]["LANE2"].values())
    output:
        bam = expand("{BAMOUTDIR}/{sample_id}_L002_sort.bam", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = SAMPLE_ID),
        bai = expand("{BAMOUTDIR}/{sample_id}_L002_sort.bai", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = SAMPLE_ID)
    shell:
        "{config[tools][bwa_mem][call]} -t 2 -R {RG_L002} {input.ref} {input.fastq} | {config[tools][PICARD][SortSam][call]} INPUT=/dev/stdin OUTPUT={output.bam}" +
        " CREATE_INDEX=true VALIDATION_STRINGENCY=SILENT SORT_ORDER=coordinate MAX_RECORDS_IN_RAM=500000"

rule merge_bam:
    input:
        expand("{BAMOUTDIR}/{sample_id}_{lanes}_sort.bam", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = SAMPLE_ID, lanes =['L001','L002'])
        #expand("{BAMOUTDIR}/{sample_id}_L002_sort.bam", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = SAMPLE_ID)
    output:
        bam = expand("{BAMOUTDIR}/{sample_id}_sort.bam", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = SAMPLE_ID),
        bai = expand("{BAMOUTDIR}/{sample_id}_sort.bai", BAMOUTDIR = config["directories"]["PIPDIR"]["mapped"], sample_id = SAMPLE_ID)
    shell:
        "{config[tools][PICARD][MergeSamFiles][call]} I={input[0]} I={input[1]} O={output.bam}" +
        "ASSUME_SORTED=true USE_THREADING=true CREATE_INDEX=true "

include : 'scripts/Snake/Bam_Processing.snake'
include : 'scripts/Snake/Variant_Calling.snake'
include : 'scripts/Snake/Quality_Control.snake'


rule report:
    input:
        expand("{DIR_METRICS}/{sample_id}_metrics.insertSize.tsv", DIR_METRICS = config["directories"]["PIPDIR"]["metrics"], sample_id = SAMPLE_ID)
    output:
        "temp/info_insertSize.txt"
    script:
        "scripts/Python/evaluate_QualityControl.py"