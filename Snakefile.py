from pathlib import Path


configfile : "config.json"

#create necessary directories

all_dirs = []
for dir in config["directories"]:
    if  type(config["directories"][dir]) is not dict:
        all_dirs.append(config["directories"][dir])
    else:
        for d in config["directories"][dir]:
            all_dirs.append(config["directories"][dir][d])

rule all:
    input:
        expand("{QC_DIR}/{samples}_fastqc.html",QC_DIR = config["directories"]["OUTDIR"]["fastqc"],samples = config["samples"].values()),
        expand("{QC_DIR}/{samples}_fastqc.zip", QC_DIR = config["directories"]["OUTDIR"]["fastqc"], samples = config["samples"].values())


rule create_Dirs:
    output:
        expand("{dirs}", dirs = all_dirs)
    run:
        for path in all_dirs:
            dir = Path(path)
            if (dir.is_dir() is not True):
                    shell("mkdir {dir}")

#read summary.txt and report FAILED ones!
rule fastqc:
    input:
        expand("{dir}/{samples}.fastq", dir = config["directories"]["SAMPLE"], samples = config["samples"].values())
    output:
        html = expand("{QC_DIR}/{samples}_fastqc.html",QC_DIR = config["directories"]["OUTDIR"]["fastqc"],samples = config["samples"].values()),
        zip = expand("{QC_DIR}/{samples}_fastqc.zip", QC_DIR = config["directories"]["OUTDIR"]["fastqc"], samples = config["samples"].values())
    shell:
        "{config[tools][FASTQC][call]} {input} -o {config[directories][OUTDIR][fastqc]}"

'''
rule all:
    input:
        "report.html"



rule bwa_map:
#map the reads
  input:
    "data2/reference/Homo_sapiens.GRCh38.dna_rm.chromosome.22.fa",

    #"data/samples/{sample}.fastq"
    #expand("data2/{samples}.fastq.gz", samples = SAMPLES)
    expand("data2/{samples}.fastq", samples = SAMPLES)
  output:
    "mapped_reads/LF2017_1.bam"
  shell:
    "bwa mem {input} | samtools view -Sb - > {output}"

rule samtools_sort:
#sort the mapped reads
    input:
        "mapped_reads/{sample}.bam"
    output:
        "sorted_reads/{sample}.bam"
    shell:
        "samtools sort -T sorted_reads/{wildcards.sample} "
        "-O bam {input} > {output}"
rule samtools_index:
#index the sorted/mapped reads
    input:
        "sorted_reads/{sample}.bam"
    output:
        "sorted_reads/{sample}.bam.bai"
    shell:
        "samtools index {input}"

#Variant calling on multiple samples

#SAMPLES = ['A', 'B']


rule bcftools_call:
    input:
        fa = "data2/reference/Homo_sapiens.GRCh38.dna_rm.chromosome.22.fa",
        bam = "sorted_reads/LF2017_1.bam",
        bai = "sorted_reads/LF2017_1.bam.bai"
    output:
        "calls/all.vcf"
    shell:
        "samtools mpileup -g -f {input.fa} {input.bam} | "
        "bcftools call -mv - > {output}"

rule report:
    input:
        "calls/all.vcf"
    output:
        "report.html"
    run:
        from snakemake.utils import report
        with open(input[0]) as vcf:
            n_calls = sum(1 for l in vcf if not l.startswith("#"))

        report("""
        An example variant calling workflow
        ===================================

        Reads were mapped to the Yeast
        reference genome and variants were called jointly with
        SAMtools/BCFtools.

        This resulted in {n_calls} variants (see Table T1_).
        """, output[0], T1=input[0])
'''
