# BudgetBuddy Lite - DevSecOps P5

BudgetBuddy Lite adalah aplikasi command-line Python untuk mencatat pengeluaran pribadi. Aplikasi mendukung tambah transaksi, melihat daftar transaksi, menghitung total pengeluaran, serta menghapus transaksi. Data disimpan secara lokal dalam berkas JSON.

## Fitur

- Menambahkan pengeluaran dengan deskripsi, nominal, dan kategori.
- Menampilkan seluruh transaksi dan menghitung total menggunakan `Decimal`.
- Menghapus transaksi berdasarkan ID.
- Memvalidasi input agar deskripsi/kategori tidak kosong dan nominal harus positif.
- Menyimpan data dalam format JSON.

## Teknologi

- Python 3.12
- `pytest` untuk unit test
- `Bandit` untuk Static Application Security Testing (SAST)
- GitHub Actions untuk Continuous Integration dan Quality Gate

## Struktur project

```text
.github/workflows/devsecops.yml  # Pipeline build, test, SAST, dan Quality Gate
app/                              # Source code aplikasi
  commands.py
  entrypoint.py
  expense_service.py
  input_validation.py
  json_repository.py
  reporting.py
  __init__.py
tests/test_expense_service.py     # Unit test
requirements.txt                  # Dependency Python
README.md
```

## Persiapan dan cara menjalankan

Pastikan Python 3.12 dan Git sudah terpasang. Jalankan perintah dari root repository.

```bash
python -m pip install -r requirements.txt
python -m app.entrypoint add "Makan siang" 25000 --category Makanan
python -m app.entrypoint add "Ongkos bus" 8000 --category Transportasi
python -m app.entrypoint list
python -m app.entrypoint total
python -m app.entrypoint remove 1
```

Data tersimpan di `expenses.json`. Untuk memakai lokasi file berbeda, berikan opsi `--data` sebelum subperintah, contoh:

```bash
python -m app.entrypoint --data demo.json list
```

## Menjalankan test dan SAST secara lokal

```bash
python -m pytest -q
python -m bandit -r app -ll
```

## Overview pipeline CI/CD

Workflow berada di `.github/workflows/devsecops.yml` dan berjalan ketika ada `push` ke branch `main` atau `pull_request` yang menargetkan `main`. Semua job menggunakan `ubuntu-latest`.

1. **Build and Unit Test (`build`)** - menyiapkan Python 3.12, menginstal dependency dari `requirements.txt`, lalu menjalankan `python -m pytest -q`.
2. **Bandit SAST and Quality Gate (`sast-scan`)** - hanya berjalan setelah `build` berhasil (`needs: build`), kemudian memindai folder `app` dengan Bandit dan mengunggah laporan JSON sebagai artifact.

## Quality Gate

Perintah `bandit -r app -ll -f json -o bandit-report.json` menetapkan ambang temuan Medium dan High. Jika Bandit menemukan isu pada ambang tersebut, perintah mengembalikan status gagal sehingga job `sast-scan` gagal. Temuan Low tidak menggagalkan gate ini. Laporan `bandit-report.json` diunggah sebagai artifact untuk ditinjau, termasuk saat langkah scan gagal jika file laporan sempat dibuat.

Quality Gate ini merupakan pemeriksaan statis berbasis pola, bukan bukti bahwa aplikasi bebas dari seluruh kerentanan. Pipeline ini belum mencakup deployment, dependency vulnerability scanning, atau secret scanning.
