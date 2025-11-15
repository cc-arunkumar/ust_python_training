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



import missing_field_error
import invalid_type_exception_error

import duplicate_claim_error

process_rows = {}
skipped_rows = []
error_rows = []
claims = [
    {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"},
    {"claim_id": "C1002", "employee": "Riya", "type": "Meals", "amount": "abc", "days": "1"},
    {"claim_id": None, "employee": "Kiran", "type": "Accommodation", "amount": "4000", "days": "2"},
    {"claim_id": "C1003", "employee": "Mona", "type": "Travel", "amount": "900", "days": "0"},
    {"claim_id": "C1004", "employee": "John", "type": "Gifts", "amount": "200", "days": "1"},
    {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"},  # duplicate
    {"claim_id": "C1005", "employee": "Nisha", "type": "Meals", "amount": "1200", "days": "2"},
    {"employee": "Ravi", "type": "Travel", "amount": "700", "days": "1"},  # missing claim_id
    {"claim_id": "C1006", "employee": "Sona", "type": "Accommodation", "amount": "3000", "days": "2"}
]

for claim in claims:
    try:

        required = ["claim_id", "employee", "type", "amount", "days"]
        for field in required:
            if field not in claim or claim[field] in [None, ""]:
                raise missing_field_error.MissingFieldError()
        valid_types = ["Travel", "Meals", "Accommodation"]
        if claim["type"] not in valid_types:
            raise invalid_type_exception_error.InvalidTypeExceptionError()
        try:
            claim["amount"] = float(claim["amount"])
        except ValueError:
            skipped_rows.append(f"{claim['claim_id']} - Invalid Amount Error")
            continue
        if claim["amount"] <= 0:
            skipped_rows.append(f"{claim['claim_id']} - Invalid Amount Error")
            continue
        try:
            claim["days"] = int(claim["days"])
        except ValueError:
            skipped_rows.append(f"{claim['claim_id']} - Invalid Days Error")
            continue
        if claim["days"] < 1:
            skipped_rows.append(f"{claim['claim_id']} - Invalid Days Error")
            continue
        if claim["claim_id"] in process_rows:
            raise duplicate_claim_error.Duplicate_claim_error()
        
        process_rows[claim["claim_id"]] = {
            "employee": claim["employee"],
            "type": claim["type"],
            "amount": claim["amount"],
            "days": claim["days"],
            "per_day_amount": claim["amount"] / claim["days"]
        }
    except missing_field_error.MissingFieldError:
        skipped_rows.append(f"{claim.get('claim_id')} - Missing Field Error")
    except invalid_type_exception_error.InvalidTypeExceptionError:
        skipped_rows.append(f"{claim.get('claim_id')} - Invalid Type Exception Error")
    except duplicate_claim_error.Duplicate_claim_error:
        skipped_rows.append(f"{claim.get('claim_id')} - Duplicate Claim Error")
    except Exception:
        error_rows.append(f"{claim.get('claim_id')} - General Exception Error")
print("Processed Rows:", process_rows)
print("Skipped Rows:", skipped_rows)
print("Error Rows:", error_rows)


# ===========sample output==================
# Processed Rows: {'C1001': {'employee': 'Arun', 'type': 'Travel', 'amount': 1500.0, 'days': 3, 'per_day_amount': 500.0}, 
#                  'C1005': {'employee': 'Nisha', 'type': 'Meals', 'amount': 1200.0, 'days': 2, 'per_day_amount': 600.0},
#                  'C1006': {'employee': 'Sona', 'type': 'Accommodation', 'amount': 3000.0, 'days': 2, 'per_day_amount': 1500.0}}



# Skipped Rows: ['C1002 - Invalid Amount Error', 'None - Missing Field Error', 
#                'C1003 - Invalid Days Error', 'C1004 - Invalid Type Exception Error',
#                'C1001 - Duplicate Claim Error', 'None - Missing Field Error']
# Error Rows: []