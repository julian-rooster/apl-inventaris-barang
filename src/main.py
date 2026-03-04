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


if __name__ == "__main__":
    main()