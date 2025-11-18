from .csv_utils import read_csv
from .validators import to_int

class Inventory:
    def __init__(self, items):
        # Store inventory as a dictionary: {item_id: stock_count}
        self.items = items

    @classmethod
    def from_csv(cls, path):
        # Read all rows from inventory CSV
        rows = read_csv(path)

        # Convert CSV rows into a dictionary of item_id → stock
        items = {}
        for row in rows:
            item_id = row["item_id"]                      # Extract item ID
            stock = to_int(row["available_stock"])        # Convert stock to integer
            items[item_id] = stock                        # Store in dictionary

        # Return an Inventory object
        return cls(items)

    def allocate(self, item_id, qty):
        # Check if item exists and stock is sufficient
        if item_id in self.items and self.items[item_id] >= qty:
            self.items[item_id] -= qty    # Reduce stock
            return True                   # Allocation successful

        # Allocation failed (item missing or not enough stock)
        return False

    def release(self, item_id, qty):
        # Add quantity back into inventory if item exists
        if item_id in self.items:
            self.items[item_id] += qty
