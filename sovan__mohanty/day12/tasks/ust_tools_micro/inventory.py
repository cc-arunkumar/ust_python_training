
from typing import Dict
from .csv_utils import read_csv
from .validators import to_int

class Inventory:
    def __init__(self, items: Dict[str, int]):
        self.items = items
    @classmethod
    def from_csv(cls, path: str) -> "Inventory":
        rows = read_csv(path)
        items = {}
        for row in rows:
            item_id = row.get("item_id")
            stock_str = row.get("available_stock", "0")
            try:
                items[item_id] = to_int(stock_str)
            except ValueError:
                items[item_id] = 0
        return cls(items)

    def allocate(self, item_id: str, qty: int) -> bool:
        
        if item_id in self.items and self.items[item_id] >= qty:
            self.items[item_id] -= qty
            return True
        return False

    def release(self, item_id: str, qty: int) -> None:
        if item_id in self.items:
            self.items[item_id] += qty

        