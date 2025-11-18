from ust_tools_micro.class_utils import read_csv

class Inventory:
    def __init__(self, items: dict[str, int]):
        self.items = items

    @classmethod
    def from_csv(cls, path: str) -> "Inventory":
        rows = read_csv(path)
        items = {}
        for row in rows:
            item_id = row.get("item_id")
            stock_str = row.get("available_stock", "0")
            try:
                stock = int(stock_str)
            except ValueError:
                stock = 0
            if item_id:
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
