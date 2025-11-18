from ust_tools_micro.csv_utils import read_csv

class Inventory:
    def __init__(self, items: dict[str, int]):
        self.items = items

    @classmethod
    def from_csv(cls, path: str):
        rows = read_csv(path)
        items = {}
        for row in rows:
            item_id = row["item_id"]
            stock = int(row["available_stock"])
            items[item_id] = stock
        return cls(items)

    def allocate(self, item_id: str, qty: int) -> bool:
        if item_id in self.items and self.items[item_id] >= qty:
            self.items[item_id] -= qty
            return True
        return False

    def release(self, item_id: str, qty: int) -> None:
        if item_id in self.items:
            self.items[item_id] += qty
