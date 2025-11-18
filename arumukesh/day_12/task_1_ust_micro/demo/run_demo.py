from ust_tools_micro.csv_utils import read_csv
from ust_tools_micro.validators import require_fields, to_int
from ust_tools_micro.inventory import Inventory

# Paths
INV_FILE = "../data/inventory.csv"
ORD_FILE = "../data/orders.csv"


def main():
    # Load inventory
    inventory = Inventory.from_csv(INV_FILE)

    # Load orders
    orders = read_csv(ORD_FILE)

    required = ["order_id", "item_id", "quantity"]

    for order in orders:

        # 1. Validate required fields
        if not require_fields(order, required):
            print("INVALID ORDER:", order)
            continue

        # 2. Convert quantity to int
        try:
            qty = to_int(order["quantity"])
        except ValueError:
            print("INVALID QUANTITY:", order)
            continue

        # 3. Attempt allocation
        order_id = order["order_id"]
        item_id = order["item_id"]

        if inventory.allocate(item_id, qty):
            print(f"ALLOCATED: {order_id} -> {item_id} ({qty})")
        else:
            print(f"FAILED: {order_id} -> {item_id} ({qty})")


if __name__ == "__main__":
    main()
