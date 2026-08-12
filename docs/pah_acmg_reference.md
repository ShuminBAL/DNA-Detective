# PAH ACMG reference

> Educational reference only; not for clinical decision-making.

Official source: [ClinGen Phenylketonuria Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for PAH Version 2.0](https://erepo.clinicalgenome.org/cspec/ui/svi/doc/135637578)

Registry version: 2.0.0 (API content field: 2.0)

Released: 2024-07-16

Gene/disease: PAH / phenylketonuria (MONDO:0009861)

DOI: https://doi.org/10.5281/zenodo.21421465

Each section separates the generic ACMG concept from the PAH-specific ClinGen VCEP specification. The PAH notes are concise source-backed extracts; consult the official record for the complete rule text and attachments.

## PVS1

Generic ACMG criterion: Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease. Caveats: * Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7). * Use caution interpreting LOF variants at the extreme 3’ end of a gene. * Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact. * Use caution in the presence of multiple transcripts.

PAH-specific applicability: Applicable

Allowed strength(s): Strong, Very Strong

Important PAH-specific notes:

- Very Strong: Applicable as described in Tayoun et al. 2018. * Any nonsense or frameshift variant occurring upstream of c.1285 * Any canonical splice site predicted to disrupt reading frame and undergo nonsense mediated decay PVS1 (RNA): splicing assay data - assays demonstrating a variant leads to aberrant splicing profile that can be categorized against a PVS1 decision tree * Use the PVS1 decision tree to determine code strength * Applicable as described in Walker et al. (PMID: 36865205)
- Strong: Use PVS1\_strong with: * Any nonsense or frameshift variant occurring downstream of c.1285 * Any canonical splice site predicted to preserve reading frame (skipping of exons 1, 9, 10) or affect the last exon (exon 13) * Initiator codon variant

## PS1

Generic ACMG criterion: Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

PAH-specific applicability: Applicable

Allowed strength(s): Strong

Important PAH-specific notes:

- Strong: Same predicted splicing impact as a previously classified (likely) pathogenic variant Applicable as described in Walker et al. (PMID: 36865205)

## PS2

Generic ACMG criterion: De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

PAH-specific applicability: Applicable

Allowed strength(s): Strong

Important PAH-specific notes:

- Strong: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity. Only applicable when proband has a known pathogenic variant in trans with the de novo variant.

## PS3

Generic ACMG criterion: Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

PAH-specific applicability: Applicable

Allowed strength(s): Moderate, Supporting

Important PAH-specific notes:

- Moderate: Functional studies with sufficient analyses to calculate OddsPath reaching strong have not been identified. Therefore, the strength of this criteria is modified to PS3\_moderate or PS3\_supporting for future or existing studies. In vitro enzyme activity \<50% compared to wild type controls. * Expression systems placing the mutant (and wild-type) cDNAs into plasmid vectors and introducing these into human or other mammalian host cells, which is the closest available approximation to the in vivo situation (e.g., COS cells) (Trunzo et al. Gene. 2016. 594:138-143. PMID: 27620137). * With ≥11 benign/pathogenic variant controls used in assay * NOTE: no papers that meet PS3\_Moderate criteria have been identified by the PAH VCEP at time of this specification update. However, there may be future studies that meet the above criteria where a moderate level of evidence can be applied.
- Supporting: In vitro enzyme activity ≤50% compared to wild type controls * with ≤10 benign/pathogenic variant controls used in assay
- Functional studies with sufficient analyses to calculate OddsPath reaching strong have not been identified. Therefore, the strength of this criteria is modified to PS3_moderate or PS3_supporting for future or existing studies.

## PS4

Generic ACMG criterion: The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls. Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance. Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

PAH-specific applicability: Not applicable

Allowed strength(s): Not applicable / none specified

Important PAH-specific notes:

- This criterion is not applicable for PAH. For proband counting, use PM3 criterion.

## PM1

Generic ACMG criterion: Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

PAH-specific applicability: Applicable

Allowed strength(s): Moderate

Important PAH-specific notes:

- Moderate: * Active site residues in PAH include: Tyr138, Arg158, Val245, Tyr268, Thr278, Pro279, Glu289, Ala300, Asp315, Phe331, Ala345, Gly346, Ser349, Tyr377 * Substrate binding residues in PAH are: 46-48, 63-69 * Cofactor binding residues in PAH are: His285, His290, Glu330, 246-266, 280-283, 322-326, 377-379 * Do not apply if PP3\_Strong applies

