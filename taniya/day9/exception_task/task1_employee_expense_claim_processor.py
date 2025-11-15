# Task
# Error Handling Task
# Employee Expense Claim Processor (UST)
# Context
# UST employees submit expense claims (travel, meals, accommodation). You must
# write a small processor that validates claims, computes per-day cost for multi-day
# claims, detects duplicates, and never crashes the batch when some claims are
# bad.
# This focuses on exception handling: built-in exceptions and a few custom ones.
# Use try/except/else/finally and keep the code easy to follow.
# Dataset
# claims = [
#  {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "150
# 0", "days": "3"},
#  {"claim_id": "C1002", "employee": "Riya", "type": "Meals", "amount": "ab
# c", "days": "1"},
#  {"claim_id": None, "employee": "Kiran", "type": "Accommodation", "amou
# nt": "4000", "days": "2"},
#  {"claim_id": "C1003", "employee": "Mona", "type": "Travel", "amount": "9
# 00", "days": "0"},
#  {"claim_id": "C1004", "employee": "John", "type": "Gifts", "amount": "20
# 0", "days": "1"},
#  {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "150
# 0", "days": "3"}, # duplicate
#  {"claim_id": "C1005", "employee": "Nisha", "type": "Meals", "amount": "12
# 00", "days": "2"},
#  {"employee": "Ravi", "type": "Travel", "amount": "700", "days": "1"}, # mi
# ssing claim_id
#  {"claim_id": "C1006", "employee": "Sona", "type": "Accommodation", "amo
# Error Handling Task 1
# unt": "3000", "days": "two"}, # days invalid
#  {"claim_id": "C1007", "employee": "Anil", "type": "Travel", "amount": "0", 
# "days": "1"},
# ]
# This dataset includes:valid claims,non-numeric amount, missing claim_id,
# days = 0 (possible divide-by-zero),
# invalid expense type,
# duplicate claim,
# missing field,
# non-numeric days,
# zero amount.
# Requirements
# 1. Create custom exceptions:
# MissingFieldError — when required field missing or None
# InvalidExpenseTypeError — when type not in allowed list
# DuplicateClaimError — when claim_id already processed
# 2. Validation rules (per claim):
# Required fields: claim_id , employee , type , amount , days . Missing or None → 
# MissingFieldError .
# Allowed types: {"Travel", "Meals", "Accommodation"} ; else → InvalidExpenseTypeError .
# amount must convert to float; if not → ValueError .
# days must convert to int; if not → TypeError or ValueError .
# Error Handling Task 2
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
# Error Handling Task 3

# Custom exceptions for specific validation failures

class MissingFieldError(Exception):
    pass

class InvalidExpenseTypeError(Exception):
    pass

class DuplicateClaimError(Exception):
    pass

# Allowed expense types

allowed_types = {"Travel", "Meals", "Accommodation"}

# Dataset of employee expense claims
claims = [
    {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"},
    {"claim_id": "C1002", "employee": "Riya", "type": "Meals", "amount": "abc", "days": "1"},
    {"claim_id": None, "employee": "Kiran", "type": "Accommodation", "amount": "4000", "days": "2"},
    {"claim_id": "C1003", "employee": "Mona", "type": "Travel", "amount": "900", "days": "0"},
    {"claim_id": "C1004", "employee": "John", "type": "Gifts", "amount": "200", "days": "1"},
    {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"},  
    {"claim_id": "C1005", "employee": "Nisha", "type": "Meals", "amount": "1200", "days": "2"},
    {"employee": "Ravi", "type": "Travel", "amount": "700", "days": "1"},  
    {"claim_id": "C1006", "employee": "Sona", "type": "Accommodation", "amount": "3000", "days": "two"},
    {"claim_id": "C1007", "employee": "Anil", "type": "Travel", "amount": "0", "days": "1"},
]

# Lists to track processing results

processed = []              # valid claims
skipped = []                 # business rule violations
errors = []                 # unexpected technical error
unique_claim_ids = []        # to track duplicates


for i, claim in enumerate(claims):
    print(f"\nProcessing claim index {i}")
    try:
        # Validate required fields
        required_fields = ["claim_id", "employee", "type", "amount", "days"]
        for field in required_fields:
            if field not in claim or claim[field] is None:
                raise MissingFieldError(f"Missing field: {field}")
        # checking the duplicate in claim id
        claim_id = claim["claim_id"]
        if unique_claim_ids.count(claim_id) > 0:
            raise DuplicateClaimError(f"Duplicate claim ID: {claim_id}")
        unique_claim_ids.append(claim_id)
         # Validate expense type
        if claim["type"] not in allowed_types:
            raise InvalidExpenseTypeError(f"Invalid expense type: {claim['type']}")
        # converting amount to float
        amount = float(claim["amount"]) 
        # converting days to integer
        days = int(claim["days"])        

        if days <= 0:
            raise ValueError("Days cannot be zero")

    
        per_day = amount / days
        #  Warn if amount is zero
        if not amount > 0:
            print(f"Warning: Amount is invalid for claim {claim_id}")
    # appending skipped item
    except (MissingFieldError, InvalidExpenseTypeError, DuplicateClaimError,ZeroDivisionError,ValueError) as e:
        skipped.append(f"{claim.get('claim_id', f'index {i}')} skipped: {str(e)}")
    # appending error item
    except Exception as e:
        errors.append(f"{claim.get('claim_id', f'index {i}')} error: {str(e)}")

    else:
        claim["per_day"] = per_day
        processed.append(claim)

    finally:
        print(f"Finished processing claim {claim.get('claim_id', f'index {i}')}")


print("\n--- Summary ---")
print(f"Total claims attempted: {len(claims)}")
print(f"Number processed: {len(processed)}")

print("\nSkipped claims:")
for reason in skipped:
    print(f"  - {reason}")

print("\nErrors:")
if errors:
    for err in errors:
        print(f"  - {err}")
else:
    print("  No unexpected errors.")

print("\nSample processed claims:")
for claim in processed[:3]:
    print(claim)
    
# Output
# Processing claim index 0
# Finished processing claim C1001  

# Processing claim index 1
# Finished processing claim C1002  

# Processing claim index 2
# Finished processing claim None   

# Processing claim index 3
# Finished processing claim C1003  

# Processing claim index 4
# Finished processing claim C1004  

# Processing claim index 5
# Finished processing claim C1001  

# Processing claim index 6
# Finished processing claim C1005  

# Processing claim index 7
# Finished processing claim index 7

# Processing claim index 8
# Finished processing claim C1006

# Processing claim index 9
# Warning: Amount is invalid for claim C1007
# Finished processing claim C1007

# --- Summary ---
# Total claims attempted: 10
# Number processed: 3

# Skipped claims:
#   - C1002 skipped: could not convert string to float: 'abc'
#   - None skipped: Missing field: claim_id
#   - C1003 skipped: Days cannot be zero
#   - C1004 skipped: Invalid expense type: Gifts
#   - C1001 skipped: Duplicate claim ID: C1001
#   - index 7 skipped: Missing field: claim_id
#   - C1006 skipped: invalid literal for int() with base 10: 'two'

# Errors:
#   No unexpected errors.

# Sample processed claims:
# {'claim_id': 'C1001', 'employee': 'Arun', 'type': 'Travel', 'amount': '1500', 'days': '3', 'per_day': 500.0}
# {'claim_id': 'C1005', 'employee': 'Nisha', 'type': 'Meals', 'amount': '1200', 'days': '2', 'per_day': 600.0}
# {'claim_id': 'C1007', 'employee': 'Anil', 'type': 'Travel', 'amount': '0', 'days': '1', 'per_day': 0.0}