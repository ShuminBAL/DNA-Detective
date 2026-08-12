# DNA Detective

Build an interactive, evidence-tracing agent that investigates a genetic variant, applies ACMG/AMP reasoning, and explains what evidence supports—or does not support—its conclusion.

> **Educational use only.** This repository is designed for a university summer-camp project. It is not a validated clinical system and must not be used for diagnosis, treatment, reproductive decisions, or patient care.

## The project challenge

Given a variant, the agent should:

1. normalize the variant and confirm the genome build and transcript;
2. collect population, computational, functional, case, segregation, and literature evidence;
3. record exactly where every piece of evidence came from;
4. (suggest) map usable evidence to an appropriate ACMG/AMP criterion and strength;
5. (suggest) return a five-tier classification with uncertainty and conflicts;
6. explain its conclusion with a concise, inspectable evidence trail; and
7. interact with the user—for example, ask for missing phase or phenotype information and answer follow-up questions.


## Dataset at a glance

The main dataset is [`data/expert_cases_50_STUDENT.jsonl`](data/expert_cases_50_STUDENT.jsonl).

| Feature | Value |
|---|---:|
| Gene | `PAH` |
| Disease | Phenylketonuria / PAH deficiency |
| Format | JSON Lines: one JSON object per line |
| Total cases | 50 |
| Pathogenic or Likely Pathogenic | 20: 14 P + 6 LP |
| Variant of Uncertain Significance | 15 |
| Benign or Likely Benign | 15: 11 B + 4 LB |
| Expert source | ClinGen Phenylketonuria Variant Curation Expert Panel |
| Dataset snapshot | Downloaded 2026-08-10 |
| SHA-256 | `ead49ce0d075ed4a9ebc1555b91e10cd40cf5e59cd0f62f7cf679d733dbebdfd` |


## The most important rule: separate input from answer key

The JSONL intentionally contains both the case input and the expert interpretation. That is useful after testing, but it creates **label leakage** if the full record is passed to the agent.

| Give the agent during a blind run | Withhold until evaluation |
|---|---|
| `case_id` | `human_expert.classification` |
| `variant` | `human_expert.criteria` |
| `disease` | `human_expert.criteria_considered_not_met` |
|  | `human_expert.overall_summary` |
|  | `human_expert.curator_assessments` |
|  | supplied `references` |

Do not place the withheld fields in a prompt, vector database, retrieval index, tool response, or conversation history during independent testing.

For a truly blind competition, the organizer should distribute only the generated input files and keep the full JSONL in a private organizer location until submissions are frozen. Because this public repository contains the answer key, it can support an honor-based class exercise but cannot technically prevent students from looking up the labels.

## Prepare the two tests

The organizer can generate leakage-safe inputs with only the Python standard library:

```bash
python3 examples/prepare_student_inputs.py
```

This creates:

```text
outputs/
  known_test_inputs.jsonl       35 P/LP or B/LB cases; labels removed
  vus_challenge_inputs.jsonl    15 expert-VUS cases; rationales removed
  organizer_answer_key.jsonl    all reference labels; do not distribute early
```

Recommended evaluation sequence:

1. **Validation test:** run the agent on the 35 known P/LP and B/LB cases. Reveal the expert labels only after all predictions and evidence logs are saved.
2. **VUS challenge:** run the same  agent on the 15 expert-VUS cases. The objective is not to force reclassification. Reward the discovery of new, traceable evidence; calibrated uncertainty; conflicts; and useful next steps.
3. **Learning review:** only after testing, compare the agent's evidence with the expert ACMG criteria, summaries, comments, and literature links in the full dataset.



## A practical agent architecture

```text
User
  ↓ variant + disease + optional phenotype/family data
Agent controller
  ├─ 1. Normalization and transcript resolver
  ├─ 2. Population-frequency retriever
  ├─ 3. Consequence and prediction annotator
  ├─ 4. ClinGen/ACMG rule retriever
  ├─ 5. Literature and functional-evidence retriever
  ├─ 6. Evidence deduplicator and conflict checker
  └─ 7. ACMG evidence combiner
  ↓
Classification + confidence + evidence table + missing evidence + follow-up actions
```

A minimal usable agent does not need every tool below. A strong first version can combine variant normalization, Ensembl VEP, gnomAD, SpliceAI, AlphaMissense or REVEL, ClinGen specifications, PubMed/LitVar2, and a final ClinVar cross-check.

## Professional tools students can connect

