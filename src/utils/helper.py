def validate_name(name):
    """
    Validasi nama barang
    """
    # ToDo: return True jika string tidak kosong
    return isinstance(name, str) and name.strip() != ""


def validate_quantity(quantity):
    """
    Validasi jumlah barang
    """
    # ToDo: return True jika integer >= 0
    return isinstance(quantity, int) and quantity >= 0