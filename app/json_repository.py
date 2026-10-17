"""JSON file storage for expense records."""
import json
from pathlib import Path
from typing import Any


def read_records(path: str | Path) -> list[dict[str, Any]]:
    target = Path(path)
    if not target.exists():
        return []
    try:
        with target.open("r", encoding="utf-8") as stream:
            records = json.load(stream)
    except json.JSONDecodeError as exc:
        raise ValueError("File transaksi berisi JSON yang tidak valid.") from exc
    if not isinstance(records, list) or any(not isinstance(row, dict) for row in records):
        raise ValueError("Format data transaksi tidak valid.")
    return records


def write_records(path: str | Path, records: list[dict[str, Any]]) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(target.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8") as stream:
        json.dump(records, stream, ensure_ascii=False, indent=2)
    temporary.replace(target)
