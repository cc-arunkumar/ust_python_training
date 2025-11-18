from .csv_utils import csv_reader

# Inventory class to manage items and stock
class Inventory:
    # Constructor to initialize the inventory with a dictionary of items and their available stock
    def __init__(self, items):
        self.items = items  
        
    # Class method to create an Inventory instance from a CSV file
    @classmethod
    def from_csv(cls, path):
        # Read data from the provided CSV file using csv_reader function
        rows = csv_reader(path)
        
        items = {} 
        
        # Loop through each row in the CSV data and extract item_id and available stock
        for row in rows:
            item_id = row["item_id"]  
            stock = int(row["available_stock"])  
            items[item_id] = stock  
        
        # Return an instance of Inventory initialized with the items dictionary
        return cls(items)

    # Method to allocate stock of a specific item if enough stock is available
    def allocate(self, item_id, qty):
        # Check if the item_id exists in the inventory
        if item_id not in self.items:
            return False  
        
        # Check if the available stock is less than the requested quantity
        if self.items[item_id] < qty:
            return False  
        
        # Subtract the allocated quantity from the available stock
        self.items[item_id] -= qty
        return True  

    # Method to release stock of a specific item (increase available stock)
    def release(self, item_id, qty):
        # Check if the item_id exists in the inventory
        if item_id in self.items:
            # Add the released quantity to the available stock of the item
            self.items[item_id] += qty

