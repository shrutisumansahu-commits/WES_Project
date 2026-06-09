# Final Variant Discovery Summary

Dataset: SRR098401 (NA12878)

Pipeline Summary:

* FASTQ generation completed
* Read quality assessment performed using FastQC and MultiQC
* Adapter and quality trimming performed using fastp
* Reads aligned to GRCh38 using BWA-MEM
* BAM files processed using SAMtools
* Read groups added using GATK
* Duplicate reads marked
* Variants called using GATK HaplotypeCaller
* High-confidence variants obtained using bcftools filtering

Final Results:

* Raw variants identified: 75,717
* Filtered variants retained: 3,488
* SNPs: 3,315
* INDELs: 173

Conclusion:

A reproducible WES workflow was successfully implemented and applied to the NA12878 benchmark exome dataset, resulting in a high-confidence variant call set suitable for downstream interpretation.
