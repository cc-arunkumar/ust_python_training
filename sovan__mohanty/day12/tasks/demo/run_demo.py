import sys
import os

DATA_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(DATA_DIR)

from ust_tools_micro.csv_utils import read_csv
from ust_tools_micro.validators import require_fields, to_int
from ust_tools_micro.inventory import Inventory
inventory_path = os.path.join(DATA_DIR,"data","inventory.csv")
orders_path = os.path.join(DATA_DIR,"data","orders.csv")
def main():
    inventory = Inventory.from_csv(inventory_path)
    orders = read_csv(orders_path)
    required = ["order_id", "item_id", "quantity"]

    for order in orders:
        if not require_fields(order, required):
            print(f"INVALID ORDER: {order}")
            continue

        try:
            qty = to_int(order["quantity"])
        except ValueError:
            print(f"INVALID QUANTITY: {order}")
            continue

        order_id = order["order_id"]
        item_id = order["item_id"]
        if inventory.allocate(item_id, qty):
            print(f"ALLOCATED: {order_id} -> {item_id} ({qty})")
        else:
            print(f"FAILED: {order_id} -> {item_id} ({qty})")

if __name__ == "__main__":
    main()
    
# Sample Execution
# ALLOCATED: O1 -> ITM1 (2)
# FAILED: O2 -> ITM1 (4)
# ALLOCATED: O3 -> ITM2 (1)
# FAILED: O4 -> ITM999 (1)