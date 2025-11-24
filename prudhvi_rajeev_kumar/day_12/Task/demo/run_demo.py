import os
import sys

# Setting the BASE_DIR to the parent directory of the current script
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# Import necessary utilities and classes
from ust_tools_micro.class_utils import read_csv
from ust_tools_micro.validators import to_int
from ust_tools_micro.inventory import Inventory

# Paths to the CSV files for inventory and orders data
inventory_path = os.path.join(BASE_DIR, "data", "inventory.csv")
orders_path = os.path.join(BASE_DIR, "data", "orders.csv")

# Function to validate if the order has required fields: order_id, item_id, and quantity.
def validate_order(order: dict[str, str]) -> bool:
    # List of required fields in an order
    required = ["order_id", "item_id", "quantity"]
    
    # Check if each required field is present and not empty
    for field in required:
        if field not in order or order[field].strip() == "":
            return False  # Return False if any field is missing or empty
    return True  # Return True if all required fields are present

# Function to execute the demo: allocate inventory based on orders
def run_demo():
    # Load the inventory data from CSV file
    inventory = Inventory.from_csv(inventory_path)

    # Read orders data from the orders CSV file
    orders = read_csv(orders_path)

    # Loop through all the orders and process them
    for order in orders:
        # Validate the current order
        if not validate_order(order):
            print(f"INVALID ORDER: {order}")  # Print invalid orders
            continue

        # Extract order details from the validated order
        order_id = order["order_id"]
        item_id = order["item_id"]
        qty = to_int(order["quantity"])  # Convert quantity to integer

        # If quantity is invalid (None), print the invalid order and continue
        if qty is None:
            print(f"INVALID ORDER: {order}")
            continue

        # Try to allocate the inventory for the given item and quantity
        if inventory.allocate(item_id, qty):
            # Print success message if allocation is successful
            print(f"ALLOCATED: {order_id} → {item_id} ({qty})")
        else:
            # Print failure message if allocation fails
            print(f"FAILED: {order_id} → {item_id} ({qty})")

# Entry point for running the script
if __name__ == "__main__":
    run_demo()

