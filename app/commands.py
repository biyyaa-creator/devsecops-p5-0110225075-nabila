"""Command-line argument definitions and command execution."""
import argparse
from app.expense_service import ExpenseService
from app.reporting import format_expense_list, format_expense


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="BudgetBuddy Lite - pencatat pengeluaran sederhana")
    parser.add_argument("--data", default="expenses.json", help="Lokasi file JSON transaksi")
    sub = parser.add_subparsers(dest="action", required=True)

    add = sub.add_parser("add", help="Catat pengeluaran baru")
    add.add_argument("description", help="Deskripsi pengeluaran")
    add.add_argument("amount", help="Nominal positif, misalnya 15000 atau 15000.50")
    add.add_argument("--category", default="Umum", help="Kategori pengeluaran")
    sub.add_parser("list", help="Tampilkan semua pengeluaran")
    sub.add_parser("total", help="Hitung total pengeluaran")
    remove = sub.add_parser("remove", help="Hapus transaksi berdasarkan ID")
    remove.add_argument("record_id", type=int, help="ID transaksi")
    return parser


def run_command(args: argparse.Namespace) -> int:
    service = ExpenseService(args.data)
    try:
        if args.action == "add":
            entry = service.add_expense(args.description, args.amount, args.category)
            print(f"Transaksi tersimpan: {format_expense(entry)}")
        elif args.action == "list":
            print(format_expense_list(service.list_expenses()))
        elif args.action == "total":
            print(f"Total pengeluaran: Rp {service.total_expenses()}")
        elif args.action == "remove":
            service.remove_expense(args.record_id)
            print(f"Transaksi #{args.record_id} berhasil dihapus.")
    except (ValueError, KeyError) as exc:
        print(f"Error: {exc}")
        return 1
    return 0
