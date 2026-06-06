# Whole Exome Sequencing (WES) Variant Analysis Pipeline

## Overview

This project aims to develop a reproducible Whole Exome Sequencing (WES) analysis workflow using the benchmark human exome dataset NA12878 (GM12878) from NCBI SRA.

## Dataset

- Sample: GM12878 (NA12878)
- Accession: SRR098401
- Platform: Illumina HiSeq 2000
- Strategy: Whole Exome Sequencing (WXS)
- Layout: Paired-End

## Workflow

## Progress

- [x] Dataset acquisition
- [x] SRA to FASTQ conversion
- [x] Read downsampling
- [x] FastQC
- [x] MultiQC
- [x] Read trimming (fastp)
- [x] GRCh38 reference preparation
- [x] Read alignment
- [ ] BAM processing
- [ ] Duplicate marking
- [ ] Variant calling
- [ ] Variant annotation

## Tools Used

- FastQC
- MultiQC
- fastp
- BWA
- SAMtools
- GATK
- Picard
- VEP

## Status

Project in Progress
