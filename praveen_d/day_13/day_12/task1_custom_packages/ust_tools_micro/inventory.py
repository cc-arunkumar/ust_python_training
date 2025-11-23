from typing import Dict
from .csv_utils import read_csv
from .validators import to_int


class Inventory:
    def __init__(self, items: Dict[str, int]) -> None:
        # items maps item_id -> available_stock
        self.items: Dict[str, int] = dict(items)

    @classmethod
    def from_csv(cls, path: str) -> "Inventory":
        rows = read_csv(path)
        items: Dict[str, int] = {}

        for row in rows:
            item_id = row.get("item_id", "").strip()
            stock_str = row.get("available_stock", "").strip()

            if not item_id:
                continue

            try:
                stock = to_int(stock_str)
            except ValueError:
                # Skip invalid stock rows
                continue

            items[item_id] = stock

        return cls(items)

    def allocate(self, item_id: str, qty: int) -> bool:
        """
        If item exists and enough stock:
        - subtract qty
        - return True
        Otherwise return False.
        """
        if qty <= 0:
            return False

        current = self.items.get(item_id)
        if current is None:
            return False

        if current >= qty:
            self.items[item_id] = current - qty
            return True
        else:
            return False

    def release(self, item_id: str, qty: int) -> None:
        """
        Add qty back into stock (only if item_id exists).
        """
        if qty <= 0:
            return
        if item_id in self.items:
            self.items[item_id] += qty
