class Item:
    """
    Model representasi barang dalam inventaris
    """

    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def display(self):
        """
        Mengembalikan string informasi barang
        """
        # ToDo: tampilkan format "Nama - Jumlah"
        return f"{self.name} - {self.quantity}"