## PM2

Generic ACMG criterion: Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

PAH-specific applicability: Applicable

Allowed strength(s): Supporting

Important PAH-specific notes:

- Supporting: * Threshold \<0.0002 (0.02%) The 0.0002 cutoff is based on disease frequency of 1:12,000 and the most common PAH pathogenic variant, R408W, the ExAC frequency is 0.0006594 (ExAC MAF: 0.001109 74/66718 European Non-Finnish) and gnomAD overall: 0.0009056 (gnomAD MAF: 0.001728 219/126,700 European Non-Finnish).

## PM3

Generic ACMG criterion: For recessive disorders, detected in trans with a pathogenic variant Note: This requires testing of parents (or offspring) to determine phase.

PAH-specific applicability: Applicable

Allowed strength(s): Strong, Moderate, Supporting, Very Strong

Important PAH-specific notes:

- Very Strong: Applicable as described in SVI recommendations for in trans criterion
- Strong: Applicable as described in SVI recommendations for in trans criterion
- Moderate: Applicable as described in SVI recommendations for in trans criterion
- Supporting: Applicable as described in SVI recommendations for in trans criterion

## PM4

Generic ACMG criterion: Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

PAH-specific applicability: Applicable

Allowed strength(s): Moderate

Important PAH-specific notes:

- Moderate: Applicable as described

## PM5

Generic ACMG criterion: Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

PAH-specific applicability: Applicable

Allowed strength(s): Moderate, Supporting

Important PAH-specific notes:

- Moderate: Applicable as described.
- Supporting: Applicable when the different missense change is likely pathogenic.

## PM6

Generic ACMG criterion: Assumed de novo, but without confirmation of paternity and maternity.

PAH-specific applicability: Not applicable

Allowed strength(s): Not applicable / none specified

Important PAH-specific notes:

- No separate PAH-specific instruction was present in the structured record.

## PP1

Generic ACMG criterion: Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

PAH-specific applicability: Applicable

Allowed strength(s): Strong, Moderate, Supporting

Important PAH-specific notes:

- Strong: * 3 affected segregations + 0 unaffected segregations OR * 2 affected segregations + 3 unaffected segregations
- Moderate: * 2 affected segregations + 0 unaffected segregations
- Supporting: * 1 affected family member + 3 unaffected segregations

## PP2

Generic ACMG criterion: Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

PAH-specific applicability: Not applicable

Allowed strength(s): Not applicable / none specified

Important PAH-specific notes:

- No separate PAH-specific instruction was present in the structured record.

## PP3

Generic ACMG criterion: Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

PAH-specific applicability: Applicable

Allowed strength(s): Strong, Moderate, Supporting

Important PAH-specific notes:

- Per SVI recommendations (PMID: 36865205), PP3 should not be used for variants with experimental evidence of altered splicing; for variants without experimental evidence of altered splicing, PP3 can be used for variants that have a SpliceAI delta score of ≥0.2.
- Strong: * Applicable as described in Pejaver et al (PMID: 36413997): REVEL score ≥0.932 for missense variants * PP3 + PM1 should not exceed Strong
- Moderate: Applicable as described in Pejaver et al (PMID: 36413997): REVEL score 0.773 - 0.932 for missense variants
- Supporting: Applicable as described in Pejaver et al. (PMID: 36413997): * REVEL score of 0.644 - 0.733 for missense variants * In frame deletion or insertion predicted deleterious by 2 out of 3 tools (PROVEAN, MutationTaster, MutPred-InDel) * Predicted impact on splicing by SpliceAI (score >0.5)

## PP4

Generic ACMG criterion: Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology.

PAH-specific applicability: Applicable

Allowed strength(s): Moderate, Supporting

Important PAH-specific notes:

- Moderate: Plasma phenylalanine concentration persistently above 120 µmol/L (2mg/dL), and either normal urine pterins and normal DHPR activity, or sequencing of genes in the BH4 cofactor metabolism pathway to exclude a defect of BH4 cofactor metabolism.
- Supporting: A plasma phenylalanine concentration persistently above 120umol/L (2mg/dL) without analysis of urine pterins, DHPR activity, or sequencing to exclude defects of BH4 cofactor metabolism.

