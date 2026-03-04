from services.inventory_service import InventoryService


def test_add_item():

    inventory = InventoryService()

    inventory.add_item("Laptop", 5)

    assert len(inventory.items) == 1