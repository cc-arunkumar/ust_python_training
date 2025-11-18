# Always assume this file is inside Day12 folder

import os
from ust_tools_micro.csv_utils import read_csv
from ust_tools_micro.validators import require_fields, to_int
from ust_tools_micro.inventory import Inventory

def main():
    # This folder (where run_demo.py exists)
    base_folder = os.path.dirname(__file__)

    # data folder inside Day12
    data_folder = os.path.join(base_folder, "data")

    inventory_path = os.path.join(data_folder, "inventory.csv")
    orders_path = os.path.join(data_folder, "orders.csv")

    required = ["order_id", "item_id", "quantity"]

    inv = Inventory.from_csv(inventory_path)
    orders = read_csv(orders_path)

    for row in orders:
        if not require_fields(row, required):
            print("INVALID ORDER:", row)
            continue

        order_id = row["order_id"].strip()
        item_id = row["item_id"].strip()
        qty_str = row["quantity"].strip()

        try:
            qty = to_int(qty_str)
        except ValueError:
            print("INVALID ORDER:", row)
            continue

        if inv.allocate(item_id, qty):
            print(f"ALLOCATED: {order_id} -> {item_id} ({qty})")
        else:
            print(f"FAILED: {order_id} -> {item_id} ({qty})")

if __name__ == "__main__":
    main()
