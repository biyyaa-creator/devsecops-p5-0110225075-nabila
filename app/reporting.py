"""Format expenses for readable terminal output."""
from typing import Any


def format_expense(row: dict[str, Any]) -> str:
    return f"#{row['id']} | {row['description']} | {row['category']} | Rp {row['amount']}"


def format_expense_list(records: list[dict[str, Any]]) -> str:
    if not records:
        return "Belum ada transaksi."
    return "\n".join(format_expense(row) for row in records)
