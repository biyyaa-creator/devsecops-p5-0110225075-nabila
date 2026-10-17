# Panduan mengunggah BudgetBuddy Lite ke repository GitHub

Repository GitHub tugas: https://github.com/biyyaa-creator/devsecops-p5-0110225075-nabila

> Penting: salin ISI folder `budgetbuddy_devsecops` ke root repository, bukan folder pembungkusnya. Setelah disalin, root repository harus berisi `README.md`, `requirements.txt`, `.github/`, `app/`, dan `tests/`.

## 1. Persiapan lokal

1. Unduh dan ekstrak ZIP project.
2. Clone repository:

```bash
git clone https://github.com/biyyaa-creator/devsecops-p5-0110225075-nabila.git
cd devsecops-p5-0110225075-nabila
```

3. Salin seluruh isi folder hasil ekstraksi `budgetbuddy_devsecops` ke folder hasil clone, lalu izinkan file `README.md` dan `.gitignore` ditimpa. Pastikan folder tersembunyi `.github/workflows/` ikut tersalin.
4. Dari root repository, jalankan:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m bandit -r app -ll
```

5. Jika test berhasil, commit dan push:

```bash
git add -A
git commit -m "feat: add BudgetBuddy DevSecOps pipeline"
git push origin main
```

## 2. Verifikasi GitHub Actions

1. Buka tab **Actions** pada repository GitHub.
2. Buka run terbaru bernama **BudgetBuddy DevSecOps Pipeline**.
3. Pastikan job **Build and Unit Test** dan **Bandit SAST and Quality Gate** berstatus hijau.
4. Buka job SAST dan pastikan langkah **Scan source and enforce Quality Gate** berhasil. Di bagian Artifacts, unduh `budgetbuddy-bandit-report` untuk melihat laporan JSON.
5. Jika job gagal, baca log langkah yang merah terlebih dahulu. Jangan mengubah ambang Quality Gate hanya untuk membuat pipeline hijau tanpa memeriksa temuan.

## 3. Screenshot untuk laporan

- Screenshot repository Code pada halaman utama, menampilkan nama repository, file/folder root, dan bagian README.
- Screenshot tab Actions yang menampilkan run berhasil beserta dua job yang hijau.
- Simpan screenshot asli dan masukkan ke bagian lampiran laporan. Ambil screenshot setelah workflow benar-benar dijalankan; jangan membuat atau mengedit screenshot seolah-olah merupakan hasil GitHub.
