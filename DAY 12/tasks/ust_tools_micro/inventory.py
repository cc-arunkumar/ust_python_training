from .validators import to_int
from .csv_utils import read_csv

class Inventory:

    # Initialize inventory with items dict: {item_id: stock}
    def __init__(self, items):
        self.items = items

    # Create Inventory instance from CSV file
    @classmethod
    def from_csv(cls, path):
        rows = read_csv(path)
        items = {}
        for row in rows:
            item_id = row.get("item_id")
            stock = to_int(row.get("available_stock"))  # Convert stock to int
            items[item_id] = stock
        return cls(items)

    # Allocate stock for an item if available
    def allocate(self, item_id, quantity):
        if item_id in self.items and self.items[item_id] >= quantity:
            self.items[item_id] -= quantity  # Reduce stock
            return True
        return False

    # Release stock back to inventory
    def release(self, item_id, quantity):
        if item_id in self.items:
            self.items[item_id] += quantity