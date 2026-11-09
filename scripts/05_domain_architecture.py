
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Read domain annotations
df = pd.read_csv("docs/spcas9_domain_annotations.csv")

# Define consistent domain colours
colors = {
    "REC": "steelblue",
    "HNH": "red",
    "RuvC": "forestgreen",
    "PI": "cyan",
    "ARM": "mediumpurple",
    "Bridge": "gold",
    "HNH_function": "indianred"
}

fig, ax = plt.subplots(figsize=(15, 7))

# Draw background protein sequence for each track
tracks = {
    "Main domain architecture": 2,
    "Discontinuous RuvC segments": 1,
    "Additional functional regions": 0
}

for y in tracks.values():
    ax.barh(
        y, 1368, left=0, height=0.35,
        color="lightgrey", zorder=1
    )

# Track 1: Main domain architecture
main_domains = [
    ("Recognition lobe (REC)", 56, 718, colors["REC"]),
    ("HNH", 770, 921, colors["HNH"]),
    ("PAM-interacting (PI)", 1099, 1368, colors["PI"])
]

for name, start, end, color in main_domains:
    ax.barh(
        2, end - start + 1, left=start - 1,
        height=0.45, color=color, zorder=2
    )
    ax.text(
        (start + end) / 2, 2,
        name, ha="center", va="center",
        fontsize=9, color="black"
    )

# Track 2: Discontinuous RuvC segments
ruvc_segments = [
    ("RuvC-I (1-62)", 1, 62),
    ("RuvC-II (718-765)", 718, 765),
    ("RuvC-III (925-1102)", 925, 1102)
]

for name, start, end in ruvc_segments:
    ax.barh(
        1, end - start + 1, left=start - 1,
        height=0.45, color=colors["RuvC"], zorder=2
    )
    ax.annotate(
        name,
        xy=((start + end) / 2, 1),
        xytext=((start + end) / 2, 1.30),
        ha="center", va="bottom", fontsize=8,
        arrowprops=dict(arrowstyle="-", lw=0.7)
    )

# Track 3: Additional functional regions
# ARM and bridge helix are separate annotations
functional_regions = [
    ("Arginine-rich motif (ARM)", 56, 73, colors["ARM"], 0.10),
    ("Bridge helix", 60, 93, colors["Bridge"], -0.10),
    ("HNH functional region", 810, 872, colors["HNH_function"], 0.0)
]

for name, start, end, color, y in functional_regions:
    ax.barh(
        y, end - start + 1, left=start - 1,
        height=0.12, color=color, zorder=3
    )

    if name == "Bridge helix":
        label_position = (145, y)
        alignment = "left"
        vertical_alignment = "center"
    else:
        label_position = ((start + end) / 2, y + 0.30)
        alignment = "center"
        vertical_alignment = "bottom"

    ax.annotate(
        name,
        xy=((start + end) / 2, y),
        xytext=label_position,
        ha=alignment,
        va=vertical_alignment,
        fontsize=9,
        arrowprops=dict(arrowstyle="-", lw=0.7)
    )
# Axis and labels
ax.set_xlim(0, 1368)
ax.set_ylim(-0.6, 2.8)
ax.set_yticks(list(tracks.values()))
ax.set_yticklabels(list(tracks.keys()))
ax.set_xlabel("SpCas9 amino acid position")
ax.set_title(
    "SpCas9 Domain Architecture and Functional Regions "
    "(UniProt Q99ZW2; 1,368 aa)",
    pad=18
)

ax.set_xticks(range(0, 1369, 100))
ax.grid(axis="x", linestyle="--", alpha=0.4)
ax.set_axisbelow(True)

# Legend
legend_items = [
    Patch(facecolor=colors["REC"], label="REC lobe"),
    Patch(facecolor=colors["HNH"], label="HNH domain"),
    Patch(facecolor=colors["RuvC"], label="RuvC segments"),
    Patch(facecolor=colors["PI"], label="PAM-interacting domain"),
    Patch(facecolor=colors["ARM"], label="Arginine-rich motif (ARM)"),
    Patch(facecolor=colors["Bridge"], label="Bridge helix"),
    Patch(facecolor=colors["HNH_function"], label="HNH functional region")
]

ax.legend(
    handles=legend_items,
    loc="lower center",
    bbox_to_anchor=(0.5, -0.25),
    ncol=3,
    frameon=False
)

plt.tight_layout()

# Save as a new version; preserve previous versions
plt.savefig(
    "results/spcas9_domain_architecture_v3.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("SpCas9 domain architecture v3 saved successfully!")
