# Project Log

## Step 1: Dataset Selection

Dataset: SRR098401

Sample: GM12878 (NA12878)

Platform: Illumina HiSeq 2000

Strategy: Whole Exome Sequencing (WXS)

Source: NCBI SRA

Status: Completed

---

## Step 2: FASTQ Generation

Tool: fasterq-dump

Input:
- SRR098401.sra

Output:
- SRR098401_1.fastq
- SRR098401_2.fastq

Status: Completed

---

## Step 3: Downsampling

Tool: seqtk

Fraction retained: 4.4%

Output:
- subset_R1.fastq
- subset_R2.fastq

Status: Completed
