# Day 9: Assignment -> EMPLOYEE EXPENSE CLAIM PROCESSOR

# UST employees submit expense claims (travel, meals, accommodation). You must 
# Writing a small processor that validates claims, computes per-day cost for multi-day 
# claims, detects duplicates, and never crashes the batch when some claims are 
# bad.
# This focuses on exception handling: built-in exceptions and a few custom ones. 
# Should use try/except/else/finally and keep the code easy to follow

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

# Defining Custom Exceptions 
class MissingFieldError(Exception):
    pass

class InvalidExpenseTypeError(Exception):
    pass

class DuplicateClaimError(Exception):
    pass


# Dataset given
claims = [
    {"claim_id": "C1001", "employee": "Arun",  "type": "Travel",    "amount": "1500", "days": "3"},
    {"claim_id": "C1002", "employee": "Riya",  "type": "Meals",     "amount": "abc",  "days": "1"},
    {"claim_id": None,    "employee": "Kiran", "type": "Accommodation", "amount": "4000", "days": "2"},
    {"claim_id": "C1003", "employee": "Mona",  "type": "Travel",    "amount": "900",  "days": "0"},
    {"claim_id": "C1004", "employee": "John",  "type": "Gifts",     "amount": "200",  "days": "1"},
    {"claim_id": "C1001", "employee": "Arun",  "type": "Travel",    "amount": "1500", "days": "3"},  # duplicate
    {"claim_id": "C1005", "employee": "Nisha", "type": "Meals",     "amount": "1200", "days": "2"},
    {"employee": "Ravi",   "type": "Travel",   "amount": "700",  "days": "1"},  # missing claim_id
    {"claim_id": "C1006", "employee": "Sona",  "type": "Accommodation", "amount": "3000", "days": "two"},  # invalid days
    {"claim_id": "C1007", "employee": "Anil",  "type": "Travel",    "amount": "0",    "days": "1"},
]

# Allowed expense types
allowed_types = {"Travel", "Meals", "Accommodation"}

# Tracking and appending claims to below lists
processed = []
skipped = []
errors = []
seen_claim_ids = set()

#Validation
for id, claim in enumerate(claims, start=1):
    print(f"\nProcessing claim {id}...")

    try:
        #Required fields in a list
        required_fields = ["claim_id", "employee", "type", "amount", "days"]
        for field in required_fields:
            if field not in claim or claim[field] is None:
                raise MissingFieldError(f"Missing field: {field}")

        # checking duplicates of claim ID
        if claim["claim_id"] in seen_claim_ids:
            raise DuplicateClaimError(f"Duplicate claim ID: {claim['claim_id']}")

        # checking expense type
        if claim["type"] not in allowed_types:
            raise InvalidExpenseTypeError(f"Invalid expense type: {claim['type']}")

        # Converting amount
        try:
            amount = float(claim["amount"])
        except ValueError:
            raise ValueError("Amount must be numeric")
        
        #converting days
        try:
            days = int(claim["days"])
        except (TypeError, ValueError):
            raise ValueError("Days should be an integer")

        if days == 0:
            raise ZeroDivisionError("Days cannot be zero")

        if amount == 0:
            print("Warning: Claim amount is zero")

        per_day = amount / days
    except (MissingFieldError, DuplicateClaimError, InvalidExpenseTypeError) as e:
    # custom validation errors → skipped list
        skipped.append({"claim": claim.get("claim_id", f"Index-{id}"), "reason": str(e)})

    except (ValueError, ZeroDivisionError) as e:
    # built-in validation errors → skipped list
        skipped.append({"claim": claim.get("claim_id", f"Index-{id}"), "reason": str(e)})

    except Exception as e:
    # Unexpected errors → errors list
        errors.append({"claim": claim.get("claim_id", f"Index-{id}"), "error": str(e)})

        
    else:
        claim["amount"] = amount
        claim["days"] = days
        claim["per_day"] = per_day
        
        processed.append(claim)
        seen_claim_ids.add(claim["claim_id"])
        
    finally:
        print(f"Completed processing claim {claim.get('claim_id', f'Index-{id}')}")


print(f"Total claims attempted: {len(claims)}")
print(f"Number processed: {len(processed)}")
print(f"Number skipped: {len(skipped)}")
print(f"Number errors: {len(errors)}")

print("\nSkipped claims:")
for s in skipped:
    print(s)

print("\nErrors:")
for e in errors:
    print(e)
else:
    print("Unexpected Errors not listed yet")
    

print("\nProcessed claims:")
for p in processed[:3]:
    print(p)

#Output:
'''
Processing claim 1...
Completed processing claim C1001

Processing claim 2...
Completed processing claim C1002

Processing claim 3...
Completed processing claim None

Processing claim 4...
Completed processing claim C1003

Processing claim 5...
Completed processing claim C1004

Processing claim 6...
Completed processing claim C1001

Processing claim 7...
Completed processing claim C1005

Processing claim 8...
Completed processing claim Index-8

Processing claim 9...
Completed processing claim C1006

Processing claim 10...
Warning: Claim amount is zero
Completed processing claim C1007
Total claims attempted: 10
Number processed: 3
Number skipped: 7
Number errors: 0

Skipped claims:
{'claim': 'C1002', 'reason': 'Amount must be numeric'}
{'claim': None, 'reason': 'Missing field: claim_id'}
{'claim': 'C1003', 'reason': 'Days cannot be zero'}
{'claim': 'C1004', 'reason': 'Invalid expense type: Gifts'}
{'claim': 'C1001', 'reason': 'Duplicate claim ID: C1001'}
{'claim': 'Index-8', 'reason': 'Missing field: claim_id'}
{'claim': 'C1006', 'reason': 'Days should be an integer'}

Errors:
Unexpected Errors not listed yet

Processed claims:
{'claim_id': 'C1001', 'employee': 'Arun', 'type': 'Travel', 'amount': 1500.0, 'days': 3, 'per_day': 500.0}
{'claim_id': 'C1005', 'employee': 'Nisha', 'type': 'Meals', 'amount': 1200.0, 'days': 2, 'per_day': 600.0}
{'claim_id': 'C1007', 'employee': 'Anil', 'type': 'Travel', 'amount': 0.0, 'days': 1, 'per_day': 0.0}
'''