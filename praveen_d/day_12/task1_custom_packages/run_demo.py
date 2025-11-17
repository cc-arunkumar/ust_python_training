import os

from ust_tools_micro import (
    Inventory,
    read_csv,
    require_fields,
    to_int,
)


def main() -> None:
    # Base directory = folder where run_demo.py is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    data_dir = os.path.join(base_dir, "data")
    inventory_path = os.path.join(data_dir, "inventory.csv")
    orders_path = os.path.join(data_dir, "orders.csv")

    # Debug paths (optional)
    print("Inventory Path:", inventory_path)
    print("Orders Path   :", orders_path)

    # Load inventory
    inventory = Inventory.from_csv(inventory_path)

    # Load orders
    orders = read_csv(orders_path)

    required = ["order_id", "item_id", "quantity"]

    #  Validate, convert quantity, allocate
    for order in orders:
        if not require_fields(order, required):
            print(f"INVALID ORDER: {order}")
            continue

        order_id = order["order_id"].strip()
        item_id = order["item_id"].strip()
        qty_str = order["quantity"].strip()

        try:
            qty = to_int(qty_str)
        except ValueError:
            print(f"INVALID ORDER (bad quantity): {order}")
            continue

        success = inventory.allocate(item_id, qty)

        if success:
            print(f"ALLOCATED: {order_id} -> {item_id} ({qty})")
        else:
            print(f"FAILED: {order_id} -> {item_id} ({qty})")


if __name__ == "__main__":
    main()
