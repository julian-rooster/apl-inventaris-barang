import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from services.inventory_service import InventoryService


def test_add_item():
    service = InventoryService()
    service.add_item("Laptop", 5)

    items = service.get_all_items()

    assert len(items) == 1


def test_remove_item():
    service = InventoryService()

    service.add_item("Mouse", 2)

    service.remove_item("Mouse")

    items = service.get_all_items()

    assert len(items) == 0


def test_get_items():
    service = InventoryService()

    service.add_item("Keyboard", 3)

    items = service.get_all_items()

    assert items[0].name == "Keyboard"