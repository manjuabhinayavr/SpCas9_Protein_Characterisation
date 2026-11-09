from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

# Step 1: Load both protein sequences
query = SeqIO.read("data/spcas9_Q99ZW2.fasta", "fasta")
reference = SeqIO.read(
    "data/spcas9_refseq_WP0112855061.fasta", "fasta"
)

# Step 2: Configure the alignment tool
aligner = PairwiseAligner()
aligner.mode = "global"
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5

# Step 3: Perform alignment
alignment = aligner.align(query.seq, reference.seq)[0]

# Step 4: Extract aligned sequences
aligned_query = str(alignment[0])
aligned_reference = str(alignment[1])

# Step 5: Calculate alignment statistics
identical = 0
mismatches = 0
gaps = 0
query_position = 0
differences = []

for q, r in zip(aligned_query, aligned_reference):

    if q != "-":
        query_position += 1

    if q == "-" or r == "-":
        gaps += 1

    elif q == r:
        identical += 1

    else:
        mismatches += 1
        differences.append((query_position, q, r))

percentage_identity = (
    identical / len(aligned_query)
) * 100

# Step 6: Display results
print("\nSPCAS9 PAIRWISE ALIGNMENT")
print("-----------------------------")
print("Query:", query.id)
print("Reference:", reference.id)
print("Query length:", len(query.seq))
print("Reference length:", len(reference.seq))
print("Alignment length:", len(aligned_query))
print("Identical residues:", identical)
print("Mismatches:", mismatches)
print("Gaps:", gaps)
print("Percentage identity:", round(percentage_identity, 3), "%")

print("\nAMINO ACID DIFFERENCES")

if differences:
    for position, q, r in differences:
        print(f"Position {position}: {q} -> {r}")
else:
    print("No amino acid differences detected.")

# Step 7: Save alignment
with open("results/spcas9_pairwise_alignment.txt", "w") as file:
    file.write(str(alignment))

print("\nAlignment saved successfully.")
