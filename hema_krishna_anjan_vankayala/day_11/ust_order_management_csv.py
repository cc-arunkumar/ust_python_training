# UST Order Management CSV Processing Scenario
# UST is working with a large Indian e-commerce marketplace that handles orders from diverse customers
# across India. The operations team receives a raw CSV export each day containing order details from multiple
# states, regions, and customer backgrounds.
# Your task is to build a Python program that reads this CSV file, validates the data, applies business rules, and
# writes two separate CSV outputs:
# 1. Cleaned and processed orders
# 2. Invalid or skipped records (due to validation failures)
# This ensures high-quality order data for downstream financial and fulfillment teams.
# Objective
# Create a Python program using Object-Oriented Programming (OOP) and proper error handling to:
# 1. Read an input CSV: orders_raw.csv
# 2. Validate and transform order data
# 3. Write valid processed orders to: orders_processed.csv
# 4. Write skipped/invalid records to: orders_skipped.csv

# 

import csv 
states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
"Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
"Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
"Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
"Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
"Uttar Pradesh", "Uttarakhand", "West Bengal" ]
class OrderRecord:
    def __init__(self,order_id,customer_name,state,product,quantity,price_per_unit,status):
        self.order_id=order_id
        self.customer_name=customer_name
        self.state=state
        self.product=product
        self.quantity=quantity
        self.price_per_unit=price_per_unit
        self.status=status  
        
    def is_valid(self):
        reason = ''
        if not self.order_id:
            reason = 'Missing order_id'
            return [False, reason]
        if not self.customer_name:
            reason = 'Missing customer_name'
            return [False, reason]
        if self.state not in states:
            reason = 'Invalid state'
            return [False, reason]
        if not self.product:
            reason = 'Missing product'
            return [False, reason]
        if self.status.upper() not in ['PENDING','SHIPPED','DELIVERED','CANCELLED']:
            reason = 'Invalid status'
            return [False, reason]
        if self.state not in states:
            reason = 'Invalid state'
            return [False, reason]
        return [True, '']
        
        #price neg then abs 
        #quantity neg then abs 
        #skip empty rows 
    def transform(self):
        self.price_per_unit=abs(self.price_per_unit)
        self.quantity=abs(self.quantity)
        self.status=self.status.upper()
    

class OrderProcessor:
    def __init__(self, input_path='orders_raw.csv', processed_path='orders_processed.csv', skipped_path='orders_skipped.csv'):
        self.input_path = input_path
        self.processed_path = processed_path
        self.skipped_path = skipped_path
        self.processed = []    # list of OrderRecord
        self.skipped = []      # list of tuples (raw_row, reason)

    def read_raw(self):
        rows = []
        try:
            with open(self.input_path, 'r', newline='') as fh:
                reader = csv.DictReader(fh)
                for r in reader:
                    rows.append(r)
        except FileNotFoundError:
            raise
        return rows

    def parse_row(self, row):
        # Normalize and coerce types where possible
        order_id = row['order_id']
        customer_name = (row.get('customer_name') or '').strip()
        state = (row.get('state') or '').strip()
        product = (row.get('product') or '').strip()
        qty_raw = row.get('quantity', '')
        price_raw = row.get('price_per_unit', '')
        status = (row.get('status') or '').strip()


        return OrderRecord(order_id, customer_name, state, product, qty_raw, price_raw, status)

    def process(self):
        raw_rows = self.read_raw()
        for row in raw_rows:
            # Skip rows that are completely empty
            if '' in row.values():
                skipped_reason = 'Empty row'
                self.skipped.append((row, skipped_reason))
                continue 
            try:
                row['order_id'] = int(row['order_id'].strip())
            except ValueError:
                skipped_reason = 'Invalid order_id'
                self.skipped.append((row, skipped_reason))
                continue
            except AttributeError:
                skipped_reason = 'Invalid order_id'
                self.skipped.append((row, skipped_reason))
                continue
            try:
                row['quantity'] = int(row['quantity'].strip())
                if row['quantity'] <=0 :
                    raise ValueError
            except ValueError:
                skipped_reason = 'Invalid quantity'
                self.skipped.append((row, skipped_reason))
                continue
            try:
                row['price_per_unit'] = float(row['price_per_unit'].strip())
                if row['price_per_unit'] ==0 :
                    raise ValueError
            except ValueError:
                skipped_reason = 'Invalid price_per_unit'
                self.skipped.append((row, skipped_reason))
                continue
            record = self.parse_row(row)
            # Re-check validity after transform
            valid, reason = record.is_valid()
            if valid:
                self.processed.append(record)
            else:
                # Determine a reason for skipping
                self.skipped.append((row, reason))

    def write_processed(self):
        # Write processed orders with a computed total_price field
        header = ['order_id', 'customer_name', 'state', 'product', 'quantity', 'price_per_unit', 'status', 'total_price']
        with open(self.processed_path, 'w', newline='') as fh:
            writer = csv.DictWriter(fh, fieldnames=header)
            writer.writeheader()
            for rec in self.processed:
                writer.writerow({
                    'order_id': rec.order_id,
                    'customer_name': rec.customer_name,
                    'state': rec.state,
                    'product': rec.product,
                    'quantity': rec.quantity,
                    'price_per_unit': rec.price_per_unit,
                    'status': rec.status,
                    'total_price': f"{rec.quantity * rec.price_per_unit}"
                })

    def write_skipped(self):
        # Write skipped rows including original fields plus error reason
        # Use the union of keys from skipped rows, but ensure common columns exist
        base_fields = ['order_id', 'customer_name', 'state', 'product', 'quantity', 'price_per_unit', 'status']
        header = base_fields + ['error']
        with open(self.skipped_path, 'w', newline='', encoding='utf-8') as fh:
            writer = csv.DictWriter(fh, fieldnames=header)
            writer.writeheader()
            for raw, reason in self.skipped:
                out = {k: raw.get(k, '') for k in base_fields}
                out['error'] = reason
                writer.writerow(out)
    
    def run(self):
        self.process()
        self.write_processed()
        self.write_skipped()
        return {
            'processed': len(self.processed),
            'skipped': len(self.skipped)
        }

orders = OrderProcessor(input_path='orders_raw.csv',
                        processed_path='orders_processed.csv',
                        skipped_path='orders_skipped.csv')
summary = orders.run()
print(summary)   

#Sample Output
# {'processed': 89, 'skipped': 61}