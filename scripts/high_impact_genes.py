genes = set()

with open("annotation/annotated_variants.vcf") as f:
    for line in f:
        if line.startswith("#"):
            continue

        if "frameshift_variant" in line or "stop_gained" in line:

            ann = line.split("ANN=")[1]
            fields = ann.split("|")

            if len(fields) > 3:
                genes.add(fields[3])

for gene in sorted(genes):
    print(gene)
