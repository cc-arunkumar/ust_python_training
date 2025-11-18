from ust_tools_micro import read_csv_file
from ust_tools_micro import Inventory
from ust_tools_micro import require_fields, to_int

# Read the orders CSV into a list of dictionaries
orders_list = read_csv_file("data/orders.csv")

# Required fields for each order row
fields_header = ["order_id", "item_id", "quantity"]

# Process each order in the CSV
for row in orders_list:
    try:
        # Validate that the row contains all required fields
        require_fields(row, fields_header)
        print("valid", row)
    except Exception as e:
        # If missing fields, skip this order
        print(f"Invalid Order req: {row} - {e}")
        continue

    # Extract values
    order_id = row["order_id"]
    item_id = row["item_id"]
    qty = row["quantity"]

    # Ensure item_id is not empty
    if not item_id:
        print(f"Invalid Order: {row}")
        continue

    # Convert quantity to an integer
    try:
        qty = to_int(qty)
    except Exception as e:
        print(f"Invalid Order: {row} - {e}")
        continue

    # Load inventory record for the given item
    inv = Inventory.from_csv(item_id, "data/inventory.csv")

    # If inventory record does not exist, fail this order
    if not inv:
        print(f"Item not found in inventory: {item_id}")
        continue

    # Attempt to allocate inventory for the requested quantity
    allocated = inv.allocate(qty)

    # Report allocation success or failure
    if allocated:
        print(f"ALLOCATED: {order_id} -> {item_id}")
    else:
        print(f"FAILED: {order_id} -> {item_id}")
