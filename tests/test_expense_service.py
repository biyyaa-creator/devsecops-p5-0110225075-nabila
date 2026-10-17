import pytest
from app.expense_service import ExpenseService
from app.input_validation import validate_amount, validate_text


def test_add_and_list_expense(tmp_path):
    service = ExpenseService(tmp_path / "expense_data.json")
    entry = service.add_expense("Kopi", "12000", "Makanan")
    assert entry["id"] == 1
    assert entry["amount"] == "12000.00"
    assert service.list_expenses() == [entry]


def test_total_uses_decimal_arithmetic(tmp_path):
    service = ExpenseService(tmp_path / "expense_data.json")
    service.add_expense("Buku", "12500.50", "Pendidikan")
    service.add_expense("Pulpen", "2500.25", "Pendidikan")
    assert service.total_expenses() == "15000.75"


def test_reject_non_positive_amount():
    with pytest.raises(ValueError):
        validate_amount("0")
    with pytest.raises(ValueError):
        validate_amount("-100")


def test_reject_empty_description():
    with pytest.raises(ValueError):
        validate_text("  ", "Deskripsi")


def test_remove_expense(tmp_path):
    service = ExpenseService(tmp_path / "expense_data.json")
    entry = service.add_expense("Parkir", "5000", "Transportasi")
    service.remove_expense(entry["id"])
    assert service.list_expenses() == []


def test_missing_record_raises_error(tmp_path):
    service = ExpenseService(tmp_path / "expense_data.json")
    with pytest.raises(KeyError):
        service.remove_expense(7)
