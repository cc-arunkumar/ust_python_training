import os
import sys
base_dir=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)
from ust_tools_micro.csv_utils import read_csv
from ust_tools_micro.validators import require_fields, to_int
from ust_tools_micro.inventory import Inventory

def main():
    inventory_path = r"C:/Users/Administrator/Desktop/sunku_sai_yaswanth/day12/data/inventory.csv"
    orders_path = r"C:/Users/Administrator/Desktop/sunku_sai_yaswanth/day12/data/orders.csv"

    invent = Inventory.from_csv(inventory_path)
    orders = read_csv(orders_path)
    required = ["order_id", "item_id", "quantity"]


    for row in orders:
        if not require_fields(row, required):
            print(f"Invalid order: Missing required fields in {row}")
            continue
        
        try:
            qty = to_int(row["quantity"])
        except ValueError:
            print(f"Invalid order: Quantity is not a valid integer in {row}")
            continue

        order_id = row["order_id"]
        item_id = row["item_id"]

        if invent.allocate(item_id, qty):
            print(f"Allocated: {order_id} -> {item_id} ({qty})")
        else:
            print(f"Failed: {order_id} -> {item_id} ({qty})")

if __name__ == "__main__":
    main()
