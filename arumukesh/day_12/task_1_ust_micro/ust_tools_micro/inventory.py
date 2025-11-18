from csv import DictReader

class Inventory:
    def __init__(self, items: dict[str, int]):
        # items = { item_id: available_stock }
        self.items = items

    @classmethod
    def from_csv(cls, path: str):
        """
        Load inventory from CSV with fields: item_id, available_stock
        """
        items = {}

        with open(path, "r") as file:
            reader = DictReader(file)
            for row in reader:
                items[row["item_id"]] = int(row["available_stock"])

        return cls(items)

    def allocate(self, item_id: str, qty: int) -> bool:
        """
        If enough stock exists, subtract and return True.
        Otherwise return False.
        """
        if item_id in self.items and self.items[item_id] >= qty:
            self.items[item_id] -= qty
            return True
        return False

    def release(self, item_id: str, qty: int) -> None:
        """
        Add qty back only if item exists.
        """
        if item_id in self.items:
            self.items[item_id] += qty
