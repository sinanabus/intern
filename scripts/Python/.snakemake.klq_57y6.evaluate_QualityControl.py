
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/sabus/miniconda3/envs/F1-pipe/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05X\x18\x00\x00\x00temp/info_insertSize.txtq\x06a}q\x07X\x06\x00\x00\x00_namesq\x08}q\tsbX\t\x00\x00\x00resourcesq\ncsnakemake.io\nResources\nq\x0b)\x81q\x0c(K\x01K\x01e}q\r(X\x06\x00\x00\x00_coresq\x0eK\x01X\x06\x00\x00\x00_nodesq\x0fK\x01h\x08}q\x10(h\x0eK\x00N\x86q\x11h\x0fK\x01N\x86q\x12uubX\x07\x00\x00\x00threadsq\x13K\x01X\t\x00\x00\x00wildcardsq\x14csnakemake.io\nWildcards\nq\x15)\x81q\x16}q\x17h\x08}q\x18sbX\x04\x00\x00\x00ruleq\x19X\x06\x00\x00\x00reportq\x1aX\x06\x00\x00\x00configq\x1b}q\x1c(X\x0b\x00\x00\x00directoriesq\x1d}q\x1e(X\x06\x00\x00\x00PIPDIRq\x1f}q (X\x06\x00\x00\x00mappedq!X\x15\x00\x00\x00analysis/mapped_readsq"X\x07\x00\x00\x00metricsq#X\x10\x00\x00\x00analysis/metricsq$X\x08\x00\x00\x00analysisq%X\x08\x00\x00\x00analysisq&uX\t\x00\x00\x00REFERENCEq\'X\t\x00\x00\x00referenceq(X\x03\x00\x00\x00BINq)X\x03\x00\x00\x00binq*X\x05\x00\x00\x00dbSNPq+X\x06\x00\x00\x00dbSNPsq,X\x06\x00\x00\x00OUTDIRq-}q.(X\x03\x00\x00\x00outq/X\x03\x00\x00\x00outq0X\x06\x00\x00\x00fastqcq1X\x15\x00\x00\x00out/results_QC/fastQCq2X\n\x00\x00\x00insertSizeq3X\x0e\x00\x00\x00out/results_QCq4uX\x06\x00\x00\x00SAMPLEq5X\x06\x00\x00\x00sampleq6X\x07\x00\x00\x00SCRIPTSq7}q8(X\x06\x00\x00\x00Pythonq9X\x0e\x00\x00\x00scripts/Pythonq:X\x05\x00\x00\x00Snakeq;X\r\x00\x00\x00scripts/Snakeq<X\x01\x00\x00\x00Rq=X\t\x00\x00\x00scripts/Rq>X\x07\x00\x00\x00scriptsq?X\x07\x00\x00\x00scriptsq@uX\x07\x00\x00\x00TEMPDIRqAX\x04\x00\x00\x00tempqBuX\x05\x00\x00\x00toolsqC}qD(X\x04\x00\x00\x00GATKqE}qF(X\x10\x00\x00\x00BaseRecalibratorqG}qHX\x04\x00\x00\x00callqIX=\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T BaseRecalibratorqJsX\x0e\x00\x00\x00IndelRealignerqK}qLhIX;\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T IndelRealignerqMsX\x0f\x00\x00\x00RealignerTargetqN}qOhIXC\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T RealignerTargetCreatorqPsX\n\x00\x00\x00PrintReadsqQ}qRhIX7\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T PrintReadsqSsuX\x06\x00\x00\x00FASTQCqT}qUhIX.\x00\x00\x00~/Application/FastQC.app/Contents/MacOS/fastqcqVsX\x06\x00\x00\x00PICARDqW}qX(X\x07\x00\x00\x00SortSamqY}qZhIX\'\x00\x00\x00java -Xmx2G -jar bin/picard.jar SortSamq[sX\x12\x00\x00\x00FixMateInformationq\\}q]hIX2\x00\x00\x00java -Xmx2G -jar bin/picard.jar FixMateInformationq^sX\x0e\x00\x00\x00MarkDuplicatesq_}q`hIX.\x00\x00\x00java -Xmx2G -jar bin/picard.jar MarkDuplicatesqasX\x18\x00\x00\x00CollectInsertSizeMetricsqb}qchIX8\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectInsertSizeMetricsqdsX\r\x00\x00\x00MergeSamFilesqe}qfhIXE\x00\x00\x00java -XX:ParallelGCThreads=2 -Xmx2G -jar bin/picard.jar MergeSamFilesqgsX\x1e\x00\x00\x00CollectAlignmentSummaryMetricsqh}qihIX>\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectAlignmentSummaryMetricsqjsuX\x07\x00\x00\x00bwa_memqk}qlhIX\x07\x00\x00\x00bwa memqmsX\x08\x00\x00\x00samtoolsqn}qo(X\x06\x00\x00\x00pileupqp}qqhIX\x10\x00\x00\x00samtools mpileupqrsX\x08\x00\x00\x00bcftoolsqs}qtX\x07\x00\x00\x00varcallquX\r\x00\x00\x00bcftools callqvsuuX\x07\x00\x00\x00samplesqw}qx(X\x05\x00\x00\x00LANE2qy}qz(X\x07\x00\x00\x00REVERSEq{X\x18\x00\x00\x00LF2017_63_S8_L002_R2_001q|X\x07\x00\x00\x00FORWARDq}X\x18\x00\x00\x00LF2017_63_S8_L002_R1_001q~uX\x05\x00\x00\x00LANE1q\x7f}q\x80(h{X\x18\x00\x00\x00LF2017_63_S8_L001_R2_001q\x81h}X\x18\x00\x00\x00LF2017_63_S8_L001_R1_001q\x82uuX\x05\x00\x00\x00SETUPq\x83\x88X\x0e\x00\x00\x00req_file_pathsq\x84}q\x85(h\'X\x19\x00\x00\x00reference/ucsc.hg19.fastaq\x86h+X(\x00\x00\x00dbSNPs/common_all_20180423_edit_2.vcf.gzq\x87uuX\x05\x00\x00\x00inputq\x88csnakemake.io\nInputFiles\nq\x89)\x81q\x8aX1\x00\x00\x00analysis/metrics/LF2017_63_metrics.insertSize.tsvq\x8ba}q\x8ch\x08}q\x8dsbX\x06\x00\x00\x00paramsq\x8ecsnakemake.io\nParams\nq\x8f)\x81q\x90}q\x91h\x08}q\x92sbX\x03\x00\x00\x00logq\x93csnakemake.io\nLog\nq\x94)\x81q\x95}q\x96h\x08}q\x97sbub.')
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