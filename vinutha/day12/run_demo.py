import os
import sys

# Ensure the parent folder (project root) is in Python's search path
base_dir = os.path.dirname(__file__)
sys.path.append(base_dir)

from ust_tools_micro import Inventory, read_csv, require_fields, to_int

def main():
    # Build paths to CSV files relative to project root
    inventory_path = os.path.join(base_dir, "data", "inventory.csv")
    orders_path = os.path.join(base_dir, "data", "orders.csv")

    # Load inventory and orders
    inventory = Inventory.from_csv(inventory_path)
    orders = read_csv(orders_path)

    required_fields = ["order_id", "item_id", "quantity"]

    for order in orders:
        if not require_fields(order, required_fields):
            print("INVALID ORDER:", order)
            continue

        order_id = order["order_id"]
        item_id = order["item_id"]

        try:
            qty = to_int(order["quantity"])
        except ValueError:
            print("INVALID QUANTITY:", order)
            continue

        if inventory.allocate(item_id, qty):
            print(f"ALLOCATED: {order_id} -> {item_id} ({qty})")
        else:
            print(f"FAILED: {order_id} -> {item_id} ({qty})")

if __name__ == "__main__":
    main()
