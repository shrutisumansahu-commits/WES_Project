import matplotlib.pyplot as plt

labels = ["SNPs", "INDELs"]
counts = [3315, 173]

plt.figure(figsize=(6,4))
plt.bar(labels, counts)
plt.ylabel("Variant Count")
plt.title("Variant Class Distribution")
plt.tight_layout()

plt.savefig("figures/variant_class_distribution.png", dpi=300)
plt.show()
