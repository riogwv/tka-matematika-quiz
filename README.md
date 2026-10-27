# TKA Matematika — Ruang Belajar

Ruang belajar mandiri untuk siswa SMA/MA/SMK: konsep, rumus, latihan, dan pembahasan. **Semua soal pada website adalah latihan buatan, bukan soal resmi.**

## Isi dan cakupan

- **99 soal:** 63 Wajib (21 kelompok), 21 Tingkat Lanjut (7 kelompok), dan 15 campuran. Setiap kelompok utama memiliki tiga latihan.
- Materi per topik memuat konsep, rumus, syarat, contoh, strategi, jebakan, dan tombol latihan.
- Kuis mendukung pilihan tunggal, pilihan majemuk, dan kategori benar/salah. Soal majemuk dinilai benar jika seluruh pilihan tepat; ini adalah aturan latihan aplikasi, bukan klaim aturan penilaian resmi.
- Navigasi, penanda tinjau, timer opsional, acak soal dan opsi, rekap, pembahasan, serta rincian hasil per topik.
- Tema, sesi, skor, dan topik yang ditandai disimpan di browser melalui LocalStorage. Data tidak tersinkron antargawai dan dapat hilang saat data situs dihapus.
- Dua rumus memakai MathML pecahan; rumus lainnya menggunakan notasi Unicode. Tidak memerlukan jaringan atau layanan eksternal setelah berkas situs terunduh.

**Batas materi:** halaman kerangka Pusmendik yang diakses mencantumkan matriks, polinomial, fungsi, vektor, lingkaran, transformasi, dan limit untuk Tingkat Lanjut. Turunan dan integral ditampilkan sebagai pengayaan karena tidak terkonfirmasi sebagai submateri dalam matriks yang diakses. Kisi-kisi bisa berubah; cek sumber resmi dan pengumuman terbaru.

## Sumber

- [Kerangka Matematika Wajib Pusmendik](https://pusmendik.kemdikbud.go.id/tka/tka/view/mata-pelajaran-wajib/sma)
- [Kerangka Matematika Tingkat Lanjut Pusmendik](https://pusmendik.kemdikbud.go.id/tka/tka/view/mata-pelajaran-pilihan/sma/matematika-tingkat-lanjut)
- PDF soal Matematika Wajib 2025 (29 halaman) yang disediakan pengguna, digunakan untuk pemetaan indikator. Kedua lampiran bernama Wajib dan Pilihan ternyata identik; PDF Pilihan yang berbeda tidak tersedia.
- Ringkasan rumus dan kunci matematika yang dibuat sebelumnya digunakan sebagai bahan awal, kemudian diperiksa kembali. PDF sumber tidak disertakan dalam repository.

Pemetaan halaman dan laporan cakupan tersedia di [COVERAGE.md](COVERAGE.md).

## Menjalankan secara lokal

Buka terminal di folder proyek lalu jalankan:

```bash
python -m http.server 8000
```

Buka `http://localhost:8000`. Gunakan server lokal karena pemuatan JSON melalui `fetch` biasanya dibatasi ketika `index.html` dibuka langsung dengan `file://`.

## GitHub Pages

Unggah seluruh isi folder proyek sehingga `index.html` berada pada root repository. Di **Settings → Pages**, pilih **Deploy from a branch**, branch utama, dan folder **/(root)**. Tunggu tautan situs ditampilkan. Semua jalur aset relatif dan tidak memerlukan backend.

## Pengujian

```bash
npm test
python tests/verify_math.py
```

Tes menggunakan Node.js bawaan dan Python standar tanpa instalasi dependensi. Tes otomatis memeriksa struktur soal, penilaian, pengacakan, dan sejumlah perhitungan, tetapi tidak menggantikan peninjauan manusia.

## Struktur

```text
index.html
css/style.css
js/app.js  js/quiz.js  js/scoring.js  js/storage.js  js/data.js  js/math.js
data/wajib.json  data/pilihan.json  data/mixed.json  data/topics.json
assets/favicon.svg
tests/quiz.test.js  tests/verify_math.py
COVERAGE.md  README.md  package.json
```

## Catatan

Bank soal didominasi soal dasar dan menengah, dengan beberapa soal menantang. Diagram matematika tersedia untuk segitiga, vektor, dan satu fungsi linear; visualisasi lainnya belum tersedia. Konten, strategi, dan tingkat kesulitan dapat dikembangkan lebih lanjut.
