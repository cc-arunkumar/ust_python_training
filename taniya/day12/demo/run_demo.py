import sys
import os

# Add parent directory to Python path so ust_tools_micro package can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import helper modules from ust_tools_micro package
from ust_tools_micro.csv_utils import read_csv        # Function to read CSV files into list of dicts
from ust_tools_micro.inventory import Inventory       # Inventory class to manage stock
from ust_tools_micro.validators import to_integer     # Validator to safely convert values to integer

# -------------------------------
# Main function
# -------------------------------
def main():
    # Load inventory from CSV file
    inventory = Inventory.from_csv("data/inventory.csv")

    # Load orders from CSV file
    orders = read_csv("data/orders.csv")

    # Define required fields for each order
    required_fields = ["order_id", "item_id", "quantity"]

    # Process each order
    for order in orders:
        # Validate that all required fields are present
        if not all(field in order for field in required_fields):
            print(f"Invalid order: {order}")
            continue

        # Validate and convert quantity to integer
        try:
            quantity = to_integer(order["quantity"])
        except ValueError:
            print(f"Invalid quantity: {order}")
            continue

        # Extract order_id and item_id
        item_id = order["item_id"]
        order_id = order["order_id"]

        # Try to allocate item from inventory
        if inventory.allocate(item_id, quantity):
            # Allocation successful
            print(f"Allocated: {order_id} -> {item_id} ({quantity})")
        else:
            # Allocation failed (not enough stock or invalid item)
            print(f"Failed: {order_id} -> {item_id} ({quantity})")

# -------------------------------
# Entry point
# -------------------------------
if __name__ == "__main__":
    main()   # Run the main function