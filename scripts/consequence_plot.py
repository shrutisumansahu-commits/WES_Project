import matplotlib.pyplot as plt

labels = [
    "Missense",
    "Synonymous",
    "Intergenic",
    "Upstream",
    "Intron",
    "Downstream",
    "Frameshift",
    "StopGained"
]

counts = [
    1028,
    798,
    453,
    385,
    295,
    240,
    21,
    11
]

plt.figure(figsize=(10,5))
bars = plt.bar(labels, counts)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        str(int(height)),
        ha='center'
    )

plt.xticks(rotation=45)
plt.ylabel("Count")
plt.title("Functional Consequence Distribution")
plt.tight_layout()

plt.savefig("figures/functional_consequences.png", dpi=300)
