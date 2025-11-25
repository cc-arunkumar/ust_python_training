from ust_tools_micro.csv_utils import read_csv

# -------------------------------
# Inventory class: manages stock items
# -------------------------------
class Inventory:
    def __init__(self, items: dict[str, int]):
        """
        Initialize inventory with a dictionary of items.
        Args:
            items: dictionary mapping item_id -> available stock count
        """
        self.items = items

    @classmethod
    def from_csv(cls, path) -> "Inventory":
        """
        Load inventory from a CSV file.
        Args:
            path: path to CSV file containing inventory data
        Returns:
            Inventory object with items loaded
        """
        rows = read_csv(path)          # Read rows from CSV file
        items = {}
        for row in rows:
            item_id = row["item_id"]   # Extract item ID
            stock = int(row["available_stocks"])  # Convert stock count to integer
            items[item_id] = stock     # Store in dictionary
        return cls(items)              # Return Inventory instance

    def allocate(self, item_id: str, quantity: int) -> bool:
        """
        Allocate (reduce) stock for a given item if enough is available.
        Args:
            item_id: ID of the item to allocate
            quantity: number of units to allocate
        Returns:
            True if allocation successful, False otherwise
        """
        if item_id in self.items and self.items[item_id] >= quantity:
            self.items[item_id] -= quantity   # Reduce stock
            return True
        return False                          # Allocation failed

    def release(self, item_id: str, quantity: int) -> None:
        """
        Release (increase) stock for a given item.
        Args:
            item_id: ID of the item to release
            quantity: number of units to add back
        """
        if item_id in self.items:
            self.items[item_id] += quantity   # Increase stock