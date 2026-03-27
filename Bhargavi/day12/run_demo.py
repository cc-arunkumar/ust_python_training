# run_demo.py

import os
import sys

# Add package path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)

from ust_tools_micro import (
    read_csv,
    require_fields,
    to_int,
    Inventory
)

DATA_DIR = os.path.join(BASE_DIR, "data")
inventory_file = os.path.join(DATA_DIR, "inventory.csv")
orders_file = os.path.join(DATA_DIR, "orders.csv")

def main():
    # Load inventory
    inventory = Inventory.from_csv(inventory_file)

    # Load orders
    orders = read_csv(orders_file)

    required = ["order_id", "item_id", "quantity"]

    for order in orders:
        # Validate required fields
        if not require_fields(order, required):
            print("INVALID ORDER:", order)
            continue

        order_id = order["order_id"]
        item_id = order["item_id"]

        try:
            qty = to_int(order["quantity"])
        except ValueError:
            print("INVALID QUANTITY:", order)
            continue

        # Try allocating
        if inventory.allocate(item_id, qty):
            print(f"ALLOCATED: {order_id} -> {item_id} ({qty})")
        else:
            print(f"FAILED: {order_id} -> {item_id} ({qty})")

if __name__ == "__main__":
    main()


# output
# ALLOCATED: O1 -> ITM1 (2)
# FAILED: O2 -> ITM1 (4)   
# ALLOCATED: O3 -> ITM2 (1)
# FAILED: O4 -> ITM999 (1) 