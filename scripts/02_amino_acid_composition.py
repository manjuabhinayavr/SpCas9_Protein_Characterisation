from Bio import SeqIO
from collections import Counter
import pandas as pd

# Read the protein sequence
record = SeqIO.read("data/spcas9_Q99ZW2.fasta", "fasta")

sequence = str(record.seq)

# Count each amino acid
amino_acid_count = Counter(sequence)

# Calculate total amino acids
total = len(sequence)

# Create a table
results = []

for amino_acid, count in amino_acid_count.items():

    percentage = (count / total) * 100

    results.append({
        "Amino_Acid": amino_acid,
        "Count": count,
        "Percentage": round(percentage, 2)
    })

# Convert results into a DataFrame
df = pd.DataFrame(results)

# Sort by amino acid count
df = df.sort_values(by="Count", ascending=False)

# Display results
print(df.to_string(index=False))

# Save results
df.to_csv("results/amino_acid_composition.csv", index=False)

print("\nTotal amino acids:", total)
print("Results saved successfully!")
