

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
## Reference Genome Preparation

Reference Genome: GRCh38 (Ensembl Release 110)

Tools:
- BWA
- SAMtools
- GATK

Completed:
- Downloaded GRCh38 primary assembly
- Generated BWA index files
- Created FASTA index (.fai)
- Created sequence dictionary (.dict)

Purpose:
Prepare the reference genome for read alignment and downstream variant calling.
## Read Alignment

Tool: BWA-MEM

Input:
- trimmed_R1.fastq
- trimmed_R2.fastq
- GRCh38 reference genome

Output:
- sample.sam

Purpose:
Mapped exome sequencing reads to the human reference genome to identify their genomic coordinates for downstream variant analysis.
## BAM Processing

Tool: SAMtools

Completed:
- Converted SAM to BAM
- Sorted BAM by genomic coordinates
- Indexed BAM

Outputs:
- sample.bam
- sample_sorted.bam
- sample_sorted.bam.bai

Purpose:
Generate compressed and indexed alignment files required for duplicate marking and variant calling.
### Troubleshooting Note

Duplicate marking initially failed because the BAM header lacked Read Group (RG) information. Read groups were added using GATK AddOrReplaceReadGroups before rerunning duplicate marking.

Reason:
GATK tools require RG metadata to distinguish sequencing libraries and samples and to maintain compatibility with GATK Best Practices.

## Variant Calling Results

Tool:
- GATK HaplotypeCaller

Output:
- raw_variants.vcf.gz

Results:
- Total variants identified: 75,717

Notes:
- Variants include both SNPs and INDELs.
- Calls generated from a downsampled subset of the NA12878 benchmark exome dataset.
