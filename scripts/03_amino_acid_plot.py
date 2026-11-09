import pandas as pd
import matplotlib.pyplot as plt

# Read amino acid results
df = pd.read_csv("results/amino_acid_composition.csv")

# Create figure
plt.figure(figsize=(14, 7))

# Draw bars
bars = plt.bar(
    df["Amino_Acid"],
    df["Percentage"],
    width=0.7
)

# Add percentage values above each bar
for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.15,
        f"{height:.2f}%",
        ha="center",
        fontsize=8
    )

# Graph title and labels
plt.title(
    "Amino Acid Composition of SpCas9 Protein",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Amino Acid", fontsize=12)
plt.ylabel("Composition (%)", fontsize=12)

# Improve appearance
plt.ylim(0, 13)
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.xticks(fontsize=11)
plt.yticks(fontsize=10)

plt.tight_layout()

# Save graph
plt.savefig(
    "results/amino_acid_composition.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Improved graph saved successfully!")
