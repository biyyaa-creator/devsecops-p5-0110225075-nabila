"""Business rules for recording and summarizing expenses."""
from decimal import Decimal
from pathlib import Path
from typing import Any

from app.input_validation import validate_amount, validate_record_id, validate_text
from app.json_repository import read_records, write_records


class ExpenseService:
    def __init__(self, data_path: str | Path = "expenses.json") -> None:
        self.data_path = Path(data_path)

    def list_expenses(self) -> list[dict[str, Any]]:
        return read_records(self.data_path)

    def add_expense(self, description: str, amount: str, category: str) -> dict[str, Any]:
        clean_description = validate_text(description, "Deskripsi", 100)
        clean_category = validate_text(category, "Kategori", 40)
        clean_amount = validate_amount(amount)
        records = self.list_expenses()
        next_id = max((int(row.get("id", 0)) for row in records), default=0) + 1
        entry = {
            "id": next_id,
            "description": clean_description,
            "amount": clean_amount,
            "category": clean_category,
        }
        records.append(entry)
        write_records(self.data_path, records)
        return entry

    def remove_expense(self, record_id: int) -> None:
        wanted_id = validate_record_id(record_id)
        records = self.list_expenses()
        remaining = [row for row in records if row.get("id") != wanted_id]
        if len(remaining) == len(records):
            raise KeyError(f"Transaksi dengan ID {wanted_id} tidak ditemukan.")
        write_records(self.data_path, remaining)

    def total_expenses(self) -> str:
        total = sum((Decimal(row["amount"]) for row in self.list_expenses()), Decimal("0.00"))
        return format(total.quantize(Decimal("0.01")), "f")
