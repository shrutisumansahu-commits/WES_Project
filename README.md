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

- [x] Dataset acquisition
- [x] SRA to FASTQ conversion
- [x] Read downsampling
- [x] Quality assessment (FastQC)
- [x] MultiQC report generation
- [x] Read trimming (fastp)
- [x] Reference genome preparation (GRCh38)

### Upcoming Steps

- [ ] BWA-MEM alignment
- [ ] BAM processing
- [ ] Duplicate marking
- [ ] Variant calling (GATK HaplotypeCaller)
- [ ] Variant filtering
- [ ] Variant annotation
- [ ] Variant interpretation

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