## PP5

Generic ACMG criterion: Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

PAH-specific applicability: Not Applicable for this VCEP

Allowed strength(s): Not applicable / none specified

Important PAH-specific notes:

- This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

References: https://pubmed.ncbi.nlm.nih.gov/29543229

## BA1

Generic ACMG criterion: Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

PAH-specific applicability: Applicable

Allowed strength(s): Stand Alone

Important PAH-specific notes:

- Stand Alone: An allele frequency ≥0.015 (1.5%), which is calculated with genetic heterogeneity of 90% to account for defects of BH4 metabolism, and penetrance of 80% to account for individuals who come to attention after becoming clinically symptomatic.

## BS1

Generic ACMG criterion: Allele frequency is greater than expected for disorder.

PAH-specific applicability: Applicable

Allowed strength(s): Strong

Important PAH-specific notes:

- Strong: Allele frequency ≥0.002 (0.2%)

## BS2

Generic ACMG criterion: Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

PAH-specific applicability: Applicable

Allowed strength(s): Strong

Important PAH-specific notes:

- Strong: Only to be used when variant is observed in the homozygous state in a healthy adult.

## BS3

Generic ACMG criterion: Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

PAH-specific applicability: Applicable

Allowed strength(s): Supporting

Important PAH-specific notes:

- Supporting: In vitro enzyme activity >85% compared to wild type * Expression systems: placing the mutant (and wildtype) cDNA into plasmid vectors and introducing these into host cells. Transiently transfected human or other mammalian host cells are the closest available approximation to the in vivo situation (e.g., COS cells) (Trunzo, et al. Gene. 2016. 594:138-143).

## BS4

Generic ACMG criterion: Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

PAH-specific applicability: Applicable

Allowed strength(s): Strong

Important PAH-specific notes:

- Strong: Applicable as described

## BP1

Generic ACMG criterion: Missense variant in a gene for which primarily truncating variants are known to cause disease.

PAH-specific applicability: Not applicable

Allowed strength(s): Not applicable / none specified

Important PAH-specific notes:

- No separate PAH-specific instruction was present in the structured record.

## BP2

Generic ACMG criterion: Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

PAH-specific applicability: Not applicable

Allowed strength(s): Not applicable / none specified

Important PAH-specific notes:

- No separate PAH-specific instruction was present in the structured record.

## BP3

Generic ACMG criterion: In frame-deletions/insertions in a repetitive region without a known function.

PAH-specific applicability: Not applicable

Allowed strength(s): Not applicable / none specified

Important PAH-specific notes:

- No separate PAH-specific instruction was present in the structured record.

## BP4

Generic ACMG criterion: Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc) Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

PAH-specific applicability: Applicable

Allowed strength(s): Strong, Moderate, Supporting

Important PAH-specific notes:

- BP4\_very strong: applicable as described in Pejaver et al.
- Strong: Applicable as described in Pejaver et al.
- Moderate: Applicable as described in Pejaver et al.
- Supporting: Applicable as described in Pejaver et al. * REVEL score of 0.183 - 0.290 for missense variants * In frame deletion or insertion predicted benign by PROVEAN, MutationTaster, and MutPred-InDel * No predicted impact on splicing by SpliceAI (score \<0.1)

## BP5

Generic ACMG criterion: Variant found in a case with an alternate molecular basis for disease.

PAH-specific applicability: Applicable

Allowed strength(s): Supporting

Important PAH-specific notes:

- Supporting: Applicable as described

## BP6

Generic ACMG criterion: Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

PAH-specific applicability: Not Applicable for this VCEP

Allowed strength(s): Not applicable / none specified

Important PAH-specific notes:

- This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee.

References: https://pubmed.ncbi.nlm.nih.gov/29543229

## BP7

Generic ACMG criterion: A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

PAH-specific applicability: Applicable

Allowed strength(s): Strong, Supporting

Important PAH-specific notes:

- Strong: Applicable as described by Walker et al. (PMID: 36865205).
- Supporting: Per SVI recommendations (PMID: 36865205), use BP7 only if BP4 is met; for variants with experimental evidence supporting that they do not alter splicing, use BP7\_strong (RNA) * intronic variants must be outside +7/-21 nt * exonic variants must be outside first and last 3 bases of exon
