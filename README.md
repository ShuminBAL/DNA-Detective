# DNA Detective

Build an interactive AI agent that investigates **one patient's VCF and phenotypes**, ranks the variants most likely to cause the patient's disease, and explains the evidence behind the ranking.

> **Educational use only.** This is a public Exomiser demonstration case for a university summer-camp project. The repository is not a validated clinical system and must not be used for patient care.

## Your mission

You receive two files from one patient:

1. [`data/Pfeiffer.vcf`](data/Pfeiffer.vcf) — a GRCh37/hg19 VCF containing many candidate variants.
2. [`data/pfeiffer-phenopacket.yml`](data/pfeiffer-phenopacket.yml) — six Human Phenotype Ontology (HPO) terms describing the patient.

Build an agent that answers:

> **Which variants are most likely to explain this patient's disease, and why?**

Your agent should not simply return one score. It should gather evidence from professional resources, compare candidates, keep a traceable evidence log, explain conflicts, and answer follow-up questions.

## Target

Submit:

- a list of candidate pathogenic variants;
- Evidence of why the agent selected those variants (e.g, ClinGen results, AlphaMissence predictions, etc)
- a short demonstration showing that a user can ask follow-up questions; and



## Data at a glance

| Feature | Value |
|---|---:|
| Case | Public Exomiser Pfeiffer demonstration case |
| Genome assembly | GRCh37 / hg19 / b37 |
| VCF sample | `manuel` |
| VCF records | 37,709 |
| Records marked `PASS` | 37,709 |
| HPO terms | 6 |
| VCF SHA-256 | `b7d1372fe63ad618908ddf5255bb441043000dad09fa604b7c0ea7585b1c21cd` |
| Phenopacket SHA-256 | `1bb05f7c6abfc0541807f6b03039cd22a6becddc0171f89833cb2381b3ecdb09` |

The phenotype file includes syndactyly, strabismus, maxillary hypoplasia, proptosis, hypertelorism, and brachyturricephaly. Do not assume that the filename or case name is the answer; rank the variants from evidence.

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/ShuminBAL/DNA-Detective.git
cd DNA-Detective
```

### 2. Inspect the inputs

The inspection script uses only the Python standard library:

```bash
python3 examples/inspect_inputs.py
```

It checks the assembly, sample name, variant count, genotype counts, and HPO terms.

### 3. Create a simple candidate table

```bash
python3 examples/vcf_to_tsv.py
```

This writes `outputs/Pfeiffer.raw_candidates.tsv`. It is only a starting table; it is **not annotated or prioritized**.

### 4. Choose an annotation route

Use at least one professional annotator:

- **Exomiser** for phenotype-driven gene/variant prioritization;
- **Ensembl VEP** for consequence, transcript, HGVS, known-variant, and plugin annotations; or
- another established VCF annotation workflow such as SnpEff/SnpSift or ANNOVAR.

The provided files are from Exomiser CLI 15.1.0. If Exomiser is already installed, a direct run is:

```bash
java -jar exomiser-cli-15.1.0.jar analyse \
  --sample data/pfeiffer-phenopacket.yml \
  --vcf data/Pfeiffer.vcf \
  --assembly hg19
```

The explicit `--vcf` argument overrides the path stored in the original example phenopacket.

An example VEP command for a local GRCh37 cache is:

```bash
vep \
  --input_file data/Pfeiffer.vcf \
  --output_file outputs/Pfeiffer.vep.vcf \
  --vcf --assembly GRCh37 --cache --offline \
  --symbol --hgvs --canonical --check_existing \
  --force_overwrite
```

VEP installation and cache setup are separate steps. Record the VEP release and cache version in your evidence log.

### 5. Build the agent loop

A useful agent loop is:

```text
OBSERVE
  Read VCF records, genotypes, assembly, and HPO terms
      ↓
PRIORITIZE
  Consequence + rarity + phenotype match + inheritance
      ↓
INVESTIGATE
  ClinVar/ClinGen + effect models + literature + functional evidence
      ↓
COMPARE
  Supporting evidence + conflicting evidence + missing evidence
      ↓
REPLAN OR STOP
  Choose another tool, inspect another candidate, or return a ranked answer
```

The intelligence is in deciding **which candidate and which evidence source to investigate next**, not in calling every tool for every VCF row.

### 6. Produce a traceable answer

Start from [`starter/agent_brief.md`](starter/agent_brief.md) and [`starter/submission_template.json`](starter/submission_template.json). Your final report should be valid JSON and should cite the exact records used.

## Potential useful tools
The complete guide is in [`docs/toolbox.md`](docs/toolbox.md), with a short ACMG/AMP guide in [`docs/acmg_evidence_guide.md`](docs/acmg_evidence_guide.md). A strong solution can combine the following:

| Purpose | Recommended tools |
|---|---|
| Inspect and normalize VCF | `bcftools`, `vt`, VariantValidator, Mutalyzer |
| Annotate consequence/transcript/HGVS | Ensembl VEP + MANE; SnpEff/SnpSift; ANNOVAR |
| Phenotype-driven ranking | Exomiser; HPO resources |
| Population frequency | gnomAD |
| Clinical interpretations | ClinVar; ClinGen Evidence Repository, CSpec, and gene–disease validity resources |
| Splicing effect | SpliceAI |
| Missense effect | AlphaMissense, REVEL, CADD, SIFT, PolyPhen-2 |
| Literature | PubMed, LitVar2 |
| Protein/domain context | UniProt, InterPro |
| Agent implementation | Any LLM or agent framework that supports tool calls and structured JSON output |

### ClinVar and ClinGen are allowed—and useful

You may query ClinVar and ClinGen directly while ranking the candidates. Their classifications and expert-curated evidence can be important clues.

Do more than copy a displayed label. Capture enough context to explain the result:

- VCV/RCV/SCV or ClinGen record identifier;
- normalized variant and condition;
- classification;
- review status or expert-panel status;
- submitter or expert panel;
- evaluation date/version;
- conflicts among submissions;
- cited publications or criterion summaries; and
- the exact URL and retrieval date.

If ClinVar, ClinGen, phenotype matching, population frequency, and effect predictors disagree, show the disagreement. That is valuable evidence, not an error to hide.

## Minimum viable agent

A minimum usable agent should:

1. verify GRCh37/hg19 and read all six HPO terms;
2. annotate the VCF and produce stable candidate identifiers;
3. remove common or clearly irrelevant candidates while preserving the reason for each filter;
4. rank genes by phenotype relevance;
5. deep-dive into a manageable shortlist;
6. query ClinVar and ClinGen for the shortlisted variants/genes;
7. add population and consequence evidence;
8. use SpliceAI or a missense model only when applicable;
9. return a top-5–10 ranking with traceable evidence; and
10. answer a follow-up question such as “Why is candidate 1 stronger than candidate 2?”




