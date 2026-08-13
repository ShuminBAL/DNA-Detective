#!/usr/bin/env python3
"""Convert the raw VCF records into a simple candidate TSV for exploration."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vcf", type=Path, default=Path("data/Pfeiffer.vcf"))
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("outputs/Pfeiffer.raw_candidates.tsv"),
    )
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)

    sample_names: list[str] = []
    rows = 0
    with args.vcf.open(encoding="utf-8") as source, args.output.open(
        "w", encoding="utf-8", newline=""
    ) as destination:
        writer = csv.writer(destination, delimiter="\t", lineterminator="\n")
        writer.writerow(
            [
                "candidate_id",
                "chrom",
                "pos",
                "vcf_id",
                "ref",
                "alt",
                "qual",
                "filter",
                "info",
                "format",
                "sample",
                "sample_value",
            ]
        )

        for line in source:
            if line.startswith("#CHROM"):
                sample_names = line.rstrip("\n").split("\t")[9:]
                continue
            if line.startswith("#"):
                continue
            columns = line.rstrip("\n").split("\t")
            if len(columns) < 8:
                raise ValueError(f"Malformed VCF row after {rows} records")

            chrom, pos, vcf_id, ref, alts, qual, filter_value, info = columns[:8]
            format_value = columns[8] if len(columns) > 8 else ""
            sample_value = columns[9] if len(columns) > 9 else ""
            sample = sample_names[0] if sample_names else ""

            for alt in alts.split(","):
                writer.writerow(
                    [
                        f"{chrom}-{pos}-{ref}-{alt}",
                        chrom,
                        pos,
                        vcf_id,
                        ref,
                        alt,
                        qual,
                        filter_value,
                        info,
                        format_value,
                        sample,
                        sample_value,
                    ]
                )
                rows += 1

    print(f"Wrote {rows:,} candidate alleles to {args.output}")


if __name__ == "__main__":
    main()
