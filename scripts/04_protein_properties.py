
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# Step 1: Read the SpCas9 protein FASTA file
record = SeqIO.read("data/spcas9_Q99ZW2.fasta", "fasta")
sequence = str(record.seq)

# Step 2: Analyse the protein sequence
analysis = ProteinAnalysis(sequence)

# Step 3: Calculate physicochemical properties
molecular_weight = analysis.molecular_weight()
isoelectric_point = analysis.isoelectric_point()
instability_index = analysis.instability_index()
gravy = analysis.gravy()

# Step 4: Count amino acids
amino_acids = analysis.count_amino_acids()
total = len(sequence)

# Step 5: Calculate amino acid percentages
A = (amino_acids["A"] / total) * 100
V = (amino_acids["V"] / total) * 100
I = (amino_acids["I"] / total) * 100
L = (amino_acids["L"] / total) * 100

# Step 6: Calculate aliphatic index manually
aliphatic_index = A + (2.9 * V) + (3.9 * (I + L))

# Step 7: Display results
print("\nSPCAS9 PROTEIN CHARACTERISATION")
print("-----------------------------------")

print("Protein ID:", record.id)
print("Sequence length:", total, "amino acids")
print("Molecular weight:", round(molecular_weight, 2), "Da")
print("Theoretical pI:", round(isoelectric_point, 2))
print("Instability index:", round(instability_index, 2))
print("Aliphatic index:", round(aliphatic_index, 2))
print("GRAVY:", round(gravy, 3))

print("\nAnalysis completed successfully!")

import pandas as pd

# Store protein properties in a table
properties = {
    "Property": [
        "Sequence length",
        "Molecular weight (Da)",
        "Theoretical pI",
        "Instability index",
        "Aliphatic index",
        "GRAVY"
    ],
    "Value": [
        total,
        round(molecular_weight, 2),
        round(isoelectric_point, 2),
        round(instability_index, 2),
        round(aliphatic_index, 2),
        round(gravy, 3)
    ]
}

df = pd.DataFrame(properties)

# Save results
df.to_csv("results/spcas9_physicochemical_properties.csv", index=False)

print("Physicochemical results saved successfully!")
