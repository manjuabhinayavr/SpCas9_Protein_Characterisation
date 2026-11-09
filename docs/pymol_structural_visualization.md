# PyMOL-Based Structural Visualisation of SpCas9

## 1. Objective
To visualise the experimentally determined three-dimensional structure of Streptococcus pyogenes Cas9 (SpCas9) in complex with guide RNA and target DNA.

## 2. Structure information
- PDB ID: 7S3H
- Structure format: mmCIF
- Structure file: data/structures/spcas9_7S3H.cif
- Experimental method: Cryo-electron microscopy (cryo-EM)
- Reported resolution: 2.5 Å
- Visualisation software: PyMOL 3.1.9

## 3. Chain identification

| Chain | Component | Extracted residues |
|---|---|---:|
| P | SpCas9 protein | 1,030 |
| R | Guide RNA | 30 |
| N | DNA | 23 |
| T | DNA | 23 |

## 4. Visualisation procedure

The structure was opened in PyMOL and inspected using cartoon representation.

The following colour scheme was applied:

- Chain P: Marine blue (SpCas9 protein)
- Chain R: Yellow (guide RNA)
- Chain T: Orange (DNA)
- Chain N: Salmon (DNA)

The nucleic acid chains were also displayed using stick representation to inspect their structural arrangement.

The structure was rotated, zoomed and oriented to obtain a suitable overall view.

## 5. Functional significance

- REC lobe: Involved in guide RNA and target DNA recognition.
- HNH domain: Responsible for cleavage of the target DNA strand.
- RuvC domain: Responsible for cleavage of the non-target DNA strand.
- PAM-interacting region: Participates in recognition of the protospacer-adjacent motif.

These functional annotations were obtained from sequence-based domain analysis. Separate domain-specific structural colouring has not yet been completed.

## 6. Structural completeness

The extracted protein chain contains 1,030 residues compared with the 1,368-amino-acid UniProt reference sequence.

Sequence comparison identified 338 reference residues absent from the extracted coordinate sequence, distributed across five regions:

- 1–2
- 94–125
- 448–715
- 1104–1135
- 1365–1368

These residues are absent from the extracted structural coordinates and should not be interpreted as biological deletions.

A T1337C substitution was also identified relative to the UniProt reference sequence.

## 7. Saved structural outputs

1. High-resolution structural image:
   `results/spcas9_7S3H_chains.png`

2. Editable PyMOL session:
   `results/spcas9_7S3H_session.pse`

The PNG image is intended for inclusion in the final project report. The PSE session preserves the PyMOL visualisation state for further inspection.

## 8. Conclusion

PyMOL was used to visualise the SpCas9–RNA–DNA complex and distinguish its protein and nucleic acid components. This analysis complements the sequence-based characterisation, domain annotation and structural sequence comparison performed in this project.

## 9. Limitations

This work represents computational structural visualisation and interpretation. No protein expression, purification, molecular docking, molecular dynamics simulation or experimental nuclease activity assay was performed.

The structure contains unresolved regions, and sequence-derived domain boundaries should not automatically be interpreted as exact structural boundaries.
