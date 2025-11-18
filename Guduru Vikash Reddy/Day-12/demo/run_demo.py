import os
import sys

# -------------------------------------------------------
# Add the project root folder to Python's module search path.
# This ensures Python can find ust_tools_micro even if this
# script is inside another folder.
# -------------------------------------------------------
base_dir = os.path.dirname(__file__)
sys.path.append(base_dir)

from ust_tools_micro import Inventory, read_csv, require_fields, to_int

def main():
    # -------------------------------------------------------
    # Build paths to inventory.csv and orders.csv
    # These files are located inside the "data" folder.
    # -------------------------------------------------------
    inventory_path = os.path.join(base_dir, "data", "inventory.csv")
    orders_path = os.path.join(base_dir, "data", "orders.csv")

    # -------------------------------------------------------
    # Load CSV data:
    # Inventory is loaded using the custom Inventory class.
    # Orders are loaded as a list of dictionaries.
    # -------------------------------------------------------
    inventory = Inventory.from_csv(inventory_path)
    orders = read_csv(orders_path)

    # Fields that every order must contain
    required_fields = ["order_id", "item_id", "quantity"]

    # -------------------------------------------------------
    # Process each order one by one
    # -------------------------------------------------------
    for order in orders:

        # Check if required fields are present
        if not require_fields(order, required_fields):
            print("INVALID ORDER:", order)
            continue   # Skip to next order

        # Extract basic values
        order_id = order["order_id"]
        item_id = order["item_id"]

        # -------------------------------------------------------
        # Convert quantity into an integer.
        # If it fails (ex: "ten"), it is considered invalid.
        # -------------------------------------------------------
        try:
            qty = to_int(order["quantity"])
        except ValueError:
            print("INVALID QUANTITY:", order)
            continue

        # -------------------------------------------------------
        # Try allocating the requested quantity from inventory.
        # allocate() returns True if inventory is available,
        # otherwise False.
        # -------------------------------------------------------
        if inventory.allocate(item_id, qty):
            print(f"ALLOCATED: {order_id} -> {item_id} ({qty})")
        else:
            print(f"FAILED: {order_id} -> {item_id} ({qty})")

# Entry point of the script
if __name__ == "__main__":
    main()