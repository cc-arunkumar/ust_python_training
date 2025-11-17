import os, csv, datetime, math

# Set the base directory where all other folders will be created
current_path = "C:/Users/303383/Desktop/Python training/ust_python_training/felix/day-11/ust_order_processing"

# Create main directory if not exists
if os.path.exists(current_path):
    print("ust_order_processing Directory already exists")
else:
    os.mkdir(current_path)
    print("ust_order_processing created")

# Create input directory
input_dir = "input"
input_path = os.path.join(current_path, input_dir)
if os.path.exists(input_path):
    print("input Directory already exists")
else:
    os.mkdir(input_path)
    print("input Directory created")

# Create output directory
output_dir = "output"
output_path = os.path.join(current_path, output_dir)
if os.path.exists(output_path):
    print("output Directory already exists")
else:
    os.mkdir(output_path)
    print("output Directory created")

# Input CSV file path
in_file = "orders.csv"
input_file = os.path.join(input_path, in_file)

# Output CSV files
processed_path = "processed.csv"
skipped_path = "skipped.csv"

# Create processed.csv if not present
if os.path.exists(os.path.join(output_path, processed_path)):
    print("processed.csv already exists")
else:
    with open(os.path.join(output_path, processed_path), "w") as file:
        pass

# Create skipped.csv if not present
if os.path.exists(os.path.join(output_path, skipped_path)):
    print("skipped.csv already exists")
else:
    with open(os.path.join(output_path, skipped_path), "w") as file:
        pass

# Create logs directory
logs_path = os.path.join(current_path, "logs")
if os.path.exists(logs_path):
    print("logs Directory already exists")
else:
    os.mkdir(logs_path)
    print("logs created")

# Execution log file
excicution_log = os.path.join(logs_path, "excicution_log.txt")
if os.path.exists(excicution_log):
    print("excicution_log.txt already exists")
else:
    with open(excicution_log, "w") as file:
        pass

# Counters for processed and skipped records
skipped = 0
processed = 0

# Custom Exceptions
class QuantityError(Exception):
    pass

class UnitPriceError(Exception):
    pass

class DateInvalidError(Exception):
    pass

class DateInFutureError(Exception):
    pass

# Write skipped items to skipped.csv
def write_to_skipped(item):
    with open(os.path.join(output_path, skipped_path), "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(item.values())

# Write messages to log file
def write_to_log(msg):
    with open(excicution_log, "a", newline="") as file:
        file.writelines(f"{datetime.date.today()} {msg}\n")

# Read and process the orders.csv file
with open(input_file, "r") as file:
    data = csv.DictReader(file)
    header = data.fieldnames

    for item in data:
        try:
            # Validate quantity
            if int(item["quantity"]) <= 0:
                raise QuantityError

            # Validate unit price
            if int(item["unit_price"]) <= 0:
                raise UnitPriceError

            # Validate and parse order_date
            today = datetime.date.today()
            order_date = datetime.datetime.strptime(item["order_date"], "%Y-%m-%d").date()

            # Check if order_date is in the future
            if order_date > today:
                raise DateInFutureError

            # Calculate total cost (rounded up)
            total_cost = math.ceil(int(item["quantity"]) * int(item["unit_price"]))
            item["total_cost"] = total_cost

            # Calculate delivery date (5 days after order)
            delivery_date = order_date + datetime.timedelta(5)

            # If delivery date is Sunday, shift to next day
            if delivery_date.weekday() == 6:  # Sunday = 6
                delivery_date = delivery_date + datetime.timedelta(1)

            item["delivery_date"] = delivery_date

        except QuantityError:
            skipped += 1
            write_to_skipped(item)
            write_to_log("Warning: quantity must be greater than zero")

        except UnitPriceError:
            skipped += 1
            write_to_skipped(item)
            write_to_log("Warning: unit price must be greater than zero")

        except ValueError as v:
            skipped += 1
            write_to_skipped(item)
            write_to_log(f"Warning: {v}")

        except DateInFutureError:
            skipped += 1
            write_to_skipped(item)
            write_to_log("Warning: order date cannot be in the future")

        except Exception:
            skipped += 1
            write_to_skipped(item)
            write_to_log("Warning: Error in date format")

        else:
            # Write processed data to processed.csv
            processed += 1
            with open(os.path.join(output_path, processed_path), "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(item.values())

            # Log successful processing
            write_to_log(f"INFO order {item['order_id']} processed successfully")

# Final summary
print("Processed data: ", processed)
print("Skipped data: ", skipped)


# output

# ust_order_processing Directory already exists
# input Directory already exists
# output Directory already exists
# processed.csv already exists
# skipped.csv already exists
# logs Directory already exists
# excicution_log.txt already exists
# Processed data:  30
# Skipped data:  20