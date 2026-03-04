from models.item import Item


class InventoryService:
    """
    Service untuk mengelola inventaris barang
    """

    def __init__(self):
        self.items = []

    def add_item(self, name, quantity):
        """
        Menambahkan barang ke inventaris
        """
        # ToDo: buat object Item lalu masukkan ke list
        pass

    def remove_item(self, name):
        """
        Menghapus barang berdasarkan nama
        """
        # ToDo: hapus item dari list
        pass

    def get_all_items(self):
        """
        Mengambil semua barang
        """
        # ToDo: return list items
        pass