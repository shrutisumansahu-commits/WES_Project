# Whole Exome Sequencing (WES) Variant Analysis Pipeline

## Project Overview

This project implements an end-to-end Whole Exome Sequencing (WES) analysis workflow using the benchmark NA12878 (GM12878) human exome dataset (SRR098401) from NCBI SRA.

The objective was to perform quality control, read alignment, BAM processing, germline variant discovery, and variant filtering following GATK Best Practices.

## Dataset

| Attribute | Value                  |
| --------- | ---------------------- |
| Sample    | NA12878 (GM12878)      |
| Accession | SRR098401              |
| Platform  | Illumina HiSeq 2000    |
| Strategy  | Whole Exome Sequencing |
| Layout    | Paired-End             |

## Workflow

Dataset Acquisition → FASTQ Generation → FastQC → MultiQC → fastp → BWA-MEM → BAM Processing → Read Group Addition → MarkDuplicates → HaplotypeCaller → Variant Filtering

## Tools Used

* FastQC
* MultiQC
* fastp
* BWA-MEM
* SAMtools
* GATK
* bcftools

## Results

| Result             |  Count |
| ------------------ | -----: |
| Raw Variants       | 75,717 |
| Filtered Variants  |  3,488 |
| SNPs               |  3,315 |
| INDELs             |    173 |
| Multiallelic Sites |     10 |

## Challenges and Troubleshooting

### Missing Read Groups

GATK MarkDuplicates initially failed because the BAM header lacked Read Group (RG) information.

Resolution:

* Verified absence of RG records in BAM header.
* Added read groups using GATK AddOrReplaceReadGroups.
* Re-ran duplicate marking successfully.

This troubleshooting step improved understanding of GATK Best Practices and BAM metadata requirements.

## Status

Completed through variant discovery and filtering.

