# Case files

This directory contains the two inputs for the DNA Detective summer-camp challenge.

## Files

### `Pfeiffer.vcf`

- Source: `exomiser-cli-15.1.0/examples/Pfeiffer.vcf`
- Format: VCF 4.1
- Assembly: b37 / GRCh37 / hg19
- Sample: `manuel`
- Records: 37,709
- SHA-256: `b7d1372fe63ad618908ddf5255bb441043000dad09fa604b7c0ea7585b1c21cd`

### `pfeiffer-phenopacket.yml`

- Source: `exomiser-cli-15.1.0/examples/pfeiffer-phenopacket.yml`
- Format: GA4GH Phenopacket schema v1 YAML
- Subject: `manuel`
- HPO terms: 6
- SHA-256: `1bb05f7c6abfc0541807f6b03039cd22a6becddc0171f89833cb2381b3ecdb09`

The phenopacket retains the original example URI `examples/Pfeiffer.vcf`. When running Exomiser from this repository, override it explicitly:

```bash
java -jar exomiser-cli-15.1.0.jar analyse \
  --sample data/pfeiffer-phenopacket.yml \
  --vcf data/Pfeiffer.vcf \
  --assembly hg19
```

These files are provided for education and reproducible demonstration, not clinical use. Refer to the Exomiser project for its software license, documentation, and citation guidance.
