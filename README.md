
# In-silico Characterisation of SpCas9 Nuclease

**A Bioinformatics Approach to Protein Sequence, Domain and Structural Analysis**

## 1. Project Overview

This independent bioinformatics project investigates the sequence, physicochemical characteristics, functional domains and three-dimensional structure of Streptococcus pyogenes Cas9 (SpCas9).

SpCas9 is an RNA-guided DNA endonuclease used in the CRISPR-Cas9 genome-editing system. Its structure contains distinct regions involved in guide RNA interaction, target DNA recognition and nuclease activity.

The project combines Python-based protein sequence analysis, database-based domain annotation, sequence similarity analysis and structural visualisation.

This is an entirely computational project. No experimental protein expression, purification or enzyme activity assays were performed.

## 2. Project Objectives

1. Retrieve and validate the reference SpCas9 protein sequence.
2. Analyse amino acid composition and sequence-derived physicochemical properties.
3. Identify functional domains and compare annotations from different databases.
4. Investigate sequence similarity using BLASTp.
5. Perform pairwise protein sequence alignment.
6. Examine the three-dimensional SpCas9 protein–RNA–DNA complex.
7. Compare the experimentally determined structural sequence with the reference UniProt sequence.
8. Visualise the protein's domains and structural components.
9. Interpret and document the computational findings.

## 3. Dataset and Reference Information

| Parameter | Information |
|---|---|
| Protein | SpCas9 |
| Organism | Streptococcus pyogenes |
| UniProt accession | Q99ZW2 |
| Reference sequence length | 1,368 amino acids |
| Sequence format | FASTA |
| Structure | PDB 7S3H |
| Structural method | Cryo-electron microscopy |
| Structural resolution | 2.5 Å |

Reference resources:
- UniProt: https://www.uniprot.org/uniprotkb/Q99ZW2/entry
- RCSB PDB: https://www.rcsb.org/structure/7S3H

## 4. Tools and Technologies

| Tool | Application |
|---|---|
| Python | Bioinformatics scripting |
| Biopython | Sequence analysis, protein properties and alignment |
| Pandas | Data organisation and CSV processing |
| Matplotlib | Scientific visualisation |
| BLASTp | Protein sequence similarity searching |
| InterProScan | Protein domain and family annotation |
| NCBI CD-Search | Conserved domain identification |
| PyMOL | Three-dimensional protein structure visualisation |
| UniProt | Reference protein sequence and annotations |
| RCSB PDB | Three-dimensional structure retrieval |
| Ubuntu WSL | Computational environment |
| Conda | Python environment management |

## 5. Methodology and Results

### 5.1 Protein Sequence Retrieval and Validation

The SpCas9 reference protein sequence was retrieved from UniProt using accession Q99ZW2.

Input file: `data/spcas9_Q99ZW2.fasta`

Biopython's SeqIO module was used to validate and extract the protein sequence.

Result:
- Sequence length: 1,368 amino acids.
- FASTA validation completed successfully.

Script: `scripts/01_validate_fasta.py`

### 5.2 Amino Acid Composition Analysis

The frequency and percentage of all 20 standard amino acids were calculated using Python.

Percentage calculation:

Percentage = (Amino acid count / Total amino acid count) × 100

Key observations:
- Lysine (K): 150 residues (10.96%).
- Leucine (L): 148 residues (10.82%).
- Cysteine (C): 2 residues (0.15%).

The results were saved as a CSV file and visualised using Matplotlib.

Scripts:
- `scripts/02_amino_acid_composition.py`
- `scripts/03_amino_acid_plot.py`

Outputs:
- `results/amino_acid_composition.csv`
- `results/amino_acid_composition.png`

### 5.3 Physicochemical Property Analysis

Biopython's ProteinAnalysis module was used to calculate sequence-derived physicochemical properties.

| Property | Result |
|---|---:|
| Sequence length | 1,368 aa |
| Molecular weight | 158,439.38 Da |
| Theoretical pI | 8.98 |
| Instability index | 37.57 |
| Aliphatic index | 89.44 |
| GRAVY | -0.594 |

Interpretation:
- The predicted molecular weight is approximately 158.44 kDa.
- The theoretical isoelectric point is 8.98.
- The instability index is below the conventional threshold of 40.
- The negative GRAVY value indicates an overall hydrophilic tendency in the sequence.

These values are computational estimates, not experimental measurements of protein stability, solubility or activity.

Script: `scripts/04_protein_properties.py`

