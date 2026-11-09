import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned BLASTp results
df = pd.read_csv("results/blastp/spcas9_blastp_hits_clean.csv")

# Plot 1: Percentage identity distribution
plt.figure(figsize=(8, 5))

plt.hist(df["Percentage_Identity"], bins=10, edgecolor="black")

plt.xlabel("Percentage Identity (%)")
plt.ylabel("Number of Protein Hits")
plt.title("SpCas9 BLASTp - Percentage Identity Distribution")

plt.tight_layout()
plt.savefig("results/blastp/spcas9_blastp_identity.png", dpi=300)
plt.show()

# Plot 2: Query coverage distribution
plt.figure(figsize=(8, 5))

plt.hist(df["Query_Coverage"], bins=10, edgecolor="black")

plt.xlabel("Query Coverage (%)")
plt.ylabel("Number of Protein Hits")
plt.title("SpCas9 BLASTp - Query Coverage Distribution")

plt.tight_layout()
plt.savefig("results/blastp/spcas9_blastp_coverage.png", dpi=300)
plt.show()

print("Both BLASTp plots saved successfully!")
