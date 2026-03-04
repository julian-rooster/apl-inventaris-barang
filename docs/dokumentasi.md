# Dokumentasi Aplikasi Inventaris Barang

## Deskripsi Aplikasi

Aplikasi Inventaris Barang adalah aplikasi sederhana berbasis Python yang digunakan untuk mengelola data barang dalam inventaris.
Aplikasi ini dibuat sebagai tugas kelompok pada mata kuliah Rancang Bangun Perangkat Lunak (RBPL).

## Fitur Aplikasi

Aplikasi ini memiliki beberapa fitur utama:

* Menambahkan barang ke dalam inventaris
* Melihat daftar barang yang tersimpan
* Menghapus barang dari inventaris

## Struktur Sistem

Aplikasi ini menggunakan struktur modular dengan pembagian sebagai berikut:

* **models**
  Berisi model data yang merepresentasikan barang dalam inventaris.

* **services**
  Berisi logika utama aplikasi untuk mengelola data inventaris.

* **utils**
  Berisi fungsi helper dan validasi data.

* **CLI (main.py)**
  Berfungsi sebagai antarmuka pengguna berbasis terminal.

## Cara Menjalankan Aplikasi

1. Masuk ke folder project
2. Jalankan perintah berikut

```
cd src
python main.py
```

## Cara Menggunakan Program

1. Pilih menu **Tambah Barang** untuk menambahkan barang baru.
2. Pilih menu **Lihat Barang** untuk melihat daftar barang yang tersimpan.
3. Pilih menu **Hapus Barang** untuk menghapus barang dari inventaris.
4. Pilih menu **Keluar** untuk menutup program.