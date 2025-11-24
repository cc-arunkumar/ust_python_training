import csv
import os
from typing import Dict

class Inventory:
    # Initialize the inventory with a dictionary of items and their available stock
    def __init__(self, items: Dict[str, int]):
        self.items = items

    # Class method to create an Inventory object from a CSV file
    @classmethod
    def from_csv(cls, path: str) -> 'Inventory':
        cls.create_sample_data()  # Create sample data if necessary
        items = {}  # Initialize an empty dictionary to store items
        with open(path, mode='r', newline='') as file:
            reader = csv.DictReader(file)  # Read the CSV file
            for row in reader:
                # For each row, store the item_id and its available stock in the items dictionary
                items[row['item_id']] = int(row['available_stock'])
        return cls(items)  # Return an instance of Inventory initialized with the items dictionary

    # Class method to create sample data and save it into CSV files
    @classmethod
    def create_sample_data(cls):
        data_dir = 'data'  # Directory where the data files will be stored
        inventory_file = os.path.join(data_dir, 'inventory.csv')
        orders_file = os.path.join(data_dir, 'orders.csv')

        # Create the 'data' directory if it doesn't exist
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        # Sample data for the inventory
        inventory_data = [
            {"item_id": "ITM1", "available_stock": "5"},
            {"item_id": "ITM2", "available_stock": "2"}
        ]

        # Sample data for orders
        orders_data = [
            {"order_id": "O1", "item_id": "ITM1", "quantity": "2"},
            {"order_id": "O2", "item_id": "ITM1", "quantity": "4"},
            {"order_id": "O3", "item_id": "ITM2", "quantity": "1"},
            {"order_id": "O4", "item_id": "ITM999", "quantity": "1"}  # Invalid item_id
        ]

        # Create the inventory file if it doesn't exist
        if not os.path.exists(inventory_file):
            with open(inventory_file, mode='w', newline='') as file:
                fieldnames = ['item_id', 'available_stock']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()  # Write the header row
                writer.writerows(inventory_data)  # Write the inventory data
            print(f"Created {inventory_file}")

        # Create the orders file if it doesn't exist
        if not os.path.exists(orders_file):
            with open(orders_file, mode='w', newline='') as file:
                fieldnames = ['order_id', 'item_id', 'quantity']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()  # Write the header row
                writer.writerows(orders_data)  # Write the orders data
            print(f"Created {orders_file}")

    # Method to allocate items from the inventory (decreases available stock)
    def allocate(self, item_id: str, qty: int) -> bool:
        if item_id in self.items and self.items[item_id] >= qty:
            self.items[item_id] -= qty  # Decrease the available stock
            return True  # Allocation successful
        return False  # Allocation failed if item is not available or stock is insufficient

    # Method to release items back to the inventory (increases available stock)
    def release(self, item_id: str, qty: int) -> None:
        if item_id in self.items:
            self.items[item_id] += qty  # Increase the available stock


# output


# Created data/inventory.csv
# Created data/orders.csv

# item_id,available_stock
# ITM1,5
# ITM2,2

# order_id,item_id,quantity
# O1,ITM1,2
# O2,ITM1,4
# O3,ITM2,1
# O4,ITM999,1