Tool outputs change over time. Every adapter should preserve the queried identifier, assembly, transcript, tool/database release, raw field and value, retrieval time, and source URL or accession.

| Task | Professional resource | What the agent should capture |
|---|---|---|
| HGVS validation and normalization | [VariantValidator REST](https://openvar.github.io/variantValidator/rest-vv/rest_VariantValidator.html) or [Mutalyzer API](https://mutalyzer.nl/api/) | Validated HGVS, reference sequence accession/version, warnings, transcript, genomic mapping |
| Consequence annotation | [Ensembl Variant Effect Predictor](https://www.ensembl.org/info/docs/tools/vep/index.html) through web, CLI, REST, or plugins | Assembly, Ensembl release, consequence, gene, transcript, canonical/MANE flags, HGVS, protein position |
| Transcript choice | [MANE](https://www.ncbi.nlm.nih.gov/refseq/MANE/) | MANE Select/Plus Clinical accession and version; explain any transcript mismatch |
| Population frequency | [gnomAD](https://gnomad.broadinstitute.org/) | Data release, assembly, allele count, allele number, filtering allele frequency, population maximum, homozygote count, filters, and coverage caveats |
| Splicing prediction | [SpliceAI](https://github.com/Illumina/SpliceAI) or the [VEP SpliceAI plugin](https://www.ensembl.org/info/docs/tools/vep/script/vep_plugins.html) | Delta score(s), predicted position(s), transcript, model/data version; do not treat prediction as a functional experiment |
| Missense prediction | [AlphaMissense](https://github.com/google-deepmind/alphamissense) through precomputed predictions/VEP | Score, qualitative class, transcript/protein mapping, prediction release and license notice |
| Calibrated missense evidence | [REVEL through VEP plugins](https://www.ensembl.org/info/docs/tools/vep/script/vep_plugins.html) | Score and version; apply only the threshold and strength specified by the relevant ClinGen rule set |
| Gene/disease-specific ACMG rules | [ClinGen Criteria Specification Registry](https://erepo.clinicalgenome.org/cspec/) | Gene, disease, inheritance, expert panel, rule-set version, release date, criterion-specific threshold |
| Expert evidence examples | [ClinGen Evidence Repository](https://erepo.clinicalgenome.org/evrepo/) | Interpretation ID/version, expert panel, date, applied criteria, primary citations |
| Existing clinical assertions—cross-check only | [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/) and [programmatic access](https://www.ncbi.nlm.nih.gov/clinvar/docs/programmatic_access/) | Variation/VCV accession and version, condition, submitter, review status, evaluation date, conflicts, and linked evidence |
| Literature discovery | [PubMed E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/) and [LitVar2](https://www.ncbi.nlm.nih.gov/research/litvar2/) | PMID, title, publication date, matched variant/gene, study type, and the exact claim supported |
| Protein/domain context | [UniProt](https://www.uniprot.org/) | Protein accession/version, domain or active-site annotation, evidence provenance |



### How to use ClinVar/ClinGen without copying its answer

ClinVar is valuable, but its aggregate classification must not become the agent's only argument.

1. Complete normalization, population, prediction, functional, and literature retrieval first.
2. Freeze the independent evidence assessment.
3. Query ClinVar/ClinGen as a cross-check.
4. Record review status, condition, date, submitters, and conflicts—not just the displayed label.
5. Follow linked submissions and primary publications when possible.
6. If ClinVar/ClinGen disagrees with the agent, report the disagreement and identify which evidence would resolve it.

Never translate “ClinVar/ClinGen says pathogenic” into PP5. PP5 and BP6 should not be used when the underlying evidence can be inspected.


## Suggested agent output contract

Save one prediction object per input case so the submission can be evaluated automatically:

```json
{
  "case_id": "DEMO001",
  "normalized_variant": {
    "assembly": "GRCh38",
    "hgvs_g": "<validated HGVS>",
    "hgvs_c": "<validated HGVS>",
    "transcript": "<accession.version>"
  },
  "prediction": "Pathogenic|Likely Pathogenic|VUS|Likely Benign|Benign",
  "confidence": 0.0,
  "acmg_assessments": [
    {
      "criterion": "<code>",
      "strength": "<strength>",
      "direction": "pathogenic|benign",
      "status": "met|not_met|uncertain",
      "evidence_ids": ["E01"],
      "rationale": "<short evidence-based explanation>"
    }
  ],
  "conflicting_evidence": [],
  "missing_evidence": [],
  "next_actions": [],
  "evidence_log": [],
  "ruleset": {
    "framework": "ACMG/AMP",
    "gene_disease_specification": "<name/version/date>"
  }
}
```

The user interface should let a person ask questions such as:

- “Show me the exact gnomAD fields and release.”
- “Why did you apply PM2 at Supporting strength?”
- “Which paper contains functional evidence, and what experiment was performed?”
- “What evidence argues against your conclusion?”
- “Would family phase data change the result?”
- “What should we investigate next?”

## ACMG/AMP: a working introduction

The 2015 ACMG/AMP framework defines five classification categories: Pathogenic, Likely Pathogenic, Variant of Uncertain Significance, Likely Benign, and Benign. Evidence codes describe the **type**, **direction**, and **strength** of evidence; they are not labels by themselves.

Pathogenic evidence strengths:

- `PVS`: very strong
- `PS`: strong
- `PM`: moderate
- `PP`: supporting

Benign evidence strengths:

- `BA`: stand-alone
- `BS`: strong
- `BP`: supporting

### Pathogenic-direction criteria

| Code | Generic idea |
|---|---|
| `PVS1` | Predicted loss-of-function variant in a gene where loss of function is an established disease mechanism |
| `PS1` | Same amino-acid change as an established pathogenic variant, with splice effects checked |
| `PS2` | Confirmed de novo occurrence in an appropriate affected individual |
| `PS3` | Well-established functional study supports a damaging effect |
| `PS4` | Variant enriched in affected individuals compared with controls |
| `PM1` | Located in a critical functional domain or mutational hotspot with little benign variation |
| `PM2` | Absent or sufficiently rare in population data for the disease model |
| `PM3` | For a recessive disease, observed in trans with a pathogenic variant |
| `PM4` | Protein-length-changing in-frame or stop-loss variant |
| `PM5` | Different missense change at a residue where another pathogenic missense variant is established |
| `PM6` | Assumed de novo without full parentage confirmation |
| `PP1` | Co-segregation with disease in informative family members |
| `PP2` | Missense variant in a gene where missense is a common disease mechanism and benign missense variation is uncommon |
| `PP3` | Calibrated computational evidence supports a damaging or splice-altering effect |
| `PP4` | Phenotype/family history is highly specific for the gene–disease relationship |
| `PP5` | Legacy reputable-source assertion; ClinGen recommends not using it without inspecting the evidence |

### Benign-direction criteria

| Code | Generic idea |
|---|---|
| `BA1` | Population frequency is high enough to be stand-alone benign evidence |
| `BS1` | Population frequency is greater than expected for the disorder |
| `BS2` | Observed in a healthy individual in a genotype incompatible with a fully penetrant early-onset disorder |
| `BS3` | Well-established functional study shows no damaging effect |
| `BS4` | Lack of segregation with disease in informative relatives |
| `BP1` | Missense variant in a gene where disease is primarily caused by truncating variants |
| `BP2` | Observed in a configuration inconsistent with causality under the relevant inheritance model |
| `BP3` | In-frame change in a repetitive region without known function |
| `BP4` | Calibrated computational evidence supports no effect on protein or splicing |
| `BP5` | Another molecular cause better explains the case |
| `BP6` | Legacy reputable-source assertion; ClinGen recommends not using it without inspecting the evidence |
| `BP7` | Synonymous or noncoding variant with no predicted splice impact under the applicable specification |


## Evaluation rubric

### Phase 1: known P/LP versus B/LB cases

Classification metrics:

- confusion matrix;
- balanced accuracy;
- precision, recall, and F1 by class;
- optional five-tier agreement after the primary P/LP versus B/LB comparison.

Scientific-quality metrics:

- correct normalization, build, and transcript;
- appropriate ACMG criterion and strength;
- traceable source/version/raw value for each claim;
- explicit conflicts and missing evidence;
- calibrated confidence; and
- useful answers to follow-up questions.

Accuracy without traceable evidence should not receive full credit.

### Phase 2: expert-VUS challenge

- whether they find relevant evidence not present in the initial input;
- whether each claim links to a source, version, and raw result;
- whether literature claims match the actual experiment or cohort;
- whether conflicts and study limitations are preserved;
- whether the conclusion remains appropriately uncertain; and
- whether the agent proposes the most informative next evidence, such as family phase, a validated assay, better phenotype data, or a newer expert review.

Any proposed reclassification should be clearly marked **research/educational only** and supported by a reproducible evidence package.




