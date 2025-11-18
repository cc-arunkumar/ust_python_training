import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from ust_tools_micro.class_utils import read_csv
from ust_tools_micro.validators import to_int
from ust_tools_micro.inventory import Inventory

inventory_path = os.path.join(BASE_DIR, "data", "inventory.csv")
orders_path = os.path.join(BASE_DIR, "data", "orders.csv")

def validate_order(order: dict[str, str]) -> bool:
    required = ["order_id", "item_id", "quantity"]
    for field in required:
        if field not in order or order[field].strip() == "":
            return False
    return True

def run_demo():
   
    inventory = Inventory.from_csv(inventory_path)
    orders = read_csv(orders_path)
    for order in orders:
        if not validate_order(order):
            print(f"INVALID ORDER: {order}")
            continue

        order_id = order["order_id"]
        item_id = order["item_id"]
        qty = to_int(order["quantity"])

        if qty is None:
            print(f"INVALID ORDER: {order}")
            continue

        if inventory.allocate(item_id, qty):
            print(f"ALLOCATED: {order_id} → {item_id} ({qty})")
        else:
            print(f"FAILED: {order_id} → {item_id} ({qty})")

if __name__ == "__main__":
    run_demo()

#Sample Output:
# ALLOCATED: O1 → ITM1 (2)
# FAILED: O2 → ITM1 (4)
# ALLOCATED: O3 → ITM2 (1)
# FAILED: O4 → ITM999 (1)