import pandas as pd

# Step 1: Define input file
input_file = "results/blastp/EY6JYVHC014-Alignment-HitTable.csv"

# Step 2: Define column names
columns = [
    "Query_ID",
    "Subject_ID",
    "Percentage_Identity",
    "Alignment_Length",
    "Mismatches",
    "Gap_Openings",
    "Query_Start",
    "Query_End",
    "Subject_Start",
    "Subject_End",
    "E_Value",
    "Bit_Score",
    "Query_Coverage"
]

# Step 3: Read the BLASTp CSV
df = pd.read_csv(input_file, header=None, names=columns)

# Step 4: Display basic information
print("\nSPCAS9 BLASTP ANALYSIS")
print("-----------------------------")

print("Total BLAST hits:", len(df))
print("Number of columns:", len(df.columns))

# Step 5: Calculate identity statistics
print("\nPERCENTAGE IDENTITY")
print("Minimum:", df["Percentage_Identity"].min())
print("Maximum:", df["Percentage_Identity"].max())
print("Average:", round(df["Percentage_Identity"].mean(), 3))

# Step 6: Calculate query coverage
print("\nQUERY COVERAGE")
print("Minimum:", df["Query_Coverage"].min())
print("Maximum:", df["Query_Coverage"].max())
print("Average:", round(df["Query_Coverage"].mean(), 3))

# Step 7: Display top 10 hits
top_hits = df.sort_values(
    by="Bit_Score",
    ascending=False
).head(10)

print("\nTOP 10 BLASTP HITS")
print(top_hits[
    ["Subject_ID", "Percentage_Identity",
     "Query_Coverage", "E_Value", "Bit_Score"]
].to_string(index=False))

# Step 8: Save clean results
output_file = "results/blastp/spcas9_blastp_hits_clean.csv"
df.to_csv(output_file, index=False)

print("\nClean BLASTp results saved:", output_file)
