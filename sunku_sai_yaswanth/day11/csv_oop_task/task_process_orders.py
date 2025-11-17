import csv

# Custom exceptions
class InvalidQuantityError(Exception):
    pass
class InvalidPriceError(Exception):
    pass
class InvalidStateError(Exception):
    pass
class MissingCustomerNameError(Exception):
    pass
valid_states = [
    'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa',
    'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala',
    'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',
    'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
    'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Andaman and Nicobar Islands',
    'Chandigarh']
required_fields = ['order_id', 'customer_name', 'state', 'product',
    'quantity', 'price_per_unit', 'status']
def missing_fields_check(order):
    missing = []
    for field in required_fields:
        value = order.get(field, "").strip() if order.get(field) else ""
        if value == "":
            missing.append(field)
    return missing
def validate_order(order):
    missing = missing_fields_check(order)
    if missing:
        return False, f"Missing fields: {', '.join(missing)}"
    try:
        try:
            quantity = int(order['quantity'])
            if quantity <= 0:
                raise InvalidQuantityError("Quantity must be positive.")
        except:
            raise InvalidQuantityError("Invalid quantity value.")
        try:
            price = float(order['price_per_unit'])
            if price == "":
                raise InvalidPriceError("Price cannot be blank.")
            if price < 0:
                price = abs(price)
        except:
            raise InvalidPriceError("Invalid price value.")
        if order['state'] not in valid_states:
            raise InvalidStateError("Invalid state name.")

        total = quantity * price
        status = order['status'].upper()

        order['quantity'] = quantity
        order['price_per_unit'] = price
        order['total_amount'] = total
        order['status'] = status

        return True, order

    except (InvalidQuantityError, InvalidPriceError, InvalidStateError) as e:
        return False, str(e)

def process_order(input_file):
    processed = []
    skipped = []
    try:
        with open(input_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                is_valid, result = validate_order(row)
                if is_valid:
                    processed.append(result)
                else:
                    row['error_reason'] = result
                    skipped.append(row)

        print(f"Processed Orders: {len(processed)}")
        print(f"Skipped Orders: {len(skipped)}")
        return processed, skipped
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
        return [], []
def write_to_csv(processed, skipped):
    if processed:
        with open("orders_processed.csv", "w", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    'order_id', 'customer_name', 'state', 'product','quantity', 'price_per_unit', 'total_amount', 'status'])
            writer.writeheader()
            writer.writerows(processed)

    if skipped:
        with open("orders_skipped.csv", "w", newline="") as f:
            writer = csv.DictWriter(f,
                fieldnames=[
                    'order_id', 'customer_name', 'state', 'product','quantity', 'price_per_unit', 'status', 'error_reason'])
            writer.writeheader()
            writer.writerows(skipped)

input_file = "orders_raw.csv"  
processed_orders, skipped_orders = process_order(input_file)
write_to_csv(processed_orders, skipped_orders)

# Processed Orders: 89
# Skipped Orders: 61