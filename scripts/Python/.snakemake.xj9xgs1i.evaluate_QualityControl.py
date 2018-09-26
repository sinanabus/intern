
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/sabus/miniconda3/envs/F1-pipe/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04(X\x0e\x00\x00\x00req_file_pathsq\x05}q\x06(X\x05\x00\x00\x00dbSNPq\x07X(\x00\x00\x00dbSNPs/common_all_20180423_edit_2.vcf.gzq\x08X\t\x00\x00\x00REFERENCEq\tX\x19\x00\x00\x00reference/ucsc.hg19.fastaq\nuX\x07\x00\x00\x00samplesq\x0b}q\x0c(X\x05\x00\x00\x00LANE2q\r}q\x0e(X\x07\x00\x00\x00FORWARDq\x0fX\x18\x00\x00\x00LF2017_63_S8_L002_R1_001q\x10X\x07\x00\x00\x00REVERSEq\x11X\x18\x00\x00\x00LF2017_63_S8_L002_R2_001q\x12uX\x05\x00\x00\x00LANE1q\x13}q\x14(h\x0fX\x18\x00\x00\x00LF2017_63_S8_L001_R1_001q\x15h\x11X\x18\x00\x00\x00LF2017_63_S8_L001_R2_001q\x16uuX\x05\x00\x00\x00toolsq\x17}q\x18(X\x08\x00\x00\x00samtoolsq\x19}q\x1a(X\x08\x00\x00\x00bcftoolsq\x1b}q\x1cX\x07\x00\x00\x00varcallq\x1dX\r\x00\x00\x00bcftools callq\x1esX\x06\x00\x00\x00pileupq\x1f}q X\x04\x00\x00\x00callq!X\x10\x00\x00\x00samtools mpileupq"suX\x06\x00\x00\x00FASTQCq#}q$h!X.\x00\x00\x00~/Application/FastQC.app/Contents/MacOS/fastqcq%sX\x06\x00\x00\x00PICARDq&}q\'(X\x18\x00\x00\x00CollectInsertSizeMetricsq(}q)h!X8\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectInsertSizeMetricsq*sX\x0e\x00\x00\x00MarkDuplicatesq+}q,h!X.\x00\x00\x00java -Xmx2G -jar bin/picard.jar MarkDuplicatesq-sX\x12\x00\x00\x00FixMateInformationq.}q/h!X2\x00\x00\x00java -Xmx2G -jar bin/picard.jar FixMateInformationq0sX\r\x00\x00\x00MergeSamFilesq1}q2h!XE\x00\x00\x00java -XX:ParallelGCThreads=2 -Xmx2G -jar bin/picard.jar MergeSamFilesq3sX\x07\x00\x00\x00SortSamq4}q5h!X\'\x00\x00\x00java -Xmx2G -jar bin/picard.jar SortSamq6sX\x1e\x00\x00\x00CollectAlignmentSummaryMetricsq7}q8h!X>\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectAlignmentSummaryMetricsq9suX\x04\x00\x00\x00GATKq:}q;(X\x0e\x00\x00\x00IndelRealignerq<}q=h!X;\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T IndelRealignerq>sX\x10\x00\x00\x00BaseRecalibratorq?}q@h!X=\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T BaseRecalibratorqAsX\x0f\x00\x00\x00RealignerTargetqB}qCh!XC\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T RealignerTargetCreatorqDsX\n\x00\x00\x00PrintReadsqE}qFh!X7\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T PrintReadsqGsuX\x07\x00\x00\x00bwa_memqH}qIh!X\x07\x00\x00\x00bwa memqJsuX\x05\x00\x00\x00SETUPqK\x88X\x0b\x00\x00\x00directoriesqL}qM(X\x07\x00\x00\x00SCRIPTSqN}qO(X\x06\x00\x00\x00PythonqPX\x0e\x00\x00\x00scripts/PythonqQX\x07\x00\x00\x00scriptsqRX\x07\x00\x00\x00scriptsqSX\x01\x00\x00\x00RqTX\t\x00\x00\x00scripts/RqUX\x05\x00\x00\x00SnakeqVX\r\x00\x00\x00scripts/SnakeqWuh\x07X\x06\x00\x00\x00dbSNPsqXX\x06\x00\x00\x00SAMPLEqYX\x06\x00\x00\x00sampleqZh\tX\t\x00\x00\x00referenceq[X\x03\x00\x00\x00BINq\\X\x03\x00\x00\x00binq]X\x07\x00\x00\x00TEMPDIRq^X\x04\x00\x00\x00tempq_X\x06\x00\x00\x00PIPDIRq`}qa(X\x07\x00\x00\x00metricsqbX\x10\x00\x00\x00analysis/metricsqcX\x08\x00\x00\x00analysisqdX\x08\x00\x00\x00analysisqeX\x06\x00\x00\x00mappedqfX\x15\x00\x00\x00analysis/mapped_readsqguX\x06\x00\x00\x00OUTDIRqh}qi(X\x03\x00\x00\x00outqjX\x03\x00\x00\x00outqkX\n\x00\x00\x00insertSizeqlX\x0e\x00\x00\x00out/results_QCqmX\x06\x00\x00\x00fastqcqnX\x15\x00\x00\x00out/results_QC/fastQCqouuuX\x06\x00\x00\x00paramsqpcsnakemake.io\nParams\nqq)\x81qr}qsX\x06\x00\x00\x00_namesqt}qusbX\t\x00\x00\x00wildcardsqvcsnakemake.io\nWildcards\nqw)\x81qx}qyht}qzsbX\x07\x00\x00\x00threadsq{K\x01X\x04\x00\x00\x00ruleq|X\x06\x00\x00\x00reportq}X\x05\x00\x00\x00inputq~csnakemake.io\nInputFiles\nq\x7f)\x81q\x80X1\x00\x00\x00analysis/metrics/LF2017_63_metrics.insertSize.tsvq\x81a}q\x82ht}q\x83sbX\x06\x00\x00\x00outputq\x84csnakemake.io\nOutputFiles\nq\x85)\x81q\x86X\x18\x00\x00\x00temp/info_insertSize.txtq\x87a}q\x88ht}q\x89sbX\x03\x00\x00\x00logq\x8acsnakemake.io\nLog\nq\x8b)\x81q\x8c}q\x8dht}q\x8esbX\t\x00\x00\x00resourcesq\x8fcsnakemake.io\nResources\nq\x90)\x81q\x91(K\x01K\x01e}q\x92(X\x06\x00\x00\x00_coresq\x93K\x01ht}q\x94(X\x06\x00\x00\x00_nodesq\x95K\x00N\x86q\x96h\x93K\x01N\x86q\x97uh\x95K\x01ubub.')
######## Original script #########


def Mean(d):             #mean function for dictionaries -- assumes dictionary values are counts
	total = 0
	for entry in d:
		total += entry * d[entry]
	return total / sum(d.values())	


with open(snakemake.input[0], 'r') as file_insertsize:
	start_storing = False
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