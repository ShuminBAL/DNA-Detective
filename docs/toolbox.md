# Student toolbox

You do not need every tool in this document. Choose a small set that covers the evidence your agent needs, connect those tools reliably, and record every result.

The input case uses **GRCh37/hg19**. Never mix GRCh37 and GRCh38 coordinates without an explicit, documented lift-over.

## Recommended workflow

| Stage | Question | Good tool choices | Save these fields |
|---|---|---|---|
| 1. Inspect | Is the VCF readable and which assembly/sample does it use? | `bcftools`, repository scripts | assembly, sample, genotype, FILTER, QUAL |
| 2. Normalize | Is the variant representation stable? | `bcftools norm`, `vt`, VariantValidator, Mutalyzer | normalized CHROM/POS/REF/ALT, HGVS, reference accession |
| 3. Annotate | Which gene/transcript and consequence are affected? | Ensembl VEP, SnpEff/SnpSift, ANNOVAR | gene, transcript, consequence, HGVSc, HGVSp, canonical/MANE flag |
| 4. Phenotype | Does the gene/disease match the HPO profile? | Exomiser, HPO, Monarch resources | HPO terms, disease, gene, phenotype score, inheritance |
| 5. Population | Is the variant too common for a rare disorder? | gnomAD | dataset release, AC, AN, AF, population maximum, homozygotes, filters |
| 6. Clinical | Has the variant or gene been clinically interpreted? | ClinVar, ClinGen | accessions, condition, classification, review status, date, conflicts |
| 7. Effect | Could the variant alter protein or splicing? | SpliceAI, AlphaMissense, REVEL, CADD | score, class, transcript, model/data version |
| 8. Literature | What experiments or case reports support the claim? | PubMed, LitVar2 | PMID, study type, exact supported claim, limitations |
| 9. Compare | Why is one candidate stronger than another? | Your agent's evidence table | supporting, conflicting, missing evidence, next action |

## VCF inspection and normalization

### bcftools

