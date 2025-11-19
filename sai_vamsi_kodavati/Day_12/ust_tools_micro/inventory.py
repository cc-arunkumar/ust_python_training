# inventory.py

from .validators import require_fields, to_int
from .csv_utils import read_csv_file

class Inventory:
    def __init__(self, row):
        # Initialize an Inventory object from a CSV row.
        
        # Each row should contain an item ID
        self.item_id = row.get("item_id")

        # Support multiple possible column names for stock.
        stock_value = (
            row.get("available_stock")
            or row.get("stock")
            or row.get("qty")
            or row.get("quantity")
        )

        # If no recognized stock column is found, fail early
        if stock_value is None or stock_value.strip() == "":
            raise ValueError(f"No available stock for item {self.item_id}")

        # Convert stock value to an integer using provided validator
        self.available_stock = to_int(stock_value)

    @classmethod
    def from_csv(cls, item_id, path):
        
        # Load inventory for a specific item_id from a CSV file.
       
        rows = read_csv_file(path)

        # Search for a row with a matching item_id
        for row in rows:
            if row["item_id"] == item_id:
                return cls(row)

        # Item not found in CSV
        return None

    def allocate(self, qty):
        
        # Prevent invalid quantities like negative or zero
        if qty <= 0:
            return False

        # Check if there is enough available stock
        if self.available_stock < qty:
            return False

        # Perform the allocation
        self.available_stock -= qty
        return True

    def release(self, qty):
        
        # Only positive values are considered valid.
        
        if qty > 0:
            self.available_stock += qty
