import pysam

vcf = pysam.VariantFile("variants/filtered_variants.vcf.gz")

transitions = 0
transversions = 0

ti = {("A","G"),("G","A"),("C","T"),("T","C")}

for rec in vcf:
    if len(rec.ref) == 1 and len(rec.alts[0]) == 1:
        if (rec.ref, rec.alts[0]) in ti:
            transitions += 1
        else:
            transversions += 1

ratio = transitions/transversions if transversions else 0

print(f"Transitions: {transitions}")
print(f"Transversions: {transversions}")
print(f"Ti/Tv Ratio: {ratio:.2f}")
