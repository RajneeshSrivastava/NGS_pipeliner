import os
import sys

f1 = []

file1 = open("ID.txt");
for l1 in file1:
	l1 = l1.strip().split('	');
	f1.append(l1);
for i in f1:
	with open(str(i[0])+".sh","w") as f:
		print>>f,"""
#!/bin/bash
#PBS -l nodes=1:ppn=16 
#PBS -l walltime=12:00:00 
#PBS -l gres=ccm
#PBS -N %s
#PBS -q gpu

module load ccm
module load hisat/0.1.6
module load samtools/1.2

ccmrun hisat -p 32 -q -x /N/dc2/projects/MAMMALEXP/RBP-Target-Evolution_and_Transcriptome_Dynamics/REFERENCE/Human/h38.84/h38.84 -U /N/dc2/projects/MAMMALEXP/Rajneesh/POPSEQ_2019_08_05/Trim_FQ/%s.fastq -S /N/dc2/projects/MAMMALEXP/Rajneesh/POPSEQ_2019_08_05/Align/%s.sam
ccmrun samtools view -bS /N/dc2/projects/MAMMALEXP/Rajneesh/POPSEQ_2019_08_05/Align/%s.sam > /N/dc2/projects/MAMMALEXP/Rajneesh/POPSEQ_2019_08_05/Align/%s.bam
ccmrun samtools sort /N/dc2/projects/MAMMALEXP/Rajneesh/POPSEQ_2019_08_05/Align/%s.bam /N/dc2/projects/MAMMALEXP/Rajneesh/POPSEQ_2019_08_05/Align/%s.sorted
ccmrun samtools index /N/dc2/projects/MAMMALEXP/Rajneesh/POPSEQ_2019_08_05/Align/%s.sorted.bam

""" %(str(i[0]), str(i[0]), str(i[0]),str(i[0]), str(i[0]), str(i[0]), str(i[0]),str(i[0]))
#for f in $(find -name '*.sh'); do qsub $f; done
