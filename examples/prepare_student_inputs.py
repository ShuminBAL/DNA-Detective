#!/usr/bin/env python3
"""Create leakage-safe student inputs and an organizer-only answer key.

This script uses only the Python standard library. It never modifies the source
JSONL. The full source file remains public in this teaching repository, so a
truly blind assessment still requires the organizer to distribute only the
generated input files and withhold the source/answer key until submissions are
frozen.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


EXPECTED_COUNTS = {
    "Pathogenic": 14,
    "Likely Pathogenic": 6,
    "Uncertain Significance": 15,
    "Likely Benign": 4,
    "Benign": 11,
}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON at {path}:{line_number}: {exc}") from exc
            if not isinstance(record, dict):
                raise ValueError(f"Expected an object at {path}:{line_number}")
            records.append(record)
    return records


def write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def validate(records: list[dict[str, Any]]) -> Counter[str]:
    if len(records) != 50:
        raise ValueError(f"Expected 50 records, found {len(records)}")

    case_ids: list[str] = []
    labels: list[str] = []
    for index, record in enumerate(records, start=1):
        missing = [
            field
            for field in ("case_id", "variant", "disease", "human_expert")
            if field not in record
        ]
        if missing:
            raise ValueError(f"Record {index} is missing required fields: {missing}")

        case_id = record["case_id"]
        if not isinstance(case_id, str) or not case_id:
            raise ValueError(f"Record {index} has an invalid case_id")
        case_ids.append(case_id)

        expert = record["human_expert"]
        if not isinstance(expert, dict) or "classification" not in expert:
            raise ValueError(f"{case_id} has no expert classification")
        labels.append(expert["classification"])

    if len(set(case_ids)) != len(case_ids):
        duplicates = sorted(case_id for case_id, count in Counter(case_ids).items() if count > 1)
        raise ValueError(f"Duplicate case_id values: {duplicates}")

    counts = Counter(labels)
    if dict(counts) != EXPECTED_COUNTS:
        raise ValueError(
            "Unexpected classification distribution. "
            f"Expected {EXPECTED_COUNTS}, found {dict(counts)}"
        )
    return counts


def student_input(record: dict[str, Any]) -> dict[str, Any]:
    """Return only fields authorized as independent agent input."""
    return {
        "case_id": record["case_id"],
        "variant": record["variant"],
        "disease": record["disease"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("data/expert_cases_50_STUDENT.jsonl"),
        help="Full dataset containing expert labels and rationales",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs"),
        help="Directory for generated inputs and the organizer answer key",
    )
    args = parser.parse_args()

    records = read_jsonl(args.source)
    counts = validate(records)

    known_inputs: list[dict[str, Any]] = []
    vus_inputs: list[dict[str, Any]] = []
    answer_key: list[dict[str, Any]] = []

    for record in records:
        label = record["human_expert"]["classification"]
        agent_record = student_input(record)
        evaluation_group = "vus_challenge" if label == "Uncertain Significance" else "known_test"
        if evaluation_group == "vus_challenge":
            vus_inputs.append(agent_record)
        else:
            known_inputs.append(agent_record)
        answer_key.append(
            {
                "case_id": record["case_id"],
                "reference_classification": label,
                "evaluation_group": evaluation_group,
            }
        )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(args.output_dir / "known_test_inputs.jsonl", known_inputs)
    write_jsonl(args.output_dir / "vus_challenge_inputs.jsonl", vus_inputs)
    write_jsonl(args.output_dir / "organizer_answer_key.jsonl", answer_key)

    digest = hashlib.sha256(args.source.read_bytes()).hexdigest()
    print(f"Validated {len(records)} records: {dict(counts)}")
    print(f"Known-label validation inputs: {len(known_inputs)}")
    print(f"VUS challenge inputs: {len(vus_inputs)}")
    print(f"Source SHA-256: {digest}")
    print(f"Wrote outputs to: {args.output_dir.resolve()}")
    print("Keep organizer_answer_key.jsonl hidden until predictions are frozen.")


if __name__ == "__main__":
    main()
