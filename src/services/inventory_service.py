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
        item = Item(name, quantity)
        self.items.append(item)

    def remove_item(self, name):
        """
        Menghapus barang berdasarkan nama
        """
        # ToDo: hapus item dari list
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                break

    def get_all_items(self):
        """
        Mengambil semua barang
        """
        # ToDo: return list items
        return self.items