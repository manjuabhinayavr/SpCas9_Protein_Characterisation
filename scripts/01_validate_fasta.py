from Bio import SeqIO

# Read the FASTA file
record = SeqIO.read("data/spcas9_Q99ZW2.fasta", "fasta")

# Display basic information
print("Protein ID:", record.id)
print("Protein description:", record.description)
print("Sequence length:", len(record.seq))
print("First 20 amino acids:", record.seq[:20])
