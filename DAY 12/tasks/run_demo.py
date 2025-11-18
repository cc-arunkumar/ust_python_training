from ust_tools_micro.csv_utils import read_csv
from ust_tools_micro.inventory import Inventory
from ust_tools_micro.validators import required_fields, to_int

def main():
    # Load inventory from CSV
    inventory = Inventory.from_csv("DAY 12\\tasks\\data\\inventory.csv")
    # Load orders from CSV
    orders = read_csv("DAY 12\\tasks\\data\\orders.csv")

    # Process each order
    for row in orders:
        # Validate required fields
        if not required_fields(row, ["order_id", "item_id", "quantity"]):
            print("INVALID ORDER:", row)
            continue

        # Convert quantity to integer
        try:
            qty = to_int(row["quantity"])
        except ValueError:
            print("INVALID ORDER (BAD QUANTITY):", row)
            continue

        item = row["item_id"]
        order_id = row["order_id"]

        # Attempt to allocate stock
        if inventory.allocate(item, qty):
            print(f"ALLOCATED: {order_id} -> {item} ({qty})")
        else:
            print(f"FAILED: {order_id} -> {item} ({qty})")

if __name__ == "__main__":
    main()

"""
SAMPLE OUTPUT

ALLOCATED: O1 -> ITM1 (2)
FAILED: O2 -> ITM1 (4)
ALLOCATED: O3 -> ITM2 (1)
FAILED: O4 -> ITM999 (1)
"""