[bcftools](https://samtools.github.io/bcftools/) can inspect, query, filter, normalize, and manipulate VCF/BCF files.

Useful inspection commands:

```bash
bcftools view -h data/Pfeiffer.vcf
bcftools stats data/Pfeiffer.vcf > outputs/Pfeiffer.stats.txt
bcftools query -l data/Pfeiffer.vcf
```

Normalization requires the matching GRCh37 reference FASTA:

```bash
bcftools norm \
  --fasta-ref /path/to/GRCh37.fa \
  --multiallelics -any \
  --output-type z \
  --output outputs/Pfeiffer.normalized.vcf.gz \
  data/Pfeiffer.vcf
```

Do not silently change the assembly. Record the reference FASTA name and checksum.

### HGVS validation

- [VariantValidator REST API](https://openvar.github.io/variantValidator/rest-vv/rest_VariantValidator.html)
- [Mutalyzer API](https://mutalyzer.nl/api/)

Use these for shortlisted variants when you need stable genomic, transcript, and protein descriptions.

## Consequence annotation

### Ensembl Variant Effect Predictor

- [VEP overview](https://www.ensembl.org/info/docs/tools/vep/index.html)
- [Command-line documentation](https://www.ensembl.org/info/docs/tools/vep/script/index.html)
- [Input/output formats](https://www.ensembl.org/info/docs/tools/vep/vep_formats.html)
- [Plugins](https://www.ensembl.org/info/docs/tools/vep/script/vep_plugins.html)

Example with a local GRCh37 cache:

```bash
vep \
  --input_file data/Pfeiffer.vcf \
  --output_file outputs/Pfeiffer.vep.vcf \
  --vcf --assembly GRCh37 --cache --offline \
  --symbol --hgvs --canonical --check_existing \
  --force_overwrite
```

VEP writes consequence annotations to the `CSQ` INFO field in VCF output. Parse the field order from the generated VCF header rather than assuming a fixed order.

Useful alternatives:

- [SnpEff/SnpSift](https://pcingola.github.io/SnpEff/)
- [ANNOVAR](https://annovar.openbioinformatics.org/) — check its download and license terms

## Phenotype-driven prioritization

### Exomiser 15.1.0

- [Input files and command options](https://exomiser.readthedocs.io/en/stable/input_files_and_options.html)
- [Analysis/job configuration](https://exomiser.readthedocs.io/en/stable/advanced_analysis.html)

```bash
java -jar exomiser-cli-15.1.0.jar analyse \
  --sample data/pfeiffer-phenopacket.yml \
  --vcf data/Pfeiffer.vcf \
  --assembly hg19
```

Exomiser can provide a strong initial ranking. Your agent should still explain which phenotype and variant evidence supports each leading candidate.

### HPO resources

- [Human Phenotype Ontology](https://hpo.jax.org/app/)
- [Monarch Initiative](https://monarchinitiative.org/)

Keep the original HPO identifiers. If you expand the phenotype set with ancestors or related terms, record that transformation.

## Population evidence

### gnomAD

- [gnomAD browser](https://gnomad.broadinstitute.org/)

For each shortlisted variant, record:

- genome build and gnomAD release;
- exome/genome dataset;
- allele count and allele number;
- overall and ancestry-specific allele frequency;
- homozygote count;
- quality filters and coverage caveats; and
- the variant-page URL or query identifier.

Absence from gnomAD is only meaningful when the locus is adequately covered and the variant representation was normalized correctly.

## ClinVar and ClinGen

Direct use of both resources is allowed in this project.

### ClinVar

- [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/)
- [How to access ClinVar data](https://www.ncbi.nlm.nih.gov/clinvar/docs/access/)
- [Programmatic use and downloads](https://www.ncbi.nlm.nih.gov/clinvar/docs/maintenance_use/)

ClinVar supports web search, downloadable VCF/XML files, and NCBI E-utilities. For each result, save:

- VCV/RCV/SCV accession and version when available;
- condition and inheritance context;
- aggregate classification;
- review status/stars;
- evaluation date;
- submitters and conflicts;
- cited PMIDs or supporting descriptions; and
- URL plus retrieval date.

### ClinGen

- [ClinGen tools](https://www.clinicalgenome.org/tools/)
- [Evidence Repository](https://erepo.clinicalgenome.org/evrepo/)
- [Criteria Specification Registry](https://erepo.clinicalgenome.org/cspec/)
- [Gene–disease validity search](https://search.clinicalgenome.org/kb/gene-validity)

Use ClinGen to investigate expert-panel variant interpretations, gene–disease validity, disease/inheritance context, and gene-specific ACMG/AMP specifications when available.

## Variant-effect models

These tools predict molecular effect; they do not measure the patient's phenotype and should not replace phenotype or clinical evidence.

### SpliceAI

- [Official SpliceAI repository](https://github.com/Illumina/SpliceAI)

```bash
spliceai \
  -I data/Pfeiffer.vcf \
  -O outputs/Pfeiffer.spliceai.vcf \
  -R /path/to/GRCh37.fa \
  -A grch37
```

Record all four delta scores and positions, the annotation/build, and the software/model version. Review the license before installing or redistributing model outputs.

### AlphaMissense

- [AlphaMissense repository](https://github.com/google-deepmind/alphamissense)
- [VEP AlphaMissense plugin documentation](https://www.ensembl.org/info/docs/tools/vep/script/vep_plugins.html)

For missense variants, record the continuous pathogenicity score, qualitative class, protein/transcript mapping, prediction-data version, and the lookup method.

### REVEL and other missense predictors

The [VEP plugin documentation](https://www.ensembl.org/info/docs/tools/vep/script/vep_plugins.html) includes REVEL and other predictors. Record the score and dataset version. Do not average unrelated scores without a justified method.

Optional additional tools include [CADD](https://cadd.gs.washington.edu/), SIFT, and PolyPhen-2.

## Literature and protein context

- [PubMed](https://pubmed.ncbi.nlm.nih.gov/)
- [NCBI E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
- [LitVar2](https://www.ncbi.nlm.nih.gov/research/litvar2/)
- [UniProt](https://www.uniprot.org/)
- [InterPro](https://www.ebi.ac.uk/interpro/)

For literature evidence, capture the PMID and state exactly what the paper contributes: a functional assay, case observation, segregation, cohort enrichment, or mechanistic context. Do not claim an experiment was performed unless the paper actually reports it.

## Agent implementation

Any agent framework is acceptable if it can:

1. call tools or adapters;
2. keep structured state for candidate variants;
3. parse outputs rather than relying on screenshots;
4. produce valid JSON;
5. attach evidence identifiers to claims;
6. stop when the ranking is sufficiently supported; and
7. answer follow-up questions from the saved evidence.

Recommended internal components:

```text
case loader
  → variant normalizer
  → annotation adapter
  → phenotype-ranking adapter
  → population adapter
  → ClinVar/ClinGen adapter
  → effect-model adapter
  → literature adapter
  → evidence store
  → candidate comparator
  → final report generator
```

Cache tool responses during development. Use rate limits, timeouts, retries, and clear error messages. Never put an API secret in the repository.

## Evidence-log format

Each evidence item should look like:

```json
{
  "evidence_id": "E01",
  "candidate_id": "chr-pos-ref-alt",
  "category": "clinvar|clingen|population|phenotype|consequence|splicing|missense|literature|other",
  "source": "ClinVar",
  "record_or_accession": "VCV...",
  "query": "<exact query>",
  "assembly": "GRCh37",
  "transcript": "<accession.version or null>",
  "raw_field": "<field name>",
  "raw_value": "<value>",
  "tool_or_data_version": "<version or retrieval date>",
  "url": "https://...",
  "retrieved_at": "YYYY-MM-DDTHH:MM:SSZ",
  "interpretation": "<one sentence>",
  "limitations": ["<important caveat>"]
}
```

The final explanation should reference `evidence_id` values so every claim can be inspected.
