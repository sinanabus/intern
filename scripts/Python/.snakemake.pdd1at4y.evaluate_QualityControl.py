
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/sabus/miniconda3/envs/F1-pipe/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04(X\x07\x00\x00\x00samplesq\x05}q\x06(X\x05\x00\x00\x00LANE1q\x07}q\x08(X\x07\x00\x00\x00FORWARDq\tX\x18\x00\x00\x00LF2017_63_S8_L001_R1_001q\nX\x07\x00\x00\x00REVERSEq\x0bX\x18\x00\x00\x00LF2017_63_S8_L001_R2_001q\x0cuX\x05\x00\x00\x00LANE2q\r}q\x0e(h\tX\x18\x00\x00\x00LF2017_63_S8_L002_R1_001q\x0fh\x0bX\x18\x00\x00\x00LF2017_63_S8_L002_R2_001q\x10uuX\x0e\x00\x00\x00req_file_pathsq\x11}q\x12(X\x05\x00\x00\x00dbSNPq\x13X(\x00\x00\x00dbSNPs/common_all_20180423_edit_2.vcf.gzq\x14X\t\x00\x00\x00REFERENCEq\x15X\x19\x00\x00\x00reference/ucsc.hg19.fastaq\x16uX\x05\x00\x00\x00SETUPq\x17\x88X\x0b\x00\x00\x00directoriesq\x18}q\x19(h\x13X\x06\x00\x00\x00dbSNPsq\x1aX\x07\x00\x00\x00SCRIPTSq\x1b}q\x1c(X\x01\x00\x00\x00Rq\x1dX\t\x00\x00\x00scripts/Rq\x1eX\x06\x00\x00\x00Pythonq\x1fX\x0e\x00\x00\x00scripts/Pythonq X\x07\x00\x00\x00scriptsq!X\x07\x00\x00\x00scriptsq"X\x05\x00\x00\x00Snakeq#X\r\x00\x00\x00scripts/Snakeq$uX\x06\x00\x00\x00OUTDIRq%}q&(X\n\x00\x00\x00insertSizeq\'X\x0e\x00\x00\x00out/results_QCq(X\x03\x00\x00\x00outq)X\x03\x00\x00\x00outq*X\x06\x00\x00\x00fastqcq+X\x15\x00\x00\x00out/results_QC/fastQCq,uX\x06\x00\x00\x00PIPDIRq-}q.(X\x06\x00\x00\x00mappedq/X\x15\x00\x00\x00analysis/mapped_readsq0X\x08\x00\x00\x00analysisq1X\x08\x00\x00\x00analysisq2X\x07\x00\x00\x00metricsq3X\x10\x00\x00\x00analysis/metricsq4uh\x15X\t\x00\x00\x00referenceq5X\x07\x00\x00\x00TEMPDIRq6X\x04\x00\x00\x00tempq7X\x03\x00\x00\x00BINq8X\x03\x00\x00\x00binq9X\x06\x00\x00\x00SAMPLEq:X\x06\x00\x00\x00sampleq;uX\x05\x00\x00\x00toolsq<}q=(X\x07\x00\x00\x00bwa_memq>}q?X\x04\x00\x00\x00callq@X\x07\x00\x00\x00bwa memqAsX\x04\x00\x00\x00GATKqB}qC(X\x0f\x00\x00\x00RealignerTargetqD}qEh@XC\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T RealignerTargetCreatorqFsX\x10\x00\x00\x00BaseRecalibratorqG}qHh@X=\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T BaseRecalibratorqIsX\n\x00\x00\x00PrintReadsqJ}qKh@X7\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T PrintReadsqLsX\x0e\x00\x00\x00IndelRealignerqM}qNh@X;\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T IndelRealignerqOsuX\x08\x00\x00\x00samtoolsqP}qQ(X\x08\x00\x00\x00bcftoolsqR}qSh@X\r\x00\x00\x00bcftools callqTsX\x06\x00\x00\x00pileupqU}qVh@X\x10\x00\x00\x00samtools mpileupqWsuX\x06\x00\x00\x00FASTQCqX}qYh@X.\x00\x00\x00~/Application/FastQC.app/Contents/MacOS/fastqcqZsX\x06\x00\x00\x00PICARDq[}q\\(X\x1e\x00\x00\x00CollectAlignmentSummaryMetricsq]}q^h@X>\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectAlignmentSummaryMetricsq_sX\r\x00\x00\x00MergeSamFilesq`}qah@XE\x00\x00\x00java -XX:ParallelGCThreads=2 -Xmx2G -jar bin/picard.jar MergeSamFilesqbsX\x18\x00\x00\x00CollectInsertSizeMetricsqc}qdh@X8\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectInsertSizeMetricsqesX\x07\x00\x00\x00SortSamqf}qgh@X\'\x00\x00\x00java -Xmx2G -jar bin/picard.jar SortSamqhsX\x0e\x00\x00\x00MarkDuplicatesqi}qjh@X.\x00\x00\x00java -Xmx2G -jar bin/picard.jar MarkDuplicatesqksX\x12\x00\x00\x00FixMateInformationql}qmh@X2\x00\x00\x00java -Xmx2G -jar bin/picard.jar FixMateInformationqnsuuuX\t\x00\x00\x00wildcardsqocsnakemake.io\nWildcards\nqp)\x81qq}qrX\x06\x00\x00\x00_namesqs}qtsbX\x05\x00\x00\x00inputqucsnakemake.io\nInputFiles\nqv)\x81qwX1\x00\x00\x00analysis/metrics/LF2017_63_metrics.insertSize.tsvqxa}qyhs}qzsbX\x07\x00\x00\x00threadsq{K\x01X\x06\x00\x00\x00outputq|csnakemake.io\nOutputFiles\nq})\x81q~X\x18\x00\x00\x00temp/info_insertSize.txtq\x7fa}q\x80hs}q\x81sbX\x06\x00\x00\x00paramsq\x82csnakemake.io\nParams\nq\x83)\x81q\x84}q\x85hs}q\x86sbX\t\x00\x00\x00resourcesq\x87csnakemake.io\nResources\nq\x88)\x81q\x89(K\x01K\x01e}q\x8a(X\x06\x00\x00\x00_nodesq\x8bK\x01hs}q\x8c(h\x8bK\x00N\x86q\x8dX\x06\x00\x00\x00_coresq\x8eK\x01N\x86q\x8fuh\x8eK\x01ubX\x04\x00\x00\x00ruleq\x90X\x06\x00\x00\x00reportq\x91X\x03\x00\x00\x00logq\x92csnakemake.io\nLog\nq\x93)\x81q\x94}q\x95hs}q\x96sbub.')
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