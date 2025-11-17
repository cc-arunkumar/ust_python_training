# process_orders.py
import csv
import os
from typing import Dict, Any, List, Optional

INDIAN_STATES = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
    "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
    "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand",
    "West Bengal"
]

REQUIRED_COLUMNS = [
    "order_id", "customer_name", "state", "product", "quantity", "price_per_unit", "status"
]


class OrderRecord:
    def __init__(self, row: Dict[str, Any]) -> None:
        self.row = row
        self.cleaned: Dict[str, Any] = {}
        self.error_reason: Optional[str] = None

    def is_completely_empty(self) -> bool:
        return not any((str(v).strip() if v is not None else "") for v in self.row.values())

    def validate_and_transform(self) -> bool:
        if self.is_completely_empty():
            self.error_reason = "Empty row"
            return False

        order_id = str(self.row.get("order_id", "")).strip()
        customer_name = str(self.row.get("customer_name", "")).strip()
        state = str(self.row.get("state", "")).strip()
        product = str(self.row.get("product", "")).strip()
        status = str(self.row.get("status", "")).strip()

        q_row = str(self.row.get("quantity", "")).strip()
        try:
            quantity = int(q_row)
            if quantity <= 0:
                self.error_reason = "Invalid quantity (must be positive integer)"
                return False
        except Exception:
            self.error_reason = "Quantity not numeric"
            return False

        p_row = str(self.row.get("price_per_unit", "")).strip()
        try:
            price = float(p_row)
        except Exception:
            self.error_reason = "Price not numeric/blank"
            return False

        if price == 0:
            self.error_reason = "Price is zero"
            return False
        if price < 0:
            price = abs(price)

        if not customer_name:
            self.error_reason = "Missing customer name"
            return False

        if state not in INDIAN_STATES:
            self.error_reason = "Invalid state"
            return False

        status = status.upper()
        total_amount = quantity * price

        self.cleaned = {
            "order_id": order_id,
            "customer_name": customer_name,
            "state": state,
            "product": product,
            "quantity": quantity,
            "price_per_unit": price,
            "total_amount": total_amount,
            "status": status,
        }
        return True


class OrderProcessor:
    def __init__(self, input_path: str, processed_path: str, skipped_path: str) -> None:
        self.input_path = input_path
        self.processed_path = processed_path
        self.skipped_path = skipped_path
        self.valid_rows: List[Dict[str, Any]] = []
        self.skipped_rows: List[Dict[str, Any]] = []

    def _check_file_exists(self) -> bool:
        if not os.path.exists(self.input_path):
            print(f"Error: File not found: {self.input_path}")
            return False
        return True

    def _check_columns(self, fieldnames: List[str]) -> bool:
        missing = [c for c in REQUIRED_COLUMNS if c not in fieldnames]
        if missing:
            print(f"Error: Missing columns in CSV: {', '.join(missing)}")
            return False
        return True

    def process(self) -> None:
        if not self._check_file_exists():
            self._write_outputs(empty=True)
            return

        try:
            with open(self.input_path, mode="r", encoding="utf-8") as infile:
          
                reader = csv.DictReader(infile, delimiter="\t")
                if reader.fieldnames is None:
                    print("Error: CSV has no header row.")
                    self._write_outputs(empty=True)
                    return

                if not self._check_columns(reader.fieldnames):
                    self._write_outputs(empty=True, fieldnames=reader.fieldnames)
                    return

                for row in reader:
                    record = OrderRecord(row)
                    try:
                        if record.validate_and_transform():
                            self.valid_rows.append(record.cleaned)
                        else:
                            skipped = {k: str(row.get(k, "")).strip() for k in reader.fieldnames}
                            skipped["error_reason"] = record.error_reason or "Unknown error"
                            self.skipped_rows.append(skipped)
                            print(f"Skipped order_id={skipped.get('order_id', '')}: {skipped['error_reason']}")
                    except Exception as e:
                        skipped = {k: str(row.get(k, "")).strip() for k in reader.fieldnames}
                        skipped["error_reason"] = f"Processing error: {e}"
                        self.skipped_rows.append(skipped)
                        print(f"Error processing row: {e}")

            self._write_outputs(fieldnames=reader.fieldnames)
            print(f"Processed {len(self.valid_rows)} valid rows")
            print(f"Skipped rows logged: {len(self.skipped_rows)}")

        except Exception as e:
            print(f"Fatal error reading file: {e}")
            self._write_outputs(empty=True)

    def _write_outputs(self, empty: bool = False, fieldnames: Optional[List[str]] = None) -> None:
        processed_headers = [
            "order_id", "customer_name", "state", "product",
            "quantity", "price_per_unit", "total_amount", "status"
        ]
        skipped_headers = (fieldnames or REQUIRED_COLUMNS) + ["error_reason"]

        with open(self.processed_path, mode="w", newline="", encoding="utf-8") as processed_file:
            writer = csv.DictWriter(processed_file, fieldnames=processed_headers)
            writer.writeheader()
            if not empty:
                for row in self.valid_rows:
                    writer.writerow(row)

        with open(self.skipped_path, mode="w", newline="", encoding="utf-8") as skipped_file:
            writer = csv.DictWriter(skipped_file, fieldnames=skipped_headers)
            writer.writeheader()
            if not empty:
                for row in self.skipped_rows:
                    writer.writerow(row)


if __name__ == "__main__":
    processor = OrderProcessor(
        input_path="file.csv",
        processed_path="orders_processed.csv",
        skipped_path="orders_skipped.csv",
    )
    processor.process()
