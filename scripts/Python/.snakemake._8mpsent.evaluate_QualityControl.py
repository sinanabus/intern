
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/sabus/miniconda3/envs/F1-pipe/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x06\x00\x00\x00configq\t}q\n(X\x07\x00\x00\x00samplesq\x0b}q\x0c(X\x05\x00\x00\x00LANE1q\r}q\x0e(X\x07\x00\x00\x00REVERSEq\x0fX\x18\x00\x00\x00LF2017_63_S8_L001_R2_001q\x10X\x07\x00\x00\x00FORWARDq\x11X\x18\x00\x00\x00LF2017_63_S8_L001_R1_001q\x12uX\x05\x00\x00\x00LANE2q\x13}q\x14(h\x0fX\x18\x00\x00\x00LF2017_63_S8_L002_R2_001q\x15h\x11X\x18\x00\x00\x00LF2017_63_S8_L002_R1_001q\x16uuX\x0b\x00\x00\x00directoriesq\x17}q\x18(X\x05\x00\x00\x00dbSNPq\x19X\x06\x00\x00\x00dbSNPsq\x1aX\x06\x00\x00\x00PIPDIRq\x1b}q\x1c(X\x07\x00\x00\x00metricsq\x1dX\x10\x00\x00\x00analysis/metricsq\x1eX\x06\x00\x00\x00mappedq\x1fX\x15\x00\x00\x00analysis/mapped_readsq X\x08\x00\x00\x00analysisq!X\x08\x00\x00\x00analysisq"uX\x06\x00\x00\x00SAMPLEq#X\x06\x00\x00\x00sampleq$X\x03\x00\x00\x00BINq%X\x03\x00\x00\x00binq&X\x07\x00\x00\x00SCRIPTSq\'}q((X\x05\x00\x00\x00Snakeq)X\r\x00\x00\x00scripts/Snakeq*X\x06\x00\x00\x00Pythonq+X\x0e\x00\x00\x00scripts/Pythonq,X\x07\x00\x00\x00scriptsq-X\x07\x00\x00\x00scriptsq.X\x01\x00\x00\x00Rq/X\t\x00\x00\x00scripts/Rq0uX\x06\x00\x00\x00OUTDIRq1}q2(X\x06\x00\x00\x00fastqcq3X\x15\x00\x00\x00out/results_QC/fastQCq4X\x03\x00\x00\x00outq5X\x03\x00\x00\x00outq6X\n\x00\x00\x00insertSizeq7X\x0e\x00\x00\x00out/results_QCq8uX\x07\x00\x00\x00TEMPDIRq9X\x04\x00\x00\x00tempq:X\t\x00\x00\x00REFERENCEq;X\t\x00\x00\x00referenceq<uX\x05\x00\x00\x00toolsq=}q>(X\x06\x00\x00\x00PICARDq?}q@(X\x0e\x00\x00\x00MarkDuplicatesqA}qBX\x04\x00\x00\x00callqCX.\x00\x00\x00java -Xmx2G -jar bin/picard.jar MarkDuplicatesqDsX\x12\x00\x00\x00FixMateInformationqE}qFhCX2\x00\x00\x00java -Xmx2G -jar bin/picard.jar FixMateInformationqGsX\x07\x00\x00\x00SortSamqH}qIhCX\'\x00\x00\x00java -Xmx2G -jar bin/picard.jar SortSamqJsX\r\x00\x00\x00MergeSamFilesqK}qLhCXE\x00\x00\x00java -XX:ParallelGCThreads=2 -Xmx2G -jar bin/picard.jar MergeSamFilesqMsX\x1e\x00\x00\x00CollectAlignmentSummaryMetricsqN}qOhCX>\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectAlignmentSummaryMetricsqPsX\x18\x00\x00\x00CollectInsertSizeMetricsqQ}qRhCX8\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectInsertSizeMetricsqSsuX\x07\x00\x00\x00bwa_memqT}qUhCX\x07\x00\x00\x00bwa memqVsX\x08\x00\x00\x00samtoolsqW}qX(X\x08\x00\x00\x00bcftoolsqY}qZhCX\x14\x00\x00\x00bcftools call -mv ->q[sX\x06\x00\x00\x00pileupq\\}q]hCX\x16\x00\x00\x00samtools mpileup -g -fq^suX\x06\x00\x00\x00FASTQCq_}q`hCX.\x00\x00\x00~/Application/FastQC.app/Contents/MacOS/fastqcqasX\x04\x00\x00\x00GATKqb}qc(X\x0e\x00\x00\x00IndelRealignerqd}qehCX;\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T IndelRealignerqfsX\x10\x00\x00\x00BaseRecalibratorqg}qhhCX=\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T BaseRecalibratorqisX\n\x00\x00\x00PrintReadsqj}qkhCX7\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T PrintReadsqlsX\x0f\x00\x00\x00RealignerTargetqm}qnhCXC\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T RealignerTargetCreatorqosuuX\x0e\x00\x00\x00req_file_pathsqp}qq(h\x19X(\x00\x00\x00dbSNPs/common_all_20180423_edit_2.vcf.gzqrh;X\x19\x00\x00\x00reference/ucsc.hg19.fastaqsuX\x05\x00\x00\x00SETUPqt\x88uX\x05\x00\x00\x00inputqucsnakemake.io\nInputFiles\nqv)\x81qwX1\x00\x00\x00analysis/metrics/LF2017_63_metrics.insertSize.tsvqxa}qyh\x07}qzsbX\x06\x00\x00\x00outputq{csnakemake.io\nOutputFiles\nq|)\x81q}X\x18\x00\x00\x00temp/info_insertSize.txtq~a}q\x7fh\x07}q\x80sbX\x03\x00\x00\x00logq\x81csnakemake.io\nLog\nq\x82)\x81q\x83}q\x84h\x07}q\x85sbX\x06\x00\x00\x00paramsq\x86csnakemake.io\nParams\nq\x87)\x81q\x88}q\x89h\x07}q\x8asbX\t\x00\x00\x00resourcesq\x8bcsnakemake.io\nResources\nq\x8c)\x81q\x8d(K\x01K\x01e}q\x8e(X\x06\x00\x00\x00_nodesq\x8fK\x01h\x07}q\x90(h\x8fK\x01N\x86q\x91X\x06\x00\x00\x00_coresq\x92K\x00N\x86q\x93uh\x92K\x01ubX\x04\x00\x00\x00ruleq\x94X\x06\x00\x00\x00reportq\x95X\x07\x00\x00\x00threadsq\x96K\x01ub.')
######## Original script #########


def Mean(d):             #mean function for dictionaries -- assumes dictionary values are counts
	total = 0
	for entry in d:
		total += entry * d[entry]
	return total / sum(d.values())	



insert_distribution = {}  # key -- insert size, value -- count
start_storing = False
out_filename = expand("{dir_metrics}/{sample_id}_metrics.insertSize.tsv", dir_metrics = DIR_METRICS, sample_id = SAMPLE_ID)

with open(out_filename[0], 'r') as file_insertsize:
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