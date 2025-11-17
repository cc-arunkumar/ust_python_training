import csv
import os

VALID_STATES = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

class OrderRecord:
    def __init__(self, row):
        self.row = row
        self.error_reason = None
        self.valid = self.validate()

    def validate(self):
        try:
            
            if not self.row.get("customer_name"):
                self.error_reason = "Missing customer_name"
                return False

            
            if self.row.get("state") not in VALID_STATES:
                self.error_reason = "Invalid state"
                return False

            
            try:
                self.row["quantity"] = int(self.row.get("quantity"))
                if self.row["quantity"] <= 0:
                    self.error_reason = "quantity must be positive"
                    return False
            except (ValueError, TypeError):
                self.error_reason = "quantity not a number"
                return False

            
            try:
                self.row["price_per_unit"] = abs(float(self.row.get("price_per_unit")))
                if self.row["price_per_unit"] <= 0:
                    self.error_reason = "price must be positive"
                    return False
            except (ValueError, TypeError):
                self.error_reason = "price not a number"
                return False

            
            self.row["total_amount"] = self.row["quantity"] * self.row["price_per_unit"]

            
            if self.row.get("status"):
                self.row["status"] = self.row["status"].upper()
            else:
                self.error_reason = "Missing status"
                return False

            return True

        except Exception as e:
            self.error_reason = str(e)
            return False


class OrderProcessor:
    def __init__(self, input_file, processed_file, skipped_file):
        self.input_file = input_file
        self.processed_file = processed_file
        self.skipped_file = skipped_file
        self.processed_count = 0
        self.skipped_count = 0

    def process_order(self):
        with open(self.input_file, newline="", encoding="utf-8") as infile, \
            open(self.processed_file, "w", newline="", encoding="utf-8") as valid_out, \
            open(self.skipped_file, "w", newline="", encoding="utf-8") as invalid_out:

            
            reader = csv.DictReader(infile, delimiter="\t")

            valid_fields = ["order_id", "customer_name", "state", "product",
                            "quantity", "price_per_unit", "total_amount", "status"]
            invalid_fields = ["order_id", "customer_name", "state", "product",
                            "quantity", "price_per_unit", "status", "error_reason"]

            
            valid_writer = csv.DictWriter(valid_out, fieldnames=valid_fields)
            invalid_writer = csv.DictWriter(invalid_out, fieldnames=invalid_fields)

            valid_writer.writeheader()
            invalid_writer.writeheader()

            for row in reader:
                order = OrderRecord(row)
                if order.valid:
                    valid_writer.writerow(order.row)
                    self.processed_count += 1
                else:
                    row["error_reason"] = order.error_reason
                    invalid_writer.writerow(row)
                    self.skipped_count += 1

        print(f"Processing complete: {self.processed_count} valid orders, {self.skipped_count} skipped orders.")



if __name__ == "__main__":
    processor = OrderProcessor("orders_raw.csv", "orders_processed.csv", "orders_skipped.csv")
    processor.process_order()
