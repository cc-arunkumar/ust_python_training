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
# This dataset includes:
# valid claims,
# non-numeric amount,
# missing claim_id,
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

# Custom error types
class MissingFieldError(Exception):
    pass

class InvalidExpenseTypeError(Exception):
    pass

class DuplicateClaimError(Exception):
    pass

# List of allowed expense types
allowed_types = {"Travel", "Meals", "Accommodation"}

# Sample claims data
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

# Lists to store results
processed = []
skipped = []
errors = []
seen_ids = set()

# Process each claim
for i, claim in enumerate(claims):
    try:
        # Check required fields
        required = ["claim_id", "employee", "type", "amount", "days"]
        for field in required:
            if field not in claim or claim[field] is None:
                raise MissingFieldError(f"{field} is missing")

        # Check for duplicate claim_id
        if claim["claim_id"] in seen_ids:
            raise DuplicateClaimError("Duplicate claim ID")
        seen_ids.add(claim["claim_id"])

        # Check valid type
        if claim["type"] not in allowed_types:
            raise InvalidExpenseTypeError("Invalid expense type")

        # Convert amount and days
        amount = float(claim["amount"])
        days = int(claim["days"])

        if days == 0:
            raise ZeroDivisionError("Days cannot be zero")

        if amount == 0:
            print(f"Warning: Amount is zero for {claim['claim_id']}")

        # Calculate per-day cost
        per_day = amount / days

    except (MissingFieldError, InvalidExpenseTypeError, DuplicateClaimError,
            ValueError, TypeError, ZeroDivisionError) as e:
        skipped.append((claim.get("claim_id", f"Index {i}"), str(e)))
    except Exception as e:
        errors.append((claim.get("claim_id", f"Index {i}"), str(e)))
    else:
        claim["per_day"] = per_day
        processed.append(claim)
    finally:
        print(f"Finished claim {claim.get('claim_id', f'Index {i}')}")

# Print summary
print("\n--- Summary ---")
print(f"Total claims: {len(claims)}")
print(f"Processed: {len(processed)}")
print("Skipped:")
for s in skipped:
    print(f"  {s[0]} - {s[1]}")
if errors:
    print("Errors:")
    for e in errors:
        print(f"  {e[0]} - {e[1]}")
print("\nSample processed claims:")
for p in processed[:3]:
     print(p)
    
    
# sample output
# Finished claim C1001
# Finished claim C1002
# Finished claim None
# Finished claim C1003
# Finished claim C1004
# Finished claim C1001
# Finished claim C1005
# Finished claim Index 7
# Finished claim C1006
# Warning: Amount is zero for C1007
# Finished claim C1007

# --- Summary ---
# Total claims: 10
# Processed: 3
# Skipped:
#   C1002 - could not convert string to float: 'abc'
#   None - claim_id is missing
#   C1003 - Days cannot be zero
#   C1004 - Invalid expense type
#   C1001 - Duplicate claim ID
#   Index 7 - claim_id is missing
#   C1006 - invalid literal for int() with base 10: 'two'

# Sample processed claims:
# {'claim_id': 'C1001', 'employee': 'Arun', 'type': 'Travel', 'amount': '1500', 'days': '3', 'per_day': 500.0}
# {'claim_id': 'C1005', 'employee': 'Nisha', 'type': 'Meals', 'amount': '1200', 'days': '2', 'per_day': 600.0}
# {'claim_id': 'C1007', 'employee': 'Anil', 'type': 'Travel', 'amount': '0', 'days': '1', 'per_day': 0.0}