
import os
from ust_tools_micro import read_csv, require_fields, to_int, Inventory

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
orders_path = os.path.join(BASE_DIR, "data", "orders.csv")
inventory_path = os.path.join(BASE_DIR, "data", "inventory.csv")

def main():
    # Load inventory
    inventory = Inventory.from_csv(inventory_path)

    # Load orders
    orders = read_csv(orders_path)

    for order in orders:
        if not require_fields(order, ["order_id", "item_id", "quantity"]):
            print(f"Invalid order: {order}")
            continue

        try:
            qty = to_int(order["quantity"])
        except ValueError:
            print(f"Invalid quantity: {order}")
            continue

        order_id = order["order_id"]
        item_id = order["item_id"]

        if inventory.allocate(item_id, qty):
            print(f"Allocated: {order_id} → {item_id} ({qty})")
        else:
            print(f"Failed: {order_id} → {item_id} ({qty})")

if __name__ == "__main__":
    main()
