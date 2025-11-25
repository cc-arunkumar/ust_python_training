import csv
from typing import Dict

# Inventory class to manage stock items
class Inventory:
    def __init__(self, items: Dict[str, int]):
        # items is a dictionary mapping item_id → available stock
        self.items = items

    @classmethod
    def from_csv(cls, path: str) -> "Inventory":
        # Class method to load inventory from a CSV file
        items: Dict[str, int] = {}
        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)   # Read CSV rows into dictionaries
            for row in reader:
                item_id = row.get("item_id")   # Extract item_id column
                stock_str = row.get("available_stock", "0")   # Extract stock column
                print(item_id, stock_str)   # Debug print each row
                try:
                    stock = int(stock_str)   # Convert stock to integer
                except ValueError:
                    stock = 0   # Default to 0 if invalid
                if item_id:   # Only add if item_id is not empty
                    items[item_id] = stock
        return cls(items)   # Return Inventory object with loaded items

    def allocate(self, item_id: str, qty: int) -> bool:
        # Allocate stock (reduce quantity if available)
        if item_id in self.items and self.items[item_id] >= qty:
            self.items[item_id] -= qty
            return True   # Allocation successful
        return False      # Allocation failed (not enough stock or item missing)

    def release(self, item_id: str, qty: int) -> None:
        # Release stock (increase quantity back)
        if item_id in self.items:
            self.items[item_id] += qty


# Demo usage
if __name__ == "__main__":
    # Load inventory from CSV file
    inv = Inventory.from_csv(r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day12\data\inventory.csv")

    print("Initial stock:", inv.items)

    # Try allocating 2 units of item_1
    success = inv.allocate("item_1", 2)
    print("success:", success)
    print("after allocation:", inv.items)

    # Release 1 unit of item_1 back into stock
    inv.release("item_1", 1)
    print("Stock after release:", inv.items)

# ==============sample output================


# item_1 5
# Initial stock: {'item_1': 5}
# success: True
# after allocation: {'item_1': 3}
# Stock after release: {'item_1': 4}
