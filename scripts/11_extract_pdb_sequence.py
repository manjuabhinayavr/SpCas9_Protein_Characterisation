from Bio.PDB import MMCIFParser
from Bio.SeqUtils import seq1
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# Load the experimental structure
parser = MMCIFParser(QUIET=True)
structure = parser.get_structure(
    "SpCas9",
    "data/structures/spcas9_7S3H.cif"
)

# Select protein chain P
chain = structure[0]["P"]

# Extract standard amino acid residues
protein_sequence = ""

for residue in chain:

    if residue.id[0] == " ":
        amino_acid = seq1(residue.resname, custom_map={"UNK": "X"})
        protein_sequence += amino_acid

# Save the extracted sequence
record = SeqRecord(
    Seq(protein_sequence),
    id="7S3H_chain_P",
    description="SpCas9 experimental structure sequence"
)

SeqIO.write(
    record,
    "data/structures/spcas9_7S3H_chain_P.fasta",
    "fasta"
)

# Display information
print("\nPDB PROTEIN SEQUENCE EXTRACTION")
print("--------------------------------")
print("Chain:", chain.id)
print("Extracted sequence length:", len(protein_sequence))
print("First 30 amino acids:", protein_sequence[:30])
print("Last 30 amino acids:", protein_sequence[-30:])

residues = [
    residue for residue in chain
    if residue.id[0] == " "
]

print("First residue identifier:", residues[0].id)
print("Last residue identifier:", residues[-1].id)

print("\nFASTA sequence saved successfully.")
