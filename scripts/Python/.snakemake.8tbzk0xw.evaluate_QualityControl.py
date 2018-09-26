
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/sabus/miniconda3/envs/F1-pipe/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\t\x00\x00\x00resourcesq\tcsnakemake.io\nResources\nq\n)\x81q\x0b(K\x01K\x01e}q\x0c(X\x06\x00\x00\x00_nodesq\rK\x01X\x06\x00\x00\x00_coresq\x0eK\x01h\x07}q\x0f(h\rK\x00N\x86q\x10h\x0eK\x01N\x86q\x11uubX\x07\x00\x00\x00threadsq\x12K\x01X\x04\x00\x00\x00ruleq\x13X\x06\x00\x00\x00reportq\x14X\x06\x00\x00\x00configq\x15}q\x16(X\x05\x00\x00\x00toolsq\x17}q\x18(X\x06\x00\x00\x00PICARDq\x19}q\x1a(X\x0e\x00\x00\x00MarkDuplicatesq\x1b}q\x1cX\x04\x00\x00\x00callq\x1dX.\x00\x00\x00java -Xmx2G -jar bin/picard.jar MarkDuplicatesq\x1esX\x1e\x00\x00\x00CollectAlignmentSummaryMetricsq\x1f}q h\x1dX>\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectAlignmentSummaryMetricsq!sX\x12\x00\x00\x00FixMateInformationq"}q#h\x1dX2\x00\x00\x00java -Xmx2G -jar bin/picard.jar FixMateInformationq$sX\x07\x00\x00\x00SortSamq%}q&h\x1dX\'\x00\x00\x00java -Xmx2G -jar bin/picard.jar SortSamq\'sX\r\x00\x00\x00MergeSamFilesq(}q)h\x1dXE\x00\x00\x00java -XX:ParallelGCThreads=2 -Xmx2G -jar bin/picard.jar MergeSamFilesq*sX\x18\x00\x00\x00CollectInsertSizeMetricsq+}q,h\x1dX8\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectInsertSizeMetricsq-suX\x04\x00\x00\x00GATKq.}q/(X\x10\x00\x00\x00BaseRecalibratorq0}q1h\x1dX=\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T BaseRecalibratorq2sX\n\x00\x00\x00PrintReadsq3}q4h\x1dX7\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T PrintReadsq5sX\x0f\x00\x00\x00RealignerTargetq6}q7h\x1dXC\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T RealignerTargetCreatorq8sX\x0e\x00\x00\x00IndelRealignerq9}q:h\x1dX;\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T IndelRealignerq;suX\x07\x00\x00\x00bwa_memq<}q=h\x1dX\x07\x00\x00\x00bwa memq>sX\x06\x00\x00\x00FASTQCq?}q@h\x1dX.\x00\x00\x00~/Application/FastQC.app/Contents/MacOS/fastqcqAsX\x08\x00\x00\x00samtoolsqB}qC(X\x06\x00\x00\x00pileupqD}qEh\x1dX\x16\x00\x00\x00samtools mpileup -g -fqFsX\x08\x00\x00\x00bcftoolsqG}qHh\x1dX\x14\x00\x00\x00bcftools call -mv ->qIsuuX\x05\x00\x00\x00SETUPqJ\x88X\x0b\x00\x00\x00directoriesqK}qL(X\x07\x00\x00\x00TEMPDIRqMX\x04\x00\x00\x00tempqNX\t\x00\x00\x00REFERENCEqOX\t\x00\x00\x00referenceqPX\x06\x00\x00\x00PIPDIRqQ}qR(X\x06\x00\x00\x00mappedqSX\x15\x00\x00\x00analysis/mapped_readsqTX\x07\x00\x00\x00metricsqUX\x10\x00\x00\x00analysis/metricsqVX\x08\x00\x00\x00analysisqWX\x08\x00\x00\x00analysisqXuX\x06\x00\x00\x00OUTDIRqY}qZ(X\x06\x00\x00\x00fastqcq[X\x15\x00\x00\x00out/results_QC/fastQCq\\X\n\x00\x00\x00insertSizeq]X\x0e\x00\x00\x00out/results_QCq^X\x03\x00\x00\x00outq_X\x03\x00\x00\x00outq`uX\x05\x00\x00\x00dbSNPqaX\x06\x00\x00\x00dbSNPsqbX\x07\x00\x00\x00SCRIPTSqc}qd(X\x01\x00\x00\x00RqeX\t\x00\x00\x00scripts/RqfX\x07\x00\x00\x00scriptsqgX\x07\x00\x00\x00scriptsqhX\x06\x00\x00\x00PythonqiX\x0e\x00\x00\x00scripts/PythonqjX\x05\x00\x00\x00SnakeqkX\r\x00\x00\x00scripts/SnakeqluX\x06\x00\x00\x00SAMPLEqmX\x06\x00\x00\x00sampleqnX\x03\x00\x00\x00BINqoX\x03\x00\x00\x00binqpuX\x07\x00\x00\x00samplesqq}qr(X\x05\x00\x00\x00LANE1qs}qt(X\x07\x00\x00\x00FORWARDquX\x18\x00\x00\x00LF2017_63_S8_L001_R1_001qvX\x07\x00\x00\x00REVERSEqwX\x18\x00\x00\x00LF2017_63_S8_L001_R2_001qxuX\x05\x00\x00\x00LANE2qy}qz(huX\x18\x00\x00\x00LF2017_63_S8_L002_R1_001q{hwX\x18\x00\x00\x00LF2017_63_S8_L002_R2_001q|uuX\x0e\x00\x00\x00req_file_pathsq}}q~(haX(\x00\x00\x00dbSNPs/common_all_20180423_edit_2.vcf.gzq\x7fhOX\x19\x00\x00\x00reference/ucsc.hg19.fastaq\x80uuX\x06\x00\x00\x00paramsq\x81csnakemake.io\nParams\nq\x82)\x81q\x83}q\x84h\x07}q\x85sbX\x05\x00\x00\x00inputq\x86csnakemake.io\nInputFiles\nq\x87)\x81q\x88X1\x00\x00\x00analysis/metrics/LF2017_63_metrics.insertSize.tsvq\x89a}q\x8ah\x07}q\x8bsbX\x06\x00\x00\x00outputq\x8ccsnakemake.io\nOutputFiles\nq\x8d)\x81q\x8eX\x18\x00\x00\x00temp/info_insertSize.txtq\x8fa}q\x90h\x07}q\x91sbX\t\x00\x00\x00wildcardsq\x92csnakemake.io\nWildcards\nq\x93)\x81q\x94}q\x95h\x07}q\x96sbub.')
######## Original script #########


def Mean(d):             #mean function for dictionaries -- assumes dictionary values are counts
	total = 0
	for entry in d:
		total += entry * d[entry]
	return total / sum(d.values())	



insert_distribution = {}  # key -- insert size, value -- count
start_storing = False
out_filename = "{DIR_METRICS}/{SAMPLE_ID}_metrics.insertSize.tsv"

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