# Submission format

Submit one JSON file named `dna_detective_report.json`. It should contain a ranked shortlist and the evidence supporting every important claim.

Use [`starter/submission_template.json`](../starter/submission_template.json) as the starting point.

## Required top-level fields

| Field | Meaning |
|---|---|
| `team` | Team name or identifier |
| `case_id` | `manuel` for this challenge |
| `input` | Input file names, assembly, sample, and phenotype identifiers |
| `method` | Agent/model version, tools used, and run time |
| `top_candidates` | Ordered list of the top 5–10 candidates |
| `evidence_log` | Traceable raw evidence records |
| `follow_up_examples` | At least two user questions and agent answers |
| `limitations` | Known weaknesses or incomplete evidence |

## Candidate fields

Each object in `top_candidates` must contain:

- `rank`;
- `candidate_id` in a stable `CHROM-POS-REF-ALT` form;
- normalized genomic and HGVS descriptions where available;
- gene, transcript, consequence, and zygosity;
- possible disease and inheritance;
- `phenotype_match` with matched HPO terms;
- `supporting_evidence_ids`;
- `conflicting_evidence_ids`;
- `missing_evidence`;
- a concise `reason_for_rank`; and
- `confidence`, clearly defined by the team.

`confidence` is not automatically a clinical probability. Explain how it was produced.

## Evidence traceability

Every database or model claim should point to one or more entries in `evidence_log`. A valid evidence item includes:

- source/tool;
- accession or query;
- raw field and value;
- assembly and transcript when relevant;
- version or retrieval date;
- URL; and
- limitations.

## Follow-up examples

Include at least two interactions, for example:

- “Why is candidate 1 more suspicious than candidate 2?”
- “Show the ClinVar and ClinGen evidence.”
- “Which phenotype terms drive the ranking?”
- “What evidence argues against your top candidate?”
- “What should we investigate next?”

The answers should use the saved evidence rather than making new unsupported claims.

## Validation checklist

Before submission:

- [ ] JSON parses successfully.
- [ ] Ranks start at 1 and are unique.
- [ ] There are 5–10 candidates.
- [ ] Every referenced evidence ID exists.
- [ ] Every major claim has a source.
- [ ] GRCh37/GRCh38 is never ambiguous.
- [ ] ClinVar/ClinGen records include condition and review/expert context.
- [ ] Predictor scores include model or dataset version.
- [ ] Conflicting and missing evidence is visible.
- [ ] No API keys, passwords, or private tokens are included.
