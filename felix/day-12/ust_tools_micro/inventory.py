import csv
from typing import Dict, Optional

class Inventory:
    """
    Inventory class to manage stock items.
    
    Attributes:
        items (Dict[str, any]): Dictionary representing an inventory item.
    """
    
    def __init__(self, items: Dict[str, any]):
        """
        Initialize Inventory with a single item.

        Args:
            items (Dict[str, any]): Inventory item data.
        """
        self.items = items

    @classmethod
    def from_csv(cls, path: str, item_id: str) -> Optional["Inventory"]:
        """
        Create an Inventory instance from a CSV file by matching item_id.

        Args:
            path (str): Path to the CSV file containing inventory data.
            item_id (str): The item_id to search for.

        Returns:
            Inventory: New Inventory instance if item is found.
            None: If item_id not found in CSV.
        """
        with open(path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for item in reader:
                if item["item_id"] == item_id:
                    return cls(item)
        return None

    def allocate(self, qty: int) -> bool:
        """
        Allocate stock for an order.

        Args:
            qty (int): Quantity to allocate.

        Returns:
            bool: True if allocation was successful (stock updated),
                  False if insufficient stock.
        """
        available_stock = int(self.items.get("available_stock", 0))
        if available_stock >= qty:
            # Subtract allocated quantity from stock
            self.items["available_stock"] = available_stock - qty
            return True
        else:
            return False