Output: `results/spcas9_physicochemical_properties.csv`

### 5.4 Protein Domain Identification and Architecture

InterProScan and NCBI CD-Search were used to investigate conserved protein domains and functional regions.

The annotations were compared to understand differences between broad architectural boundaries and database-specific profile matches.

Important annotations include:

| Region | Approximate residues |
|---|---|
| RuvC-I | 1–62 |
| Arginine-rich motif (ARM) | 56–73 |
| Recognition lobe (REC) | 56–718 |
| Bridge helix | 60–93 |
| RuvC-II | 718–765 |
| HNH | 770–921 |
| HNH functional region | 810–872 |
| RuvC-III | 925–1102 |
| PAM-interacting region | 1099–1368 |

Important annotation distinctions:
- The REC architectural boundary is broader than the InterProScan and NCBI REC profile matches.
- The ARM and bridge helix are distinct, partially overlapping annotations.
- The HNH functional region is not identical to the narrower Pfam profile match.
- RuvC is a discontinuous domain comprising three sequence segments.

The boundaries are approximate and depend on the annotation source and definition.

Scripts:
- `scripts/05_domain_architecture.py`
- `scripts/06_domain_comparison_plot.py`

Supporting files:
- `docs/spcas9_domain_annotations.csv`
- `docs/spcas9_domain_comparison.csv`
- `results/interpro/`

Visual outputs:
- `results/spcas9_domain_architecture_v3.png`
- `results/spcas9_domain_comparison_v2.png`

### 5.5 BLASTp Sequence Similarity Analysis

BLASTp was used to compare the reference SpCas9 sequence against protein database sequences.

The retrieved filtered results contained 51 hits.

Summary:
- Mean sequence identity: 99.874%.
- Mean query coverage: 99.971%.
- Five hits showed 100% sequence identity.
- Most retrieved sequences were highly similar to the reference.

The high similarity reflects the selected search results and should not be interpreted as 51 independent evolutionary homologues.

Scripts:
- `scripts/07_blastp_analysis.py`
- `scripts/08_blastp_visualization.py`

Outputs:
- `results/blastp/spcas9_blastp_hits_clean.csv`
- `results/blastp/spcas9_blastp_identity.png`
- `results/blastp/spcas9_blastp_coverage.png`
- `docs/blastp_analysis.md`

### 5.6 Pairwise Sequence Alignment

A global pairwise alignment was performed between:
- Reference: UniProt Q99ZW2.
- Comparison sequence: WP_011285506.1.

Biopython PairwiseAligner was used with the BLOSUM62 substitution matrix.

Alignment results:

| Parameter | Result |
|---|---:|
| Query length | 1,368 aa |
| Reference length | 1,368 aa |
| Identical residues | 1,367 |
| Mismatches | 1 |
| Gaps | 0 |
| Percentage identity | 99.927% |

One amino acid substitution was identified: E24D.

This is a conservative substitution between acidic amino acids. Its functional impact was not experimentally assessed.

Script: `scripts/09_pairwise_alignment.py`

Outputs:
- `results/spcas9_pairwise_alignment.txt`
- `results/spcas9_sequence_differences.csv`

### 5.7 Three-Dimensional Structure Analysis

The SpCas9 structure was obtained from the RCSB Protein Data Bank (PDB ID: 7S3H).

The cryo-EM structure represents a SpCas9 complex containing protein, guide RNA and target DNA.

The structure was examined using PyMOL.

Modelled chains:
- Chain P: SpCas9 protein (1,030 modelled residues).
- Chain R: RNA (30 residues).
- Chain N: DNA (23 residues).
- Chain T: DNA (23 residues).

The protein, RNA and DNA chains were visualised using different colours.

The protein was also visualised with different colours assigned to selected functional regions, including REC, HNH, RuvC, PAM-interacting and bridge helix regions.

Scripts:
- `scripts/10_verify_pdb_structure.py`
- `scripts/11_extract_pdb_sequence.py`
- `scripts/12_compare_pdb_sequence.py`

Supporting files:
- `data/structures/spcas9_7S3H.cif`
- `data/structures/spcas9_7S3H_chain_P.fasta`
- `docs/pymol_structural_visualization.md`

Visual outputs:
- `results/spcas9_7S3H_chains_v3.png`
- `results/spcas9_domain_visualization_v2.png`

Note: The domain-coloured PyMOL image retains the evaluation watermark from the installed PyMOL version.

### 5.8 PDB and UniProt Sequence Comparison

