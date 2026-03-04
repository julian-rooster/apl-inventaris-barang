# Aplikasi Inventaris Barang

Aplikasi Inventaris Barang adalah aplikasi sederhana berbasis Python yang digunakan untuk mencatat dan mengelola data barang dalam inventaris.  
Aplikasi ini dibuat sebagai tugas kelompok pada mata kuliah **Rancang Bangun Perangkat Lunak (RBPL)**.


## Fitur Aplikasi

Aplikasi ini memiliki beberapa fitur utama:

- Menambahkan barang ke inventaris
- Melihat daftar barang
- Menghapus barang dari inventaris


## Struktur Project

Struktur folder pada project ini adalah sebagai berikut:
apl-inventaris-barang
│
├── docs/ # Dokumentasi project
├── src/ # Source code aplikasi
│ ├── models/ # Model data
│ │ └── item.py
│ │
│ ├── services/ # Logic aplikasi
│ │ └── inventory_service.py
│ │
│ ├── utils/ # Helper dan validation
│ │ └── helper.py
│ │
│ └── main.py # CLI aplikasi
│
├── tests/ # Unit testing
│ └── test_inventory.py
│
├── requirements.txt
└── README.md


## Cara Menjalankan Aplikasi

1. Clone repository
git clone https://github.com/julian-rooster/apl-inventaris-barang.git

2. Masuk ke folder project
cd apl-inventaris-barang

3. Jalankan program
cd src
python main.py


## Contoh Tampilan Program
Menu utama aplikasi:
=== APLIKASI INVENTARIS BARANG ===
1.Tambah Barang
2.Lihat Barang
3.Hapus Barang
4.Keluar


## Pengujian Program

Pengujian dilakukan menggunakan unit test yang berada pada folder `tests`.

Untuk menjalankan test:
python tests/test_inventory.py


## Anggota Kelompok

- Julian – Setup project & testing
- Oki – Inventory Service
- Agna – Model Layer
- Hifzhan – Utility & Validation
- Rifan – CLI Interface