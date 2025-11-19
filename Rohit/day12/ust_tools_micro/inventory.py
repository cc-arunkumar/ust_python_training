import csv
from typing import Dict

class Inventory:
    def __init__(self, items: Dict[str, int]):
        self.items = items

    @classmethod
    def from_csv(cls, path: str) -> "Inventory":
    
        items: Dict[str, int] = {}
        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                
                item_id = row.get("item_id")
                stock_str = row.get("available_stock", "0")
                print(item_id, stock_str)
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

if __name__ == "__main__":

    inv = Inventory.from_csv(r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day12\data\inventory.csv")

    print("Initial stock:", inv.items)

    success = inv.allocate("item_1", 2)
    print("success:", success)
    print("after allocation:", inv.items)

    
    
    inv.release("item_1", 1)
    print("Stock after release:", inv.items)