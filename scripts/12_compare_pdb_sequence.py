from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

# Step 1: Load both sequences
reference = SeqIO.read(
    "data/spcas9_Q99ZW2.fasta", "fasta"
)

pdb_sequence = SeqIO.read(
    "data/structures/spcas9_7S3H_chain_P.fasta", "fasta"
)

# Step 2: Configure global alignment
aligner = PairwiseAligner()
aligner.mode = "global"
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5

# Step 3: Align reference against the PDB sequence
alignment = aligner.align(
    reference.seq, pdb_sequence.seq
)[0]

aligned_reference = str(alignment[0])
aligned_pdb = str(alignment[1])

# Step 4: Identify missing residues and substitutions
missing_positions = []
substitutions = []

reference_position = 0

for ref_aa, pdb_aa in zip(aligned_reference, aligned_pdb):

    if ref_aa != "-":
        reference_position += 1

    if ref_aa != "-" and pdb_aa == "-":
        missing_positions.append(reference_position)

    elif ref_aa != "-" and pdb_aa != "-" and ref_aa != pdb_aa:
        substitutions.append(
            (reference_position, ref_aa, pdb_aa)
        )

# Step 5: Group consecutive missing positions
missing_regions = []

if missing_positions:
    start = missing_positions[0]
    end = start

    for position in missing_positions[1:]:
        if position == end + 1:
            end = position
        else:
            missing_regions.append((start, end))
            start = position
            end = position

    missing_regions.append((start, end))

# Step 6: Display results
print("\nPDB AND UNIPROT SEQUENCE COMPARISON")
print("------------------------------------")

print("Reference length:", len(reference.seq))
print("PDB sequence length:", len(pdb_sequence.seq))
print("Alignment length:", len(aligned_reference))
print("Missing reference residues:", len(missing_positions))
print("Number of missing regions:", len(missing_regions))

print("\nMISSING REGIONS")

for start, end in missing_regions:
    print(f"{start}-{end} ({end - start + 1} residues)")

print("\nSEQUENCE SUBSTITUTIONS")

if substitutions:
    for position, ref_aa, pdb_aa in substitutions:
        print(f"Position {position}: {ref_aa} -> {pdb_aa}")
else:
    print("No substitutions detected.")

# Step 7: Save alignment
with open(
    "results/spcas9_pdb_uniprot_alignment.txt", "w"
) as file:
    file.write(str(alignment))

print("\nAlignment saved successfully.")
