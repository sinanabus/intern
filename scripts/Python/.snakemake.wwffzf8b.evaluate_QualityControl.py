
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/sabus/miniconda3/envs/F1-pipe/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x05\x00\x00\x00inputq\x04csnakemake.io\nInputFiles\nq\x05)\x81q\x06X1\x00\x00\x00analysis/metrics/LF2017_63_metrics.insertSize.tsvq\x07a}q\x08X\x06\x00\x00\x00_namesq\t}q\nsbX\x06\x00\x00\x00outputq\x0bcsnakemake.io\nOutputFiles\nq\x0c)\x81q\rX\x18\x00\x00\x00temp/info_insertSize.txtq\x0ea}q\x0fh\t}q\x10sbX\x06\x00\x00\x00configq\x11}q\x12(X\x0b\x00\x00\x00directoriesq\x13}q\x14(X\t\x00\x00\x00REFERENCEq\x15X\t\x00\x00\x00referenceq\x16X\x07\x00\x00\x00SCRIPTSq\x17}q\x18(X\x01\x00\x00\x00Rq\x19X\t\x00\x00\x00scripts/Rq\x1aX\x06\x00\x00\x00Pythonq\x1bX\x0e\x00\x00\x00scripts/Pythonq\x1cX\x05\x00\x00\x00Snakeq\x1dX\r\x00\x00\x00scripts/Snakeq\x1eX\x07\x00\x00\x00scriptsq\x1fX\x07\x00\x00\x00scriptsq uX\x03\x00\x00\x00BINq!X\x03\x00\x00\x00binq"X\x05\x00\x00\x00dbSNPq#X\x06\x00\x00\x00dbSNPsq$X\x06\x00\x00\x00SAMPLEq%X\x06\x00\x00\x00sampleq&X\x07\x00\x00\x00TEMPDIRq\'X\x04\x00\x00\x00tempq(X\x06\x00\x00\x00OUTDIRq)}q*(X\x03\x00\x00\x00outq+X\x03\x00\x00\x00outq,X\n\x00\x00\x00insertSizeq-X\x0e\x00\x00\x00out/results_QCq.X\x06\x00\x00\x00fastqcq/X\x15\x00\x00\x00out/results_QC/fastQCq0uX\x06\x00\x00\x00PIPDIRq1}q2(X\x07\x00\x00\x00metricsq3X\x10\x00\x00\x00analysis/metricsq4X\x08\x00\x00\x00analysisq5X\x08\x00\x00\x00analysisq6X\x06\x00\x00\x00mappedq7X\x15\x00\x00\x00analysis/mapped_readsq8uuX\x05\x00\x00\x00toolsq9}q:(X\x06\x00\x00\x00PICARDq;}q<(X\x18\x00\x00\x00CollectInsertSizeMetricsq=}q>X\x04\x00\x00\x00callq?X8\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectInsertSizeMetricsq@sX\x0e\x00\x00\x00MarkDuplicatesqA}qBh?X.\x00\x00\x00java -Xmx2G -jar bin/picard.jar MarkDuplicatesqCsX\x07\x00\x00\x00SortSamqD}qEh?X\'\x00\x00\x00java -Xmx2G -jar bin/picard.jar SortSamqFsX\r\x00\x00\x00MergeSamFilesqG}qHh?XE\x00\x00\x00java -XX:ParallelGCThreads=2 -Xmx2G -jar bin/picard.jar MergeSamFilesqIsX\x1e\x00\x00\x00CollectAlignmentSummaryMetricsqJ}qKh?X>\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectAlignmentSummaryMetricsqLsX\x12\x00\x00\x00FixMateInformationqM}qNh?X2\x00\x00\x00java -Xmx2G -jar bin/picard.jar FixMateInformationqOsuX\x04\x00\x00\x00GATKqP}qQ(X\x0f\x00\x00\x00RealignerTargetqR}qSh?XC\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T RealignerTargetCreatorqTsX\n\x00\x00\x00PrintReadsqU}qVh?X7\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T PrintReadsqWsX\x0e\x00\x00\x00IndelRealignerqX}qYh?X;\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T IndelRealignerqZsX\x10\x00\x00\x00BaseRecalibratorq[}q\\h?X=\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T BaseRecalibratorq]suX\x08\x00\x00\x00samtoolsq^}q_(X\x06\x00\x00\x00pileupq`}qah?X\x16\x00\x00\x00samtools mpileup -g -fqbsX\x08\x00\x00\x00bcftoolsqc}qdh?X\x14\x00\x00\x00bcftools call -mv ->qesuX\x07\x00\x00\x00bwa_memqf}qgh?X\x07\x00\x00\x00bwa memqhsX\x06\x00\x00\x00FASTQCqi}qjh?X.\x00\x00\x00~/Application/FastQC.app/Contents/MacOS/fastqcqksuX\x07\x00\x00\x00samplesql}qm(X\x05\x00\x00\x00LANE2qn}qo(X\x07\x00\x00\x00FORWARDqpX\x18\x00\x00\x00LF2017_63_S8_L002_R1_001qqX\x07\x00\x00\x00REVERSEqrX\x18\x00\x00\x00LF2017_63_S8_L002_R2_001qsuX\x05\x00\x00\x00LANE1qt}qu(hpX\x18\x00\x00\x00LF2017_63_S8_L001_R1_001qvhrX\x18\x00\x00\x00LF2017_63_S8_L001_R2_001qwuuX\x05\x00\x00\x00SETUPqx\x88X\x0e\x00\x00\x00req_file_pathsqy}qz(h\x15X\x19\x00\x00\x00reference/ucsc.hg19.fastaq{h#X(\x00\x00\x00dbSNPs/common_all_20180423_edit_2.vcf.gzq|uuX\x03\x00\x00\x00logq}csnakemake.io\nLog\nq~)\x81q\x7f}q\x80h\t}q\x81sbX\x04\x00\x00\x00ruleq\x82X\x06\x00\x00\x00reportq\x83X\t\x00\x00\x00wildcardsq\x84csnakemake.io\nWildcards\nq\x85)\x81q\x86}q\x87h\t}q\x88sbX\x06\x00\x00\x00paramsq\x89csnakemake.io\nParams\nq\x8a)\x81q\x8b}q\x8ch\t}q\x8dsbX\t\x00\x00\x00resourcesq\x8ecsnakemake.io\nResources\nq\x8f)\x81q\x90(K\x01K\x01e}q\x91(h\t}q\x92(X\x06\x00\x00\x00_nodesq\x93K\x00N\x86q\x94X\x06\x00\x00\x00_coresq\x95K\x01N\x86q\x96uh\x93K\x01h\x95K\x01ubub.')
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