The modelled protein sequence from PDB chain P was extracted and aligned against the UniProt reference sequence.

Results:
- Reference sequence length: 1,368 amino acids.
- Modelled protein residues: 1,030.
- Missing from the structural coordinates: 338 residues.
- One substitution identified at reference position 1337 (T to C).

Several regions were absent from the structural model, including the large region 448–715.

Missing coordinate residues should not be interpreted as biologically deleted residues. They may be unresolved or absent from the experimentally determined structural model.

Output: `results/spcas9_pdb_uniprot_alignment.txt`

## 6. Project Directory Structure

```text
SpCas9_Protein_Characterisation/
│
├── data/
│   ├── spcas9_Q99ZW2.fasta
│   └── structures/
│       ├── spcas9_7S3H.cif
│       └── spcas9_7S3H_chain_P.fasta
│
├── scripts/
│   ├── 01_validate_fasta.py
│   ├── 02_amino_acid_composition.py
│   ├── 03_amino_acid_plot.py
│   ├── 04_protein_properties.py
│   ├── 05_domain_architecture.py
│   ├── 06_domain_comparison_plot.py
│   ├── 07_blastp_analysis.py
│   ├── 08_blastp_visualization.py
│   ├── 09_pairwise_alignment.py
│   ├── 10_verify_pdb_structure.py
│   ├── 11_extract_pdb_sequence.py
│   └── 12_compare_pdb_sequence.py
│
├── results/
│   ├── amino_acid_composition.csv
│   ├── amino_acid_composition.png
│   ├── spcas9_physicochemical_properties.csv
│   ├── spcas9_domain_architecture_v3.png
│   ├── spcas9_domain_comparison_v2.png
│   ├── spcas9_pairwise_alignment.txt
│   ├── spcas9_pdb_uniprot_alignment.txt
│   ├── spcas9_sequence_differences.csv
│   ├── spcas9_7S3H_chains_v3.png
│   ├── spcas9_domain_visualization_v2.png
│   └── blastp/
│
├── docs/
│   ├── blastp_analysis.md
│   ├── pymol_structural_visualization.md
│   ├── spcas9_domain_annotations.csv
│   └── spcas9_domain_comparison.csv
│
└── README.md
```

## 7. Overall Findings

The computational analyses provided the following observations:

1. The reference SpCas9 protein contains 1,368 amino acids.
2. Lysine and leucine are the most abundant amino acids in the sequence.
3. The predicted molecular weight is approximately 158.44 kDa.
4. Conserved domain resources identify the major functional regions of SpCas9, although their reported boundaries vary by annotation method.
5. BLASTp identified highly similar protein sequences in the selected database results.
6. Pairwise alignment identified one conservative substitution between the selected sequences.
7. Structural visualisation demonstrated the organisation of SpCas9 with its associated RNA and DNA.
8. Comparison of the PDB model with UniProt identified regions missing from the structural coordinates.

## 8. Limitations

- Physicochemical properties are sequence-based predictions.
- Domain boundaries depend on the database or structural definition used.
- BLASTp results depend on the database, search settings and filtering criteria.
- Missing residues in the PDB model do not necessarily represent biological deletions.
- Structural visualisation does not establish biochemical activity.
- No molecular dynamics simulations, protein expression, purification, enzyme activity assays or experimental validation were performed.

## 9. References and Databases

1. UniProt Consortium. UniProt entry Q99ZW2, SpCas9.
2. RCSB Protein Data Bank. PDB entry 7S3H.
3. Nishimasu H. et al. (2014). Crystal Structure of Cas9 in Complex with Guide RNA and Target DNA. Cell, 156(5), 935–949. https://doi.org/10.1016/j.cell.2014.02.001
4. NCBI BLASTp: https://blast.ncbi.nlm.nih.gov/
5. InterPro: https://www.ebi.ac.uk/interpro/
6. NCBI Conserved Domain Search: https://www.ncbi.nlm.nih.gov/Structure/cdd/wrpsb.cgi
7. Biopython documentation: https://biopython.org/

## 10. Conclusion

This project demonstrates an integrated computational workflow for the characterisation of SpCas9 using protein sequence analysis, physicochemical calculations, conserved domain annotation, sequence similarity searching, pairwise alignment and three-dimensional structural visualisation.

The work provides practical experience in Python-based bioinformatics, interpretation of protein sequence data, use of public biological databases and structural bioinformatics tools.

The project is intended as an independent computational bioinformatics portfolio demonstrating foundational skills relevant to protein science and bioinformatics research.
