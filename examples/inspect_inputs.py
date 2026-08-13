#!/usr/bin/env python3
"""Inspect the DNA Detective VCF and phenopacket without external packages."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


HPO_ID = re.compile(r"^\s+id:\s+(HP:\d+)\s*$")
LABEL = re.compile(r"^\s+label:\s+(.+?)\s*$")
ASSEMBLY = re.compile(r"^\s+genomeAssembly:\s+(.+?)\s*$")


def parse_phenopacket(path: Path) -> tuple[list[tuple[str, str]], str | None]:
    terms: list[tuple[str, str]] = []
    pending_id: str | None = None
    assembly: str | None = None

    for line in path.read_text(encoding="utf-8").splitlines():
        if match := HPO_ID.match(line):
            pending_id = match.group(1)
            continue
        if pending_id and (match := LABEL.match(line)):
            terms.append((pending_id, match.group(1)))
            pending_id = None
            continue
        if match := ASSEMBLY.match(line):
            assembly = match.group(1)

    return terms, assembly


def genotype_class(sample_value: str, format_value: str) -> str:
    keys = format_value.split(":")
    values = sample_value.split(":")
    fields = dict(zip(keys, values))
    gt = fields.get("GT", "./.").replace("|", "/")
    if gt == "0/0":
        return "hom_ref"
    if gt in {"0/1", "1/0"}:
        return "het"
    if gt == "1/1":
        return "hom_alt"
    return "other_or_missing"


def inspect_vcf(path: Path) -> dict[str, object]:
    samples: list[str] = []
    records = 0
    passed = 0
    chromosomes: Counter[str] = Counter()
    genotypes: Counter[str] = Counter()
    assembly_tags: set[str] = set()

    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("##contig="):
                match = re.search(r"assembly=([^,>]+)", line)
                if match:
                    assembly_tags.add(match.group(1))
                continue
            if line.startswith("#CHROM"):
                columns = line.rstrip("\n").split("\t")
                samples = columns[9:]
                continue
            if line.startswith("#"):
                continue

            columns = line.rstrip("\n").split("\t")
            if len(columns) < 8:
                raise ValueError(f"Malformed VCF record at record {records + 1}")
            records += 1
            chromosomes[columns[0]] += 1
            if columns[6] == "PASS":
                passed += 1
            if len(columns) >= 10:
                genotypes[genotype_class(columns[9], columns[8])] += 1

    return {
        "samples": samples,
        "records": records,
        "passed": passed,
        "chromosomes": chromosomes,
        "genotypes": genotypes,
        "assembly_tags": sorted(assembly_tags),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vcf", type=Path, default=Path("data/Pfeiffer.vcf"))
    parser.add_argument(
        "--phenopacket",
        type=Path,
        default=Path("data/pfeiffer-phenopacket.yml"),
    )
    args = parser.parse_args()

    terms, phenopacket_assembly = parse_phenopacket(args.phenopacket)
    vcf = inspect_vcf(args.vcf)

    print("DNA Detective input summary")
    print(f"VCF:              {args.vcf}")
    print(f"Samples:          {', '.join(vcf['samples'])}")
    print(f"Assembly tags:    {', '.join(vcf['assembly_tags'])}")
    print(f"Phenopacket build:{' ' if phenopacket_assembly else ''}{phenopacket_assembly}")
    print(f"Variant records:  {vcf['records']:,}")
    print(f"PASS records:     {vcf['passed']:,}")
    print(f"Sequence names:   {len(vcf['chromosomes'])}")
    print("Genotypes:")
    for name, count in sorted(vcf["genotypes"].items()):
        print(f"  {name:18s} {count:,}")
    print("HPO terms:")
    for term_id, label in terms:
        print(f"  {term_id}  {label}")

    if vcf["samples"] != ["manuel"]:
        raise SystemExit("Unexpected VCF sample name")
    if vcf["records"] != 37_709:
        raise SystemExit("Unexpected VCF record count")
    if len(terms) != 6:
        raise SystemExit("Unexpected HPO term count")


if __name__ == "__main__":
    main()
