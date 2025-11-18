# process_orders.py
import csv
import os

# ---- Configuration ----
input_file = "Day11\\orders_raw.csv"
output_file = "Day11\\orders_processed.csv"
output_skipped = "Day11\\orders_skipped.csv"

# Minimal list of valid states — extend as needed
VALID_STATES = {
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir",
    "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
    "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
    "Uttarakhand", "West Bengal", "Ladakh"
}

# Required input columns
req_colmn = ["order_id", "customer_name", "state", "product", "quantity", "price_per_unit", "status"]


# ---- Classes ----
class OrderRecord:


    def __init__(self, raw_row: dict, line_no: int):
        # keep a shallow copy to avoid mutating original external data unexpectedly
        self.raw = {k: (v or "").strip() for k, v in (raw_row.items() if raw_row else [])}
        self.line_no = line_no
        self.error_reason = None
        self.normalized = {}

    def is_empty_row(self):
        # treat row as empty if all fields are empty strings
        return all((v == "" for v in self.raw.values()))

    def validate_and_normalize(self):

        # 0. quick empty row skip
        if self.is_empty_row():
            self.error_reason = "Empty row"
            return False

        # 1. required columns present and non-empty
        for col in req_colmn:
            if col not in self.raw:
                self.error_reason = f"Missing column: {col}"
                return False

        # 2. customer_name not empty
        if not self.raw["customer_name"].strip():
            self.error_reason = "Customer name missing"
            return False

        # 3. quantity must be positive integer (>0)
        qty_raw = self.raw["quantity"]
        try:
            qty = int(qty_raw)
            if qty <= 0:
                self.error_reason = "Quantity must be greater than 0"
                return False
        except Exception:
            self.error_reason = "Quantity is not a valid integer"
            return False

        # 4. price_per_unit numeric and positive (if negative convert to abs)
        price_raw = self.raw["price_per_unit"]
        try:
            price = float(price_raw)
            if price < 0:
                price = abs(price)  # convert negative to absolute per business rule
        except Exception:
            self.error_reason = "Invalid price_per_unit"
            return False

        # 5. state must be in VALID_STATES (case-insensitive compare)
        state_raw = self.raw["state"].strip()
        if not state_raw:
            self.error_reason = "State missing"
            return False
        # normalize state capitalization for comparison
        # attempt simple match: compare lowercased tokens
        normalized_state = None
        for s in VALID_STATES:
            if s.lower() == state_raw.lower():
                normalized_state = s
                break
        if not normalized_state:
            self.error_reason = f"Invalid state: {state_raw}"
            return False

        # 6. compute total_amount and normalize status to uppercase
        total_amount = round(qty * price, 2)
        status = (self.raw["status"] or "").strip().upper() or "UNKNOWN"

        # Build normalized dict (order of columns will match output header)
        self.normalized = {
            "order_id": self.raw.get("order_id", ""),
            "customer_name": self.raw.get("customer_name", ""),
            "state": normalized_state,
            "product": self.raw.get("product", ""),
            "quantity": qty,
            "price_per_unit": f"{price:.2f}",
            "total_amount": f"{total_amount:.2f}",
            "status": status
        }

        return True


class OrderProcessor:
    """
    Reads input CSV, processes rows using OrderRecord, stores valid and skipped lists,
    and writes output CSVs.
    """

    def __init__(self, input_path: str):
        self.input_path = input_path
        self.processed = []  # list of normalized dicts
        self.skipped = []    # list of raw dicts with error_reason

    def _ensure_input_exists(self):
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file '{self.input_path}' not found.")

    def process(self):
        try:
            self._ensure_input_exists()
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return

        with open(self.input_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            # check required columns presence in header
            header = reader.fieldnames or []
            missing_cols = [c for c in req_colmn if c not in header]
            if missing_cols:
                print(f"Input CSV missing required columns: {missing_cols}")
                # we will still attempt to read rows; each row will be marked skipped
            line_no = 1  # logical line counter for friendly messages
            for row in reader:
                line_no += 1
                record = OrderRecord(row, line_no)
                try:
                    valid = record.validate_and_normalize()
                except Exception as ex:
                    # unexpected error during validation: log and continue
                    record.error_reason = f"Unexpected validation error: {ex}"
                    valid = False

                if valid:
                    self.processed.append(record.normalized)
                else:
                    # include original raw data plus reason and line number
                    skipped_row = dict(row)  # shallow copy
                    skipped_row["error_reason"] = record.error_reason
                    skipped_row["__line_no"] = record.line_no
                    self.skipped.append(skipped_row)

        # summary printed to console
        print("Processing complete.")
        print(f"Total rows processed: {len(self.processed) + len(self.skipped)}")
        print(f"Valid rows  : {len(self.processed)}")
        print(f"Skipped rows: {len(self.skipped)}")

    def save_outputs(self, processed_path=output_file, skipped_path=output_skipped):
        # Write processed rows
        if self.processed:
            processed_headers = ["order_id", "customer_name", "state", "product",
                                 "quantity", "price_per_unit", "total_amount", "status"]
            with open(processed_path, "w", newline="", encoding="utf-8") as pf:
                writer = csv.DictWriter(pf, fieldnames=processed_headers)
                writer.writeheader()
                for r in self.processed:
                    writer.writerow(r)
            print(f"Wrote {len(self.processed)} rows to {processed_path}")
        else:
            # create empty file with header so downstream systems find the file
            processed_headers = ["order_id", "customer_name", "state", "product",
                                 "quantity", "price_per_unit", "total_amount", "status"]
            with open(processed_path, "w", newline="", encoding="utf-8") as pf:
                writer = csv.DictWriter(pf, fieldnames=processed_headers)
                writer.writeheader()
            print(f"No valid rows. Created empty file {processed_path} with headers.")

        # Write skipped rows
        skipped_headers = None
        if self.skipped:
            # union of keys from skipped rows to build header (keep readable order)
            # ensure error_reason included
            keys = set()
            for r in self.skipped:
                keys.update(r.keys())
            # prefer known column order if available
            preferred = ["order_id", "customer_name", "state", "product", "quantity",
                         "price_per_unit", "status", "error_reason", "__line_no"]
            # build headers preserving preferred columns first
            skipped_headers = [k for k in preferred if k in keys] + [k for k in keys if k not in preferred]
            with open(skipped_path, "w", newline="", encoding="utf-8") as sf:
                writer = csv.DictWriter(sf, fieldnames=skipped_headers)
                writer.writeheader()
                for r in self.skipped:
                    writer.writerow(r)
            print(f"Wrote {len(self.skipped)} skipped rows to {skipped_path}")
        else:
            # create empty skipped file with basic header
            skipped_headers = ["order_id", "customer_name", "state", "product",
                               "quantity", "price_per_unit", "status", "error_reason", "__line_no"]
            with open(skipped_path, "w", newline="", encoding="utf-8") as sf:
                writer = csv.DictWriter(sf, fieldnames=skipped_headers)
                writer.writeheader()
            print(f"No skipped rows. Created empty file {skipped_path} with headers.")


# ---- Main runner ----
def main():
    print("Order processing started.")
    processor = OrderProcessor(input_file)
    processor.process()
    processor.save_outputs()


if __name__ == "__main__":
    main()


# sample output:

# Order processing started.
# Processing complete.
# Total rows processed: 150
# Valid rows  : 96
# Skipped rows: 54
# Wrote 96 rows to orders_processed.csv
# Wrote 54 skipped rows to orders_skipped.csv
