import csv
import os
from order_record import OrderRecord
 
class OrderProcessor:
 
    def __init__(self, input_file, processed_file, skipped_file):
        self.input_file = input_file
        self.processed_file = processed_file
        self.skipped_file = skipped_file
        self.valid_records = []
        self.skipped_records = []
 
        # Counters for skip reasons
        self.skip_counts = {
            "empty_row": 0,
            "customer_name_missing": 0,
            "invalid_state": 0,
            "invalid_quantity": 0,
            "invalid_price": 0,
            "other_error": 0,
            "total_skipped": 0
        }
 
    def process(self):
        if not os.path.exists(self.input_file):
            print(f"ERROR: File not found → {self.input_file}")
            return
 
        try:
            with open(self.input_file, newline='', encoding="utf-8") as f:
                reader = csv.DictReader(f)
 
                required_cols = {
                    "order_id", "customer_name", "state", "product",
                    "quantity", "price_per_unit", "status"
                }
                missing_cols = required_cols - set(reader.fieldnames)
                if missing_cols:
                    print(f"ERROR: Missing required columns → {missing_cols}")
                    return
 
                for row in reader:
                    record = OrderRecord(row)
 
                    if record.validate():
                        self.valid_records.append(record.to_processed_dict())
                    else:
                        self.skipped_records.append(record.to_skipped_dict())
                        self._update_skip_counter(record.error_reason)
 
        except Exception as e:
            print("Error reading CSV:", e)
 
        self.write_outputs()
 
    def _update_skip_counter(self, reason: str):
        reason_lower = reason.lower()
 
        if "empty row" in reason_lower:
            self.skip_counts["empty_row"] += 1
        elif "customer name" in reason_lower:
            self.skip_counts["customer_name_missing"] += 1
        elif "invalid state" in reason_lower or "state" in reason_lower:
            self.skip_counts["invalid_state"] += 1
        elif "quantity" in reason_lower:
            self.skip_counts["invalid_quantity"] += 1
        elif "price" in reason_lower:
            self.skip_counts["invalid_price"] += 1
        else:
            self.skip_counts["other_error"] += 1
 
        self.skip_counts["total_skipped"] += 1
 
    def write_outputs(self):
        # Write valid records
        if self.valid_records:
            with open(self.processed_file, "w", newline='', encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=self.valid_records[0].keys())
                writer.writeheader()
                writer.writerows(self.valid_records)
 
        # Write skipped records
        if self.skipped_records:
            with open(self.skipped_file, "w", newline='', encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=self.skipped_records[0].keys())
                writer.writeheader()
                writer.writerows(self.skipped_records)
 
        # Summary
        print("\nProcessing Complete!")
        print(f"Valid records → {len(self.valid_records)}")
        print(f"Skipped records → {len(self.skipped_records)}")
        print("Skip summary →", self.skip_counts)