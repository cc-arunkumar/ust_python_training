from .csv_utils import read_csv

class Inventory:
    def __init__(self, items):
        self.items = items

    @classmethod
    def from_csv(cls, path):
        rows = read_csv(path)
        items = {}
        for r in rows:
            item_id = r["item_id"]                # example: "ITM1"
            stock_str = r["available_stock"]      # example: "5"
            stock = int(stock_str)                # convert string to integer

            items[item_id] = stock
        return cls(items)

    def allocate(self, item_id, qty):

        if item_id not in self.items:
            return False


        if self.items[item_id] >= qty:

            self.items[item_id] -= qty
            return True

        return False

    def release(self, item_id, qty):

        if item_id in self.items:
            self.items[item_id] += qty
