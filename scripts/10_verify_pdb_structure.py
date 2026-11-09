from Bio.PDB import MMCIFParser

# Step 1: Read the mmCIF structure
parser = MMCIFParser(QUIET=True)

structure = parser.get_structure(
    "SpCas9",
    "data/structures/spcas9_7S3H.cif"
)

# Step 2: Select the first model
model = structure[0]

# Step 3: Display structure information
print("\nSPCAS9 PDB STRUCTURE VERIFICATION")
print("-----------------------------------")

print("PDB ID: 7S3H")
print("Number of models:", len(structure))

# Step 4: Identify chains
print("\nCHAIN INFORMATION")
print("-----------------")

for chain in model:

    residues = list(chain.get_residues())

    print(
        "Chain:", chain.id,
        "| Residues:", len(residues)
    )

print("\nStructure successfully loaded.")
