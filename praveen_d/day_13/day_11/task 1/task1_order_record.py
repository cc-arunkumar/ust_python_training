import csv
import os


class OrderRecord:

    # Allowed states (at least include the ones in sample)
    VALID_STATES = {
        "Uttar Pradesh", "Maharashtra", "Ladakh", "Karnataka", "Tamil Nadu",
        "Gujarat", "Punjab", "Goa", "Delhi", "Kerala", "Telangana", "Bihar",
        "Rajasthan", "West Bengal", "Haryana", "Madhya Pradesh", "Odisha",
        "Jharkhand", "Assam", "Chhattisgarh", "Uttarakhand", "Himachal Pradesh",
        "Jammu and Kashmir"
    }

    def __init__(self, row: dict):
        # raw dictionary from csv.DictReader
        self.raw = row or {}

    # small helper to avoid None / spaces
    def _get(self, key):
        return (self.raw.get(key, "") or "").strip()

    def is_empty(self):
    
        return all((v is None or str(v).strip() == "") for v in self.raw.values())

    def _base_row_for_skip(self):
        return {
            "order_id": self._get("order_id"),
            "customer_name": self._get("customer_name"),
            "state": self._get("state"),
            "product": self._get("product"),
            "quantity": self._get("quantity"),
            "price_per_unit": self._get("price_per_unit"),
            "status": self._get("status"),
        }

    def validate_and_transform(self):

        # 7. Skip completely empty rows
        if self.is_empty():
            return False, self._base_row_for_skip(), "Empty row"

        base = self._base_row_for_skip()

        # 3. customer_name must not be empty
        customer_name = base["customer_name"]
        if customer_name == "":
            return False, base, "Customer name is empty"

        # 4. state must be valid
        state = base["state"]
        if state == "":
            return False, base, "State is empty"

        # normalize like "uttar pradesh" → "Uttar Pradesh"
        state_norm = state.title()
        if state_norm not in self.VALID_STATES:
            return False, base, f"Invalid state: {state}"

        # 1. quantity must be positive integer
        q_str = base["quantity"]
        try:
            quantity = int(q_str)
        except ValueError:
            return False, base, f"Invalid quantity format: {q_str!r}"

        if quantity <= 0:
            return False, base, "Quantity must be positive"

        # 2. price_per_unit must be positive
        p_str = base["price_per_unit"]
        if p_str == "":
            return False, base, "Missing price_per_unit"

        try:
            price = float(p_str)
        except ValueError:
            return False, base, f"Invalid price_per_unit format: {p_str!r}"

        # If negative, convert to absolute value
        if price < 0:
            price = abs(price)

        # If zero, treat as invalid (not positive)
        if price == 0:
            return False, base, "price_per_unit must be > 0"

        # 6. Normalize status to uppercase
        status_raw = base["status"]
        status_up = status_raw.strip().upper() if status_raw else ""

        # 5. Add total_amount
        total_amount = quantity * price

        # Build the processed row for orders_processed.csv
        processed = {
            "order_id": base["order_id"],
            "customer_name": customer_name,
            "state": state_norm,
            "product": base["product"],
            "quantity": quantity,
            "price_per_unit": price,
            "total_amount": total_amount,
            "status": status_up,
        }

        return True, processed, None


class OrderProcessor:

    def __init__(
        self,
        input_file="task 1\data\orders_raw.csv",
        processed_file="task 1\data\orders_processed.csv",
        skipped_file="task 1\data\orders_skipped.csv",
    ):
        self.input_file = input_file
        self.processed_file = processed_file
        self.skipped_file = skipped_file

    def process(self):
        required_cols = [
            "order_id",
            "customer_name",
            "state",
            "product",
            "quantity",
            "price_per_unit",
            "status",
        ]

        # --- File not found handling ---
        try:
            with open(self.input_file, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)

                # Missing header row
                if reader.fieldnames is None:
                    print("ERROR: Input CSV has no header row.")
                    return

                # Missing columns
                missing = [c for c in required_cols if c not in reader.fieldnames]
                if missing:
                    print("ERROR: Missing columns in CSV:", ", ".join(missing))
                    return

                valid_rows = []
                skipped_rows = []

                for row in reader:
                    record = OrderRecord(row)

                    # Skip completely empty rows (no output)
                    if record.is_empty():
                        continue

                    ok, processed, error = record.validate_and_transform()

                    if ok:
                        valid_rows.append(processed)
                    else:
                        skip_row = record._base_row_for_skip()
                        skip_row["error_reason"] = error
                        skipped_rows.append(skip_row)

                        # also log to console
                        print(
                            f"Skipping order {skip_row.get('order_id') or '(no id)'}: {error}"
                        )

        except FileNotFoundError:
            print(f"ERROR: Input file {self.input_file!r} not found.")
            return

        # --- Write valid orders to orders_processed.csv ---
        processed_fields = [
            "order_id",
            "customer_name",
            "state",
            "product",
            "quantity",
            "price_per_unit",
            "total_amount",
            "status",
        ]

        with open(self.processed_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=processed_fields)
            writer.writeheader()
            for row in valid_rows:
                writer.writerow(row)

        # --- Write skipped orders to orders_skipped.csv ---
        skipped_fields = [
            "order_id",
            "customer_name",
            "state",
            "product",
            "quantity",
            "price_per_unit",
            "status",
            "error_reason",
        ]

        with open(self.skipped_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=skipped_fields)
            writer.writeheader()
            for row in skipped_rows:
                writer.writerow(row)

        print("Processing complete.")
        print(f"Valid records   : {len(valid_rows)}")
        print(f"Skipped records : {len(skipped_rows)}")


if __name__ == "__main__":
    processor = OrderProcessor()   # uses default file names
    processor.process()
