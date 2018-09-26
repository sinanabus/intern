
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/sabus/miniconda3/envs/F1-pipe/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04(X\x0e\x00\x00\x00req_file_pathsq\x05}q\x06(X\x05\x00\x00\x00dbSNPq\x07X(\x00\x00\x00dbSNPs/common_all_20180423_edit_2.vcf.gzq\x08X\t\x00\x00\x00REFERENCEq\tX\x19\x00\x00\x00reference/ucsc.hg19.fastaq\nuX\x0b\x00\x00\x00directoriesq\x0b}q\x0c(h\x07X\x06\x00\x00\x00dbSNPsq\rh\tX\t\x00\x00\x00referenceq\x0eX\x03\x00\x00\x00BINq\x0fX\x03\x00\x00\x00binq\x10X\x07\x00\x00\x00SCRIPTSq\x11}q\x12(X\x07\x00\x00\x00scriptsq\x13X\x07\x00\x00\x00scriptsq\x14X\x05\x00\x00\x00Snakeq\x15X\r\x00\x00\x00scripts/Snakeq\x16X\x06\x00\x00\x00Pythonq\x17X\x0e\x00\x00\x00scripts/Pythonq\x18X\x01\x00\x00\x00Rq\x19X\t\x00\x00\x00scripts/Rq\x1auX\x06\x00\x00\x00OUTDIRq\x1b}q\x1c(X\n\x00\x00\x00insertSizeq\x1dX\x0e\x00\x00\x00out/results_QCq\x1eX\x06\x00\x00\x00fastqcq\x1fX\x15\x00\x00\x00out/results_QC/fastQCq X\x03\x00\x00\x00outq!X\x03\x00\x00\x00outq"uX\x06\x00\x00\x00SAMPLEq#X\x06\x00\x00\x00sampleq$X\x07\x00\x00\x00TEMPDIRq%X\x04\x00\x00\x00tempq&X\x06\x00\x00\x00PIPDIRq\'}q((X\x07\x00\x00\x00metricsq)X\x10\x00\x00\x00analysis/metricsq*X\x08\x00\x00\x00analysisq+X\x08\x00\x00\x00analysisq,X\x06\x00\x00\x00mappedq-X\x15\x00\x00\x00analysis/mapped_readsq.uuX\x05\x00\x00\x00SETUPq/\x88X\x05\x00\x00\x00toolsq0}q1(X\x06\x00\x00\x00PICARDq2}q3(X\x12\x00\x00\x00FixMateInformationq4}q5X\x04\x00\x00\x00callq6X2\x00\x00\x00java -Xmx2G -jar bin/picard.jar FixMateInformationq7sX\x1e\x00\x00\x00CollectAlignmentSummaryMetricsq8}q9h6X>\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectAlignmentSummaryMetricsq:sX\r\x00\x00\x00MergeSamFilesq;}q<h6XE\x00\x00\x00java -XX:ParallelGCThreads=2 -Xmx2G -jar bin/picard.jar MergeSamFilesq=sX\x0e\x00\x00\x00MarkDuplicatesq>}q?h6X.\x00\x00\x00java -Xmx2G -jar bin/picard.jar MarkDuplicatesq@sX\x18\x00\x00\x00CollectInsertSizeMetricsqA}qBh6X8\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectInsertSizeMetricsqCsX\x07\x00\x00\x00SortSamqD}qEh6X\'\x00\x00\x00java -Xmx2G -jar bin/picard.jar SortSamqFsuX\x04\x00\x00\x00GATKqG}qH(X\x0e\x00\x00\x00IndelRealignerqI}qJh6X;\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T IndelRealignerqKsX\x0f\x00\x00\x00RealignerTargetqL}qMh6XC\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T RealignerTargetCreatorqNsX\x10\x00\x00\x00BaseRecalibratorqO}qPh6X=\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T BaseRecalibratorqQsX\n\x00\x00\x00PrintReadsqR}qSh6X7\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T PrintReadsqTsuX\x08\x00\x00\x00samtoolsqU}qV(X\x06\x00\x00\x00pileupqW}qXh6X\x16\x00\x00\x00samtools mpileup -g -fqYsX\x08\x00\x00\x00bcftoolsqZ}q[h6X\x14\x00\x00\x00bcftools call -mv ->q\\suX\x06\x00\x00\x00FASTQCq]}q^h6X.\x00\x00\x00~/Application/FastQC.app/Contents/MacOS/fastqcq_sX\x07\x00\x00\x00bwa_memq`}qah6X\x07\x00\x00\x00bwa memqbsuX\x07\x00\x00\x00samplesqc}qd(X\x05\x00\x00\x00LANE2qe}qf(X\x07\x00\x00\x00REVERSEqgX\x18\x00\x00\x00LF2017_63_S8_L002_R2_001qhX\x07\x00\x00\x00FORWARDqiX\x18\x00\x00\x00LF2017_63_S8_L002_R1_001qjuX\x05\x00\x00\x00LANE1qk}ql(hgX\x18\x00\x00\x00LF2017_63_S8_L001_R2_001qmhiX\x18\x00\x00\x00LF2017_63_S8_L001_R1_001qnuuuX\x03\x00\x00\x00logqocsnakemake.io\nLog\nqp)\x81qq}qrX\x06\x00\x00\x00_namesqs}qtsbX\x06\x00\x00\x00outputqucsnakemake.io\nOutputFiles\nqv)\x81qwX\x18\x00\x00\x00temp/info_insertSize.txtqxa}qyhs}qzsbX\x07\x00\x00\x00threadsq{K\x01X\x06\x00\x00\x00paramsq|csnakemake.io\nParams\nq})\x81q~}q\x7fhs}q\x80sbX\t\x00\x00\x00wildcardsq\x81csnakemake.io\nWildcards\nq\x82)\x81q\x83}q\x84hs}q\x85sbX\x05\x00\x00\x00inputq\x86csnakemake.io\nInputFiles\nq\x87)\x81q\x88X1\x00\x00\x00analysis/metrics/LF2017_63_metrics.insertSize.tsvq\x89a}q\x8ahs}q\x8bsbX\t\x00\x00\x00resourcesq\x8ccsnakemake.io\nResources\nq\x8d)\x81q\x8e(K\x01K\x01e}q\x8f(hs}q\x90(X\x06\x00\x00\x00_coresq\x91K\x00N\x86q\x92X\x06\x00\x00\x00_nodesq\x93K\x01N\x86q\x94uh\x91K\x01h\x93K\x01ubX\x04\x00\x00\x00ruleq\x95X\x06\x00\x00\x00reportq\x96ub.')
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