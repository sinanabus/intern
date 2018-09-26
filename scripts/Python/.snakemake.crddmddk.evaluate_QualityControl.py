
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/sabus/miniconda3/envs/F1-pipe/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x04\x00\x00\x00ruleq\tX\x06\x00\x00\x00reportq\nX\x05\x00\x00\x00inputq\x0bcsnakemake.io\nInputFiles\nq\x0c)\x81q\rX1\x00\x00\x00analysis/metrics/LF2017_63_metrics.insertSize.tsvq\x0ea}q\x0fh\x07}q\x10sbX\x06\x00\x00\x00outputq\x11csnakemake.io\nOutputFiles\nq\x12)\x81q\x13X\x18\x00\x00\x00temp/info_insertSize.txtq\x14a}q\x15h\x07}q\x16sbX\x06\x00\x00\x00paramsq\x17csnakemake.io\nParams\nq\x18)\x81q\x19}q\x1ah\x07}q\x1bsbX\x07\x00\x00\x00threadsq\x1cK\x01X\t\x00\x00\x00resourcesq\x1dcsnakemake.io\nResources\nq\x1e)\x81q\x1f(K\x01K\x01e}q (X\x06\x00\x00\x00_coresq!K\x01X\x06\x00\x00\x00_nodesq"K\x01h\x07}q#(h"K\x00N\x86q$h!K\x01N\x86q%uubX\x03\x00\x00\x00logq&csnakemake.io\nLog\nq\')\x81q(}q)h\x07}q*sbX\x06\x00\x00\x00configq+}q,(X\x0b\x00\x00\x00directoriesq-}q.(X\x05\x00\x00\x00dbSNPq/X\x06\x00\x00\x00dbSNPsq0X\x06\x00\x00\x00PIPDIRq1}q2(X\x08\x00\x00\x00analysisq3X\x08\x00\x00\x00analysisq4X\x06\x00\x00\x00mappedq5X\x15\x00\x00\x00analysis/mapped_readsq6X\x07\x00\x00\x00metricsq7X\x10\x00\x00\x00analysis/metricsq8uX\x06\x00\x00\x00OUTDIRq9}q:(X\n\x00\x00\x00insertSizeq;X\x0e\x00\x00\x00out/results_QCq<X\x03\x00\x00\x00outq=X\x03\x00\x00\x00outq>X\x06\x00\x00\x00fastqcq?X\x15\x00\x00\x00out/results_QC/fastQCq@uX\x07\x00\x00\x00TEMPDIRqAX\x04\x00\x00\x00tempqBX\x03\x00\x00\x00BINqCX\x03\x00\x00\x00binqDX\x06\x00\x00\x00SAMPLEqEX\x06\x00\x00\x00sampleqFX\t\x00\x00\x00REFERENCEqGX\t\x00\x00\x00referenceqHX\x07\x00\x00\x00SCRIPTSqI}qJ(X\x01\x00\x00\x00RqKX\t\x00\x00\x00scripts/RqLX\x06\x00\x00\x00PythonqMX\x0e\x00\x00\x00scripts/PythonqNX\x05\x00\x00\x00SnakeqOX\r\x00\x00\x00scripts/SnakeqPX\x07\x00\x00\x00scriptsqQX\x07\x00\x00\x00scriptsqRuuX\x07\x00\x00\x00samplesqS}qT(X\x05\x00\x00\x00LANE2qU}qV(X\x07\x00\x00\x00REVERSEqWX\x18\x00\x00\x00LF2017_63_S8_L002_R2_001qXX\x07\x00\x00\x00FORWARDqYX\x18\x00\x00\x00LF2017_63_S8_L002_R1_001qZuX\x05\x00\x00\x00LANE1q[}q\\(hWX\x18\x00\x00\x00LF2017_63_S8_L001_R2_001q]hYX\x18\x00\x00\x00LF2017_63_S8_L001_R1_001q^uuX\x05\x00\x00\x00SETUPq_\x88X\x05\x00\x00\x00toolsq`}qa(X\x06\x00\x00\x00FASTQCqb}qcX\x04\x00\x00\x00callqdX.\x00\x00\x00~/Application/FastQC.app/Contents/MacOS/fastqcqesX\x06\x00\x00\x00PICARDqf}qg(X\x0e\x00\x00\x00MarkDuplicatesqh}qihdX.\x00\x00\x00java -Xmx2G -jar bin/picard.jar MarkDuplicatesqjsX\x18\x00\x00\x00CollectInsertSizeMetricsqk}qlhdX8\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectInsertSizeMetricsqmsX\r\x00\x00\x00MergeSamFilesqn}qohdXE\x00\x00\x00java -XX:ParallelGCThreads=2 -Xmx2G -jar bin/picard.jar MergeSamFilesqpsX\x12\x00\x00\x00FixMateInformationqq}qrhdX2\x00\x00\x00java -Xmx2G -jar bin/picard.jar FixMateInformationqssX\x07\x00\x00\x00SortSamqt}quhdX\'\x00\x00\x00java -Xmx2G -jar bin/picard.jar SortSamqvsX\x1e\x00\x00\x00CollectAlignmentSummaryMetricsqw}qxhdX>\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectAlignmentSummaryMetricsqysuX\x04\x00\x00\x00GATKqz}q{(X\x10\x00\x00\x00BaseRecalibratorq|}q}hdX=\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T BaseRecalibratorq~sX\x0f\x00\x00\x00RealignerTargetq\x7f}q\x80hdXC\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T RealignerTargetCreatorq\x81sX\n\x00\x00\x00PrintReadsq\x82}q\x83hdX7\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T PrintReadsq\x84sX\x0e\x00\x00\x00IndelRealignerq\x85}q\x86hdX;\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T IndelRealignerq\x87suX\x07\x00\x00\x00bwa_memq\x88}q\x89hdX\x07\x00\x00\x00bwa memq\x8asX\x08\x00\x00\x00samtoolsq\x8b}q\x8c(X\x06\x00\x00\x00pileupq\x8d}q\x8ehdX\x16\x00\x00\x00samtools mpileup -g -fq\x8fsX\x08\x00\x00\x00bcftoolsq\x90}q\x91hdX\x14\x00\x00\x00bcftools call -mv ->q\x92suuX\x0e\x00\x00\x00req_file_pathsq\x93}q\x94(h/X(\x00\x00\x00dbSNPs/common_all_20180423_edit_2.vcf.gzq\x95hGX\x19\x00\x00\x00reference/ucsc.hg19.fastaq\x96uuub.')
######## Original script #########


def Mean(d):             #mean function for dictionaries -- assumes dictionary values are counts
	total = 0
	for entry in d:
		total += entry * d[entry]
	return total / sum(d.values())	



insert_distribution = {}  # key -- insert size, value -- count
start_storing = False
out_filename = DIR_METRICS + "/" + SAMPLE_ID + "metrics.insertSize.tsv"

with open(out_filename, 'r') as file_insertsize:
	for line in file_insertsize:
		#print(line)
		data = line.split('\t')
		if start_storing == True and data[0] != '\n':
			#print(data)
			insert_distribution[int(data[0])] = int(data[1])
		if start_storing == False and data[0] == 'insert_size':
			start_storing = True
#print(insert_distribution)
print('Total number of reads: ', sum(insert_distribution.values()))		
print('Average insert size: ', Mean(insert_distribution))

with open('temp/info_insertSize.txt', 'w') as ifile:
	ifile.write('Total number of Reads:\t%i\n' %(sum(insert_distribution.values())))
	ifile.write('Average insert size:\t%f\n' %(Mean(insert_distribution)))
ifile.close()