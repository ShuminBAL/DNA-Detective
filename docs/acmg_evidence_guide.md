# ACMG/AMP evidence guide for this project

The main task is **variant prioritization**: compare many variants from one patient and decide which ones most plausibly explain the phenotype. ACMG/AMP is a related but different task: classify one variant for a specific gene–disease relationship and inheritance model.

Students may use ACMG/AMP terminology to structure the evidence for shortlisted variants. Do not assign criteria mechanically to all 37,709 records.

## Before applying a criterion

Confirm:

1. the normalized allele and genome build;
2. gene and transcript;
3. disease and inheritance model;
4. molecular consequence and disease mechanism; and
5. whether a ClinGen expert-panel specification exists.

Use the [ClinGen Criteria Specification Registry](https://erepo.clinicalgenome.org/cspec/) when a relevant specification is available. Record its version and date.

## Evidence categories that are useful here

| Evidence question | Related ACMG/AMP concepts | Useful resources |
|---|---|---|
| Is the allele too common for the proposed rare disease? | `BA1`, `BS1`, `PM2` | gnomAD, disease prevalence/inheritance sources |
| Is loss of function an established disease mechanism? | `PVS1` | ClinGen gene–disease/mechanism evidence, literature, transcript annotation |
| Does a different nucleotide change produce an established amino-acid change? | `PS1` | ClinVar/ClinGen, transcript-aware annotation |
| Is another pathogenic missense change known at the same residue? | `PM5` | ClinVar/ClinGen, protein mapping |
| Does a validated functional experiment show an effect? | `PS3`, `BS3` | primary literature, expert-panel summaries |
| Does the phenotype strongly match the gene–disease relationship? | `PP4` | HPO, Exomiser, disease resources |
| Do calibrated computational models support an effect? | `PP3`, `BP4` | SpliceAI, AlphaMissense, REVEL, gene-specific specifications |
| Is the variant de novo or does it segregate with disease? | `PS2`, `PM6`, `PP1`, `BS4` | pedigree and family testing; not available in this singleton case unless supplied later |

## Strength matters

ACMG/AMP codes describe both evidence type and strength. A prediction score should not automatically become `PP3`, and absence from a population database should not automatically become `PM2`. Use thresholds and strengths from the relevant ClinGen specification when available.

## How to report criteria

```json
{
  "criterion": "PP3",
  "strength": "supporting",
  "status": "met|not_met|uncertain",
  "evidence_ids": ["E07", "E08"],
  "rationale": "<why these exact results satisfy the applicable rule>",
  "ruleset": "<generic ACMG/AMP or ClinGen specification name/version/date>"
}
```

The candidate ranking should still explain phenotype fit, inheritance, and comparisons with alternative variants. An ACMG classification alone does not prove that a variant explains this patient's phenotype.
