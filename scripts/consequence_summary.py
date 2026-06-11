from collections import Counter

counts = Counter()

with open("annotation/annotated_variants.vcf") as f:
    for line in f:
        if line.startswith("#"):
            continue

        if "ANN=" in line:
            ann = line.split("ANN=")[1].split("|")[1]
            counts[ann] += 1

for k,v in counts.most_common(20):
    print(f"{k}\t{v}")
