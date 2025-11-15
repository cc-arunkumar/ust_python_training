# Sample claims data with intentional errors (missing fields, invalid values, duplicates, etc.)
claims = [
    {"claim_id": "C1001", "employee": "Arun",  "type": "Travel",    "amount": "1500", "days": "3"},
    {"claim_id": "C1002", "employee": "Riya",  "type": "Meals",     "amount": "abc",  "days": "1"},  # invalid amount
    {"claim_id": None, "employee": "Kiran", "type": "Accommodation", "amount": "4000", "days": "2"}, # missing claim_id
    {"claim_id": "C1003", "employee": "Mona",  "type": "Travel","amount": "900",  "days": "0"},      # invalid days
    {"claim_id": "C1004", "employee": "John",  "type": "Gifts","amount": "200",  "days": "1"},       # invalid type
    {"claim_id": "C1001", "employee": "Arun",  "type": "Travel","amount": "1500", "days": "3"},      # duplicate
    {"claim_id": "C1005", "employee": "Nisha", "type": "Meals","amount": "1200", "days": "2"},
    {"employee": "Ravi",   "type": "Travel",   "amount": "700","days": "1"},                         # missing claim_id
    {"claim_id": "C1006", "employee": "Sona",  "type": "Accommodation","amount": "3000", "days": "two"}, # invalid days format
    {"claim_id": "C1007", "employee": "Anil",  "type": "Travel","amount": "0","days": "1"},          # zero amount
]

# Custom exception classes for specific validation errors
class MissingFieldError(Exception):
    pass

class InvalidExpenseTypeError(Exception):
    pass

class DuplicateClaimError(Exception):
    pass


# Lists to track results
processed = []   # valid claims
skipped = []     # claims skipped due to validation errors
error = []       # unexpected errors
seen_ids = set() # track unique claim IDs

# Required fields and allowed expense types
req_claim = ["claim_id", "employee", "type", "amount", "days"]
allowed_types = {"Travel", "Meals", "Accommodation"}

# Loop through each claim
idx = 0
for row in claims:
    try:
        # Check for missing required fields
        for field in req_claim:
            if field not in row or row[field] is None:
                raise MissingFieldError(f"Missing required field: {field} in claim {row}")
            
        # Check for duplicate claim IDs
        if row["claim_id"] in seen_ids:
            raise DuplicateClaimError(f"Duplicate claim ID found: {row['claim_id']}")
        seen_ids.add(row["claim_id"])

        # Validate expense type
        if row["type"] not in allowed_types:
            raise InvalidExpenseTypeError(f"Invalid expense type: {row['type']} in claim {row}")
        
        # Convert amount and days to numeric values
        amt = float(row["amount"])
        days = int(row["days"])

        # Days must be positive
        if days <= 0:
            raise ValueError(f"Days must be positive integer in claim {row}")
        
        # Warn if amount is zero (but still process)
        if amt == 0:
            print(f"Warning: Zero amount in claim {row}")
        
        # Calculate per-day expense
        per_day = amt / days

    # Handle known validation errors
    except (MissingFieldError, InvalidExpenseTypeError, DuplicateClaimError, ValueError, ZeroDivisionError) as e:
        skipped.append({"claim": row.get("claim_id", f"index_{idx}"), "reason": str(e)})

    # Handle unexpected errors
    except Exception as e:
        error.append({"claim": row.get("claim_id", f"index_{idx}"), "error": str(e)})

    # If no errors, mark claim as processed
    else:
        processed.append(row)

    # Always print completion message
    finally:
        print(f"Completed claim index {idx}")
    idx += 1

# ------------------- Summary Report -------------------
print("\n--- Summary ---")
print(f"Total claims attempted: {len(claims)}")
print(f"Number processed: {len(processed)}")
print(f"Skipped claims: {skipped}")
print(f"Errors: {error}")

print("\nSample processed claims:")
for c in processed[:5]:
    print(c)


        
# Completed claim index 0
# Completed claim index 1
# Completed claim index 2
# Completed claim index 3
# Completed claim index 4
# Completed claim index 5
# Completed claim index 6
# Completed claim index 7
# Completed claim index 8
# Warning: Zero amount in claim {'claim_id': 'C1007', 'employee': 'Anil', 'type': 'Travel', 'amount': '0', 'days': '1'}
# Completed claim index 9

# --- Summary ---
# Total claims attempted: 10
# Number processed: 3
# Skipped claims: [{'claim': 'C1002', 'reason': "could not convert string to float: 'abc'"}, {'claim': None, 'reason': "Missing required field: claim_id in claim {'claim_id': None, 'employee': 'Kiran', 'type': 'Accommodation', 'amount': '4000', 'days': '2'}"}, 
# {'claim': 'C1003', 'reason': "Days must be positive integer in claim {'claim_id': 'C1003', 'employee': 'Mona', 'type': 'Travel', 'amount': '900', 'days': '0'}"}, {'claim': 'C1004', 'reason': "Invalid expense type: Gifts in claim {'claim_id': 'C1004', 'employee': 'John', 'type': 'Gifts', 'amount': '200', 'days': '1'}"}, 
# {'claim': 'C1001', 'reason': 'Duplicate claim ID found: C1001'}, {'claim': 'index_7', 'reason': "Missing required field: claim_id in claim {'employee': 'Ravi', 'type': 'Travel', 'amount': '700', 'days': '1'}"}, {'claim': 'C1006', 'reason': "invalid literal for int() with base 10: 'two'"}]
# Errors: []

# Sample processed claims:
# {'claim_id': 'C1001', 'employee': 'Arun', 'type': 'Travel', 'amount': '1500', 'days': '3'}        
# {'claim_id': 'C1005', 'employee': 'Nisha', 'type': 'Meals', 'amount': '1200', 'days': '2'}        
# {'claim_id': 'C1007', 'employee': 'Anil', 'type': 'Travel', 'amount': '0', 'days': '1'}
        

