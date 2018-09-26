
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/sabus/miniconda3/envs/F1-pipe/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05X\x18\x00\x00\x00temp/info_insertSize.txtq\x06a}q\x07X\x06\x00\x00\x00_namesq\x08}q\tsbX\x06\x00\x00\x00paramsq\ncsnakemake.io\nParams\nq\x0b)\x81q\x0c}q\rh\x08}q\x0esbX\x07\x00\x00\x00threadsq\x0fK\x01X\x05\x00\x00\x00inputq\x10csnakemake.io\nInputFiles\nq\x11)\x81q\x12X1\x00\x00\x00analysis/metrics/LF2017_63_metrics.insertSize.tsvq\x13a}q\x14h\x08}q\x15sbX\t\x00\x00\x00wildcardsq\x16csnakemake.io\nWildcards\nq\x17)\x81q\x18}q\x19h\x08}q\x1asbX\x06\x00\x00\x00configq\x1b}q\x1c(X\x0b\x00\x00\x00directoriesq\x1d}q\x1e(X\t\x00\x00\x00REFERENCEq\x1fX\t\x00\x00\x00referenceq X\x07\x00\x00\x00SCRIPTSq!}q"(X\x05\x00\x00\x00Snakeq#X\r\x00\x00\x00scripts/Snakeq$X\x01\x00\x00\x00Rq%X\t\x00\x00\x00scripts/Rq&X\x07\x00\x00\x00scriptsq\'X\x07\x00\x00\x00scriptsq(X\x06\x00\x00\x00Pythonq)X\x0e\x00\x00\x00scripts/Pythonq*uX\x05\x00\x00\x00dbSNPq+X\x06\x00\x00\x00dbSNPsq,X\x06\x00\x00\x00PIPDIRq-}q.(X\x08\x00\x00\x00analysisq/X\x08\x00\x00\x00analysisq0X\x07\x00\x00\x00metricsq1X\x10\x00\x00\x00analysis/metricsq2X\x06\x00\x00\x00mappedq3X\x15\x00\x00\x00analysis/mapped_readsq4uX\x07\x00\x00\x00TEMPDIRq5X\x04\x00\x00\x00tempq6X\x03\x00\x00\x00BINq7X\x03\x00\x00\x00binq8X\x06\x00\x00\x00OUTDIRq9}q:(X\n\x00\x00\x00insertSizeq;X\x0e\x00\x00\x00out/results_QCq<X\x06\x00\x00\x00fastqcq=X\x15\x00\x00\x00out/results_QC/fastQCq>X\x03\x00\x00\x00outq?X\x03\x00\x00\x00outq@uX\x06\x00\x00\x00SAMPLEqAX\x06\x00\x00\x00sampleqBuX\x0e\x00\x00\x00req_file_pathsqC}qD(h\x1fX\x19\x00\x00\x00reference/ucsc.hg19.fastaqEh+X(\x00\x00\x00dbSNPs/common_all_20180423_edit_2.vcf.gzqFuX\x05\x00\x00\x00SETUPqG\x88X\x07\x00\x00\x00samplesqH}qI(X\x05\x00\x00\x00LANE1qJ}qK(X\x07\x00\x00\x00REVERSEqLX\x18\x00\x00\x00LF2017_63_S8_L001_R2_001qMX\x07\x00\x00\x00FORWARDqNX\x18\x00\x00\x00LF2017_63_S8_L001_R1_001qOuX\x05\x00\x00\x00LANE2qP}qQ(hLX\x18\x00\x00\x00LF2017_63_S8_L002_R2_001qRhNX\x18\x00\x00\x00LF2017_63_S8_L002_R1_001qSuuX\x05\x00\x00\x00toolsqT}qU(X\x04\x00\x00\x00GATKqV}qW(X\x0f\x00\x00\x00RealignerTargetqX}qYX\x04\x00\x00\x00callqZXC\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T RealignerTargetCreatorq[sX\x0e\x00\x00\x00IndelRealignerq\\}q]hZX;\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T IndelRealignerq^sX\n\x00\x00\x00PrintReadsq_}q`hZX7\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T PrintReadsqasX\x10\x00\x00\x00BaseRecalibratorqb}qchZX=\x00\x00\x00java -Xmx8G -jar bin/GenomeAnalysisTK.jar -T BaseRecalibratorqdsuX\x06\x00\x00\x00FASTQCqe}qfhZX.\x00\x00\x00~/Application/FastQC.app/Contents/MacOS/fastqcqgsX\x06\x00\x00\x00PICARDqh}qi(X\x12\x00\x00\x00FixMateInformationqj}qkhZX2\x00\x00\x00java -Xmx2G -jar bin/picard.jar FixMateInformationqlsX\r\x00\x00\x00MergeSamFilesqm}qnhZXE\x00\x00\x00java -XX:ParallelGCThreads=2 -Xmx2G -jar bin/picard.jar MergeSamFilesqosX\x1e\x00\x00\x00CollectAlignmentSummaryMetricsqp}qqhZX>\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectAlignmentSummaryMetricsqrsX\x18\x00\x00\x00CollectInsertSizeMetricsqs}qthZX8\x00\x00\x00java -Xmx2G -jar bin/picard.jar CollectInsertSizeMetricsqusX\x07\x00\x00\x00SortSamqv}qwhZX\'\x00\x00\x00java -Xmx2G -jar bin/picard.jar SortSamqxsX\x0e\x00\x00\x00MarkDuplicatesqy}qzhZX.\x00\x00\x00java -Xmx2G -jar bin/picard.jar MarkDuplicatesq{suX\x08\x00\x00\x00samtoolsq|}q}(X\x08\x00\x00\x00bcftoolsq~}q\x7fhZX\x14\x00\x00\x00bcftools call -mv ->q\x80sX\x06\x00\x00\x00pileupq\x81}q\x82hZX\x16\x00\x00\x00samtools mpileup -g -fq\x83suX\x07\x00\x00\x00bwa_memq\x84}q\x85hZX\x07\x00\x00\x00bwa memq\x86suuX\x04\x00\x00\x00ruleq\x87X\x06\x00\x00\x00reportq\x88X\t\x00\x00\x00resourcesq\x89csnakemake.io\nResources\nq\x8a)\x81q\x8b(K\x01K\x01e}q\x8c(X\x06\x00\x00\x00_nodesq\x8dK\x01h\x08}q\x8e(h\x8dK\x00N\x86q\x8fX\x06\x00\x00\x00_coresq\x90K\x01N\x86q\x91uh\x90K\x01ubX\x03\x00\x00\x00logq\x92csnakemake.io\nLog\nq\x93)\x81q\x94}q\x95h\x08}q\x96sbub.')
######## Original script #########


def Mean(d):             #mean function for dictionaries -- assumes dictionary values are counts
	total = 0
	for entry in d:
		total += entry * d[entry]
	return total / sum(d.values())	



insert_distribution = {}  # key -- insert size, value -- count
start_storing = False
out_filename = "{DIR_METRICS}/{SAMPLE_ID}_metrics.insertSize.tsv"

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