from services.inventory_service import InventoryService


def main():

    inventory = InventoryService()

    while True:
        print("\n=== APLIKASI INVENTARIS BARANG ===")
        print("1. Tambah Barang")
        print("2. Lihat Barang")
        print("3. Hapus Barang")
        print("4. Keluar")

        choice = input("Pilih menu: ")

        # ToDo: implement menu logic
        if choice == "1":
            nama = input("Nama barang: ")

            try:
                jumlah = int(input("Jumlah stok: "))
            except ValueError:
                print("Jumlah stok harus berupa angka.")
                continue

            inventory.add_item(nama, jumlah)
            print("Barang berhasil ditambahkan.")

        elif choice == "2":
            items = inventory.get_all_items()

            if not items:
                print("Belum ada barang di inventaris.")
            else:
                print("\n=== DAFTAR BARANG ===")
                for item in items:
                    print(item.display())

        elif choice == "3":
            nama = input("Masukkan nama barang yang ingin dihapus: ")
            inventory.remove_item(nama)
            print("Barang berhasil dihapus (jika ada).")

        elif choice == "4":
            print("Keluar dari program...")
            break

        else:
            print("Pilihan tidak valid.")
            

if __name__ == "__main__":
    main()