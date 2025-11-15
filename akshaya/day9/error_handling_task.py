# Create custom exceptions:
# MissingFieldError — when required field missing or None
# InvalidExpenseTypeError — when type not in allowed list
# DuplicateClaimError — when claim_id already processed
# 2. Validation rules (per claim):
# Required fields: claim_id , employee , type , amount , days . Missing or None → 
# MissingFieldError .
# Allowed types: {"Travel", "Meals", "Accommodation"} ; else → InvalidExpenseTypeError .
# amount must convert to float; if not → ValueError .
# days must convert to int; if not → TypeError or ValueError .
# days must be >= 1; if 0 → this will cause ZeroDivisionError when you compute
# per-day; handle it explicitly.
# amount 0 is allowed but should warn.
# 3. Processing:
# Compute per_day = amount / days .
# Store valid processed claims in processed list (as dicts including per_day).
# Keep skipped list (claim_id or index + reason) for claims you skip due to
# invalid input.
# Keep errors list for unexpected failures.
# 4. Flow:
# Use try / except for validation and calculation.
# Use else for the happy-path (after validation) to append to processed .
# Use finally to always print a short per-claim completion line.
# 5. Summary at the end:
# Total claims attempted
# Number processed
# Skipped claims (with reasons)
# Errors (if any)
# Print sample processed claims

# Custom exceptions
class MissingFieldError(Exception):
    pass

class InvalidExpenseTypeError(Exception):
    pass

class DuplicateClaimError(Exception):
    pass

# Allowed expense types
allowed_expense_types = {"Travel", "Meals", "Accommodation"}

# Initialize lists to store processed claims and errors
claims = [
    {"claim_id": "C1001", "employee": "Arun",  "type": "Travel",    "amount": "1500", "days": "3"},
    {"claim_id": "C1002", "employee": "Riya",  "type": "Meals",     "amount": "abc",  "days": "1"},
    {"claim_id": None,     "employee": "Kiran", "type": "Accommodation", "amount": "4000", "days": "2"},
    {"claim_id": "C1003", "employee": "Mona",  "type": "Travel",    "amount": "900",  "days": "0"},
    {"claim_id": "C1004", "employee": "John",  "type": "Gifts",     "amount": "200",  "days": "1"},
    {"claim_id": "C1001", "employee": "Arun",  "type": "Travel",    "amount": "1500", "days": "3"},  
    {"claim_id": "C1005", "employee": "Nisha", "type": "Meals",     "amount": "1200", "days": "2"},
    {"employee": "Ravi",   "type": "Travel",   "amount": "700",  "days": "1"}, 
    {"claim_id": "C1006", "employee": "Sona",  "type": "Accommodation", "amount": "3000", "days": "two"}, 
    {"claim_id": "C1007", "employee": "Anil",  "type": "Travel",    "amount": "0",    "days": "1"},
]

# Initialize lists to store processed claims and errors
processed_list = []
skipped_list = []
error_list = []
count = 0  # To keep track of total claims attempted

# Process each claim
for claim in claims:
    count += 1
    try:
        # Step 1: Check for missing fields
        if not claim.get("claim_id") or not claim.get("employee") or not claim.get("type") or not claim.get("amount") or not claim.get("days"):
            raise MissingFieldError("Missing required field")

        # Step 2: Validate expense type
        if claim["type"] not in allowed_expense_types:
            raise InvalidExpenseTypeError("Invalid expense type")

        # Step 3: Convert amount to float and days to integer
        amount = float(claim["amount"])
        day = int(claim["days"])

        # Step 4: Handle zero amount warning
        if amount == 0:
            print(f"Warning: Claim ID {claim['claim_id']} has amount = 0.")

        # Step 5: Calculate per day cost
        if day == 0:
            raise ZeroDivisionError("Days cannot be 0 for per-day calculation")
        per_day = amount / day

        # Step 6: Check for duplicate claim_id
        if any(existing_claim["claim_id"] == claim["claim_id"] for existing_claim in processed_list):
            raise DuplicateClaimError(f"Duplicate claim_id {claim['claim_id']}")

    except (MissingFieldError, InvalidExpenseTypeError, ValueError, ZeroDivisionError, DuplicateClaimError) as e:
        # Append to skipped list with the reason
        skipped_list.append((claim.get("claim_id", "N/A"), str(e)))
    except Exception as e:
        # General errors
        error_list.append((claim.get("claim_id", "N/A"), str(e)))
    else:
        # No errors, add to processed list
        claim["per_day"] = per_day
        processed_list.append(claim)
    finally:
        # Always print completion line for each claim
        print(f"Processed claim ID: {claim.get('claim_id', 'N/A')}")

# Summary
print("\nSummary Report:")
print(f"Total claims attempted: {count}")
print(f"Number processed: {len(processed_list)}")
print(f"Skipped claims (with reasons): {skipped_list}")
print(f"Errors: {error_list}")
print("\nSample processed claims:")
for processed_claim in processed_list[:3]:  # Show up to 3 claims for sample
    print(processed_claim)
    
    
# sample output
# Processed claim ID: C1001
# Processed claim ID: C1002
# Processed claim ID: None
# Processed claim ID: C1003
# Processed claim ID: C1004
# Processed claim ID: C1001
# Processed claim ID: C1005
# Processed claim ID: N/A
# Processed claim ID: C1006
# Warning: Claim ID C1007 has amount = 0.
# Processed claim ID: C1007

# Summary Report:
# Total claims attempted: 10
# Number processed: 3
# Skipped claims (with reasons): [('C1002', "could not convert string to float: 'abc'"), (None, 'Missing required field'), ('C1003', 'Days cannot be 0 for per-day calculation'), ('C1004', 'Invalid expense type'), ('C1001', 'Duplicate claim_id C1001'), ('N/A', 'Missing required field'), ('C1006', "invalid literal for int() with base 10: 'two'")]
# Errors: []

# Sample processed claims:
# {'claim_id': 'C1001', 'employee': 'Arun', 'type': 'Travel', 'amount': '1500', 'days': '3', 'per_day': 500.0}
# {'claim_id': 'C1005', 'employee': 'Nisha', 'type': 'Meals', 'amount': '1200', 'days': '2', 'per_day': 600.0}
# {'claim_id': 'C1007', 'employee': 'Anil', 'type': 'Travel', 'amount': '0', 'days': '1', 'per_day': 0.0}

