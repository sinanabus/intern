
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/sabus/miniconda3/envs/F1-pipe/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x06\x00\x00\x00outputq\tcsnakemake.io\nOutputFiles\nq\n)\x81q\x0bX\x18\x00\x00\x00temp/info_insertSize.txtq\x0ca}q\rh\x07}q\x0esbX\x06\x00\x00\x00paramsq\x0fcsnakemake.io\nParams\nq\x10)\x81q\x11}q\x12h\x07}q\x13sbX\x06\x00\x00\x00configq\x14}q\x15(X\x05\x00\x00\x00toolsq\x16}q\x17(X\x06\x00\x00\x00FASTQCq\x18}q\x19X\x04\x00\x00\x00callq\x1aX.\x00\x00\x00~/Application/FastQC.app/Contents/MacOS/fastqcq\x1bsX\x04\x00\x00\x00GATKq\x1c}q\x1d(X\x10\x00\x00\x00BaseRecalibratorq\x1e}q\x1fh\x1aX=\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T BaseRecalibratorq sX\x0e\x00\x00\x00IndelRealignerq!}q"h\x1aX;\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T IndelRealignerq#sX\x0f\x00\x00\x00RealignerTargetq$}q%h\x1aXC\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T RealignerTargetCreatorq&sX\n\x00\x00\x00PrintReadsq\'}q(h\x1aX7\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T PrintReadsq)suX\x07\x00\x00\x00bwa_memq*}q+h\x1aX\x07\x00\x00\x00bwa memq,sX\x08\x00\x00\x00samtoolsq-}q.(X\x08\x00\x00\x00bcftoolsq/}q0X\x07\x00\x00\x00varcallq1X\r\x00\x00\x00bcftools callq2sX\x06\x00\x00\x00pileupq3}q4h\x1aX\x10\x00\x00\x00samtools mpileupq5suX\x06\x00\x00\x00PICARDq6}q7(X\x12\x00\x00\x00FixMateInformationq8}q9h\x1aX2\x00\x00\x00java -Xmx2G -jar bin/picard.jar FixMateInformationq:sX\r\x00\x00\x00MergeSamFilesq;}q<h\x1aXE\x00\x00\x00java -XX:ParallelGCThreads=2 -Xmx2G -jar bin/picard.jar MergeSamFilesq=sX\x1e\x00\x00\x00CollectAlignmentSummaryMetricsq>}q?h\x1aX>\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectAlignmentSummaryMetricsq@sX\x18\x00\x00\x00CollectInsertSizeMetricsqA}qBh\x1aX8\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectInsertSizeMetricsqCsX\x0e\x00\x00\x00MarkDuplicatesqD}qEh\x1aX.\x00\x00\x00java -Xmx2G -jar bin/picard.jar MarkDuplicatesqFsX\x07\x00\x00\x00SortSamqG}qHh\x1aX\'\x00\x00\x00java -Xmx2G -jar bin/picard.jar SortSamqIsuuX\x05\x00\x00\x00SETUPqJ\x88X\x0e\x00\x00\x00req_file_pathsqK}qL(X\t\x00\x00\x00REFERENCEqMX\x19\x00\x00\x00reference/ucsc.hg19.fastaqNX\x05\x00\x00\x00dbSNPqOX(\x00\x00\x00dbSNPs/common_all_20180423_edit_2.vcf.gzqPuX\x07\x00\x00\x00samplesqQ}qR(X\x05\x00\x00\x00LANE1qS}qT(X\x07\x00\x00\x00FORWARDqUX\x18\x00\x00\x00LF2017_63_S8_L001_R1_001qVX\x07\x00\x00\x00REVERSEqWX\x18\x00\x00\x00LF2017_63_S8_L001_R2_001qXuX\x05\x00\x00\x00LANE2qY}qZ(hUX\x18\x00\x00\x00LF2017_63_S8_L002_R1_001q[hWX\x18\x00\x00\x00LF2017_63_S8_L002_R2_001q\\uuX\x0b\x00\x00\x00directoriesq]}q^(X\x06\x00\x00\x00OUTDIRq_}q`(X\x03\x00\x00\x00outqaX\x03\x00\x00\x00outqbX\x06\x00\x00\x00fastqcqcX\x15\x00\x00\x00out/results_QC/fastQCqdX\n\x00\x00\x00insertSizeqeX\x0e\x00\x00\x00out/results_QCqfuX\x06\x00\x00\x00SAMPLEqgX\x06\x00\x00\x00sampleqhhOX\x06\x00\x00\x00dbSNPsqiX\x06\x00\x00\x00PIPDIRqj}qk(X\x06\x00\x00\x00mappedqlX\x15\x00\x00\x00analysis/mapped_readsqmX\x07\x00\x00\x00metricsqnX\x10\x00\x00\x00analysis/metricsqoX\x08\x00\x00\x00analysisqpX\x08\x00\x00\x00analysisqquX\x07\x00\x00\x00TEMPDIRqrX\x04\x00\x00\x00tempqshMX\t\x00\x00\x00referenceqtX\x07\x00\x00\x00SCRIPTSqu}qv(X\x06\x00\x00\x00PythonqwX\x0e\x00\x00\x00scripts/PythonqxX\x05\x00\x00\x00SnakeqyX\r\x00\x00\x00scripts/SnakeqzX\x07\x00\x00\x00scriptsq{X\x07\x00\x00\x00scriptsq|X\x01\x00\x00\x00Rq}X\t\x00\x00\x00scripts/Rq~uX\x03\x00\x00\x00BINq\x7fX\x03\x00\x00\x00binq\x80uuX\x04\x00\x00\x00ruleq\x81X\x06\x00\x00\x00reportq\x82X\t\x00\x00\x00resourcesq\x83csnakemake.io\nResources\nq\x84)\x81q\x85(K\x01K\x01e}q\x86(h\x07}q\x87(X\x06\x00\x00\x00_nodesq\x88K\x00N\x86q\x89X\x06\x00\x00\x00_coresq\x8aK\x01N\x86q\x8buh\x8aK\x01h\x88K\x01ubX\x05\x00\x00\x00inputq\x8ccsnakemake.io\nInputFiles\nq\x8d)\x81q\x8eX1\x00\x00\x00analysis/metrics/LF2017_63_metrics.insertSize.tsvq\x8fa}q\x90h\x07}q\x91sbX\t\x00\x00\x00wildcardsq\x92csnakemake.io\nWildcards\nq\x93)\x81q\x94}q\x95h\x07}q\x96sbX\x07\x00\x00\x00threadsq\x97K\x01ub.')
######## Original script #########


def Mean(d):             #mean function for dictionaries -- assumes dictionary values are counts
	total = 0
	for entry in d:
		total += entry * d[entry]
	return total / sum(d.values())	


with open(snakemake.input[0], 'r') as file_insertsize:
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