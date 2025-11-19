import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ust_tools_micro.csv_utils import read_csv
from ust_tools_micro.inventory import Inventory
from ust_tools_micro.validators import to_integer

def main():
    inventory = Inventory.from_csv("data/inventory.csv")
    orders = read_csv("data/orders.csv")
    required_fields = ["order_id", "item_id", "quantity"]

    for order in orders:
        if not all(field in order for field in required_fields):
            print(f"Invalid order: {order}")
            continue
        try:
            quantity = to_integer(order["quantity"])
        except ValueError:
            print(f"Invalid quantity: {order}")
            continue

        item_id = order["item_id"]
        order_id = order["order_id"]

        if inventory.allocate(item_id, quantity):
            print(f"Allocated: {order_id} -> {item_id} ({quantity})")
        else:
            print(f"Failed: {order_id} -> {item_id} ({quantity})")

if __name__ == "__main__":
    main()