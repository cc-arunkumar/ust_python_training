from .csv_utils import read_csv
from .validators import to_int

class Inventory:
    def __init__(self, items):
        self.items = items

    @classmethod
    def from_csv(cls, path):
        rows = read_csv(path)
        items = {}
        for row in rows:
            item_id = row["item_id"]
            stock = to_int(row["available_stock"])
            items[item_id] = stock
        return cls(items)

    def allocate(self, item_id, qty):
        if item_id in self.items and self.items[item_id] >= qty:
            self.items[item_id] -= qty
            return True
        return False

    def release(self, item_id, qty):
        if item_id in self.items:
            self.items[item_id] += qty
