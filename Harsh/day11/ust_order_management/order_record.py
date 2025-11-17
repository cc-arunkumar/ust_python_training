class OrderRecord:
    VALID_STATES = {
        "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
        "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
        "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
        "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
        "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand",
        "West Bengal", "Delhi", "Jammu & Kashmir", "Ladakh"
    }
 
    def __init__(self, raw_row: dict):
        self.raw_row = raw_row
        self.error_reason = ""
 
        # Safely extract and strip
        self.order_id = raw_row.get("order_id", "")
        self.customer_name = str(raw_row.get("customer_name", "")).strip()
        self.state = str(raw_row.get("state", "")).strip()
        self.product = str(raw_row.get("product", "")).strip()
        self.quantity = raw_row.get("quantity", "")
        self.price_per_unit = raw_row.get("price_per_unit", "")
        self.status = str(raw_row.get("status", "")).strip()
 
        self.total_amount = None
 
    def validate(self):
        try:
            # 1. Completely empty row
            if not any(str(val).strip() for val in self.raw_row.values()):
                raise ValueError("Empty row")
 
            # 2. Customer name must not be empty
            if not self.customer_name:
                raise ValueError("Customer name missing")
 
            # 3. State validation
            if self.state not in self.VALID_STATES:
                raise ValueError(f"Invalid state: {self.state}")
 
            # 4. Quantity validation
            try:
                qty = int(float(self.quantity))  # handle floats like "5.0"
            except:
                raise ValueError(f"Non-numeric quantity: {self.quantity}")
 
            if qty <= 0:
                raise ValueError("Quantity must be positive")
 
            self.quantity = abs(qty)  # convert negative to positive just in case
 
            # 5. Price validation
            try:
                price = float(self.price_per_unit)
            except:
                raise ValueError(f"Non-numeric price: {self.price_per_unit}")
 
            if price <= 0:
                raise ValueError("Price must be positive")
 
            self.price_per_unit = price
 
            # 6. Normalize status to uppercase
            self.status = self.status.upper() if self.status else ""
 
            # 7. Compute total_amount
            self.total_amount = self.quantity * self.price_per_unit
 
            return True
 
        except Exception as e:
            self.error_reason = str(e)
            return False
 
    # Output dictionaries
    def to_processed_dict(self):
        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "state": self.state,
            "product": self.product,
            "quantity": self.quantity,
            "price_per_unit": self.price_per_unit,
            "total_amount": self.total_amount,
            "status": self.status
        }
 
    def to_skipped_dict(self):
        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "state": self.state,
            "product": self.product,
            "quantity": self.quantity,
            "price_per_unit": self.price_per_unit,
            "status": self.status,
            "error_reason": self.error_reason
        }