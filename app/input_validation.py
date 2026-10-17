"""Validation helpers for expense descriptions, categories, and amounts."""
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def validate_text(value: str, field_name: str, max_length: int = 80) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{field_name} harus berupa teks.")
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"{field_name} tidak boleh kosong.")
    if len(cleaned) > max_length:
        raise ValueError(f"{field_name} maksimal {max_length} karakter.")
    return cleaned


def validate_amount(value: str | int | float | Decimal) -> str:
    try:
        amount = Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError("Nominal harus berupa angka yang valid.") from exc
    if not amount.is_finite() or amount <= 0:
        raise ValueError("Nominal harus lebih besar dari nol.")
    normalized = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return format(normalized, "f")


def validate_record_id(record_id: int) -> int:
    if isinstance(record_id, bool) or not isinstance(record_id, int) or record_id < 1:
        raise ValueError("ID transaksi harus berupa bilangan bulat positif.")
    return record_id
