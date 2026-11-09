import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Read domain comparison data
df = pd.read_csv("docs/spcas9_domain_comparison.csv")

# Keep only rows with valid coordinates for plotting
valid = df.dropna(subset=["Start", "End"]).copy()

# Create separate labels for individual matches
valid["Label"] = valid.apply(
    lambda row: f'{row["Feature"]} ({row["Accession"]})',
    axis=1
)

# Set consistent colours by database
colors = {
    "InterProScan": "steelblue",
    "NCBI CD-Search": "darkorange"
}

fig, ax = plt.subplots(figsize=(13, 7))

# Plot each detected database match
for i, row in valid.reset_index(drop=True).iterrows():
    ax.plot(
        [row["Start"], row["End"]],
        [i, i],
        color=colors[row["Database"]],
        linewidth=7 if row["Database"] == "InterProScan" else 4,
        linestyle="-" if row["Database"] == "InterProScan" else "--",
        solid_capstyle="butt"
    )

# Add labels for features without specific NCBI hits
labels = valid["Label"].tolist()

for _, row in df.iterrows():
    if pd.isna(row["Start"]) or pd.isna(row["End"]):
        labels.append(f'{row["Feature"]} — {row["Database"]}: not detected')

# Y-axis labels
ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels)

# Axis formatting
ax.set_xlim(1, 1368)
ax.set_xlabel("Amino Acid Position")
ax.set_ylabel("Database matches")
ax.set_title("SpCas9 Domain Annotation: InterProScan vs NCBI CD-Search")

ax.grid(axis="x", linestyle=":", alpha=0.5)

# Database legend
legend_elements = [
    Line2D([0], [0], color="steelblue", linewidth=7,
           label="InterProScan"),
    Line2D([0], [0], color="darkorange", linewidth=4,
           linestyle="--", label="NCBI CD-Search")
]

ax.legend(handles=legend_elements, loc="lower right")

plt.tight_layout()

plt.savefig(
    "results/spcas9_domain_comparison_v2.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Updated domain comparison plot saved successfully!")
