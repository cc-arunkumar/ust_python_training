# Error Handling Task
# Employee Expense Claim Processor (UST)

# Dataset
# This dataset includes:
# valid claims,non-numeric amount,missing claim_id,days = 0 (possible divide-by-zero),invalid expense type,
# duplicate claim,missing field,non-numeric days,zero amount.

claims = [
 {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"},
 {"claim_id": "C1002", "employee": "Riya", "type": "Meals", "amount": "abc", "days": "1"},
 {"claim_id": None, "employee": "Kiran", "type": "Accommodation", "amount": "4000", "days": "2"},
 {"claim_id": "C1003", "employee": "Mona", "type": "Travel", "amount": "900", "days": "0"},
 {"claim_id": "C1004", "employee": "John", "type": "Gifts", "amount": "200", "days": "1"},
 {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"}, # duplicate
 {"claim_id": "C1005", "employee": "Nisha", "type": "Meals", "amount": "1200", "days": "2"},
 {"employee": "Ravi", "type": "Travel", "amount": "700", "days": "1"}, # missing claim_id
 {"claim_id": "C1006", "employee": "Sona", "type": "Accommodation", "amount": "3000", "days": "two"}, # days invalid
 {"claim_id": "C1007", "employee": "Anil", "type": "Travel", "amount": "0", "days": "1"},
]

processed=[]
skipped = []
errors = []
seen_ids = [] 

required = ["claim_id" , "employee" , "type" , "amount" , "days"]
allowed_types = ["Travel", "Meals", "Accommodation"]

# 1. Create custom exceptions:
# MissingFieldError — when required field missing or None
# InvalidExpenseTypeError — when type not in allowed list
# DuplicateClaimError — when claim_id already processed

class MissingFieldError(Exception):
    pass

class InvalidExpenseTypeError(Exception):
    pass

class DuplicateClaimError(Exception):
    pass


# 2. Validation rules (per claim):
# Required fields: claim_id , employee , type , amount , days . Missing or None → 
# MissingFieldError .
# Allowed types: {"Travel", "Meals", "Accommodation"} ; else → InvalidExpenseTypeError .
# amount must convert to float; if not → ValueError .
# days must convert to int; if not → TypeError or ValueError .
# days must be >= 1; if 0 → this will cause ZeroDivisionError when you compute
# per-day; handle it explicitly.
# amount 0 is allowed but should warn.

for idx, row in enumerate(claims):
    try:
        
        for field in required:
            if field not in row or row[field] is None:
                raise MissingFieldError(f"Missing required field: {field} in claim {row}")
            
            if row["claim_id"] in seen_ids:
                raise DuplicateClaimError(f"Duplicate claim ID found: {row['claim_id']}")

       
        if row["type"] not in allowed_types:
            raise InvalidExpenseTypeError(f"Invalid expense type: {row['type']} in claim {row}")
        
        amt = float(row["amount"])
        days = int(row["days"])

        if days <= 0:
            raise ZeroDivisionError("Days must be >= 1")

        if amt == 0:
            print(f"Warning: Zero amount in claim {row['claim_id']}")
            print("---------------------------------------")

# Compute per_day = amount / days .
# Store valid processed claims in processed list (as dicts including per_day).
# Keep skipped list (claim_id or index + reason) for claims you skip due to
# invalid input.
# Keep errors list for unexpected failures.
# 4. Flow:
# Use try / except for validation and calculation.
# Use else for the happy-path (after validation) to append to processed .
# Use finally to always print a short per-claim completion line.

        per_day = amt / days
    except (MissingFieldError, InvalidExpenseTypeError, DuplicateClaimError,
            ValueError, ZeroDivisionError) as e:
        skipped.append({"claim": row.get("claim_id", f"index_{idx}"), "reason": str(e)})
        
    except Exception as e:
        errors.append({"claim": row.get("claim_id", f"index_{idx}"), "error": str(e)})
        
    else:
        processed.append({
            "claim_id": row["claim_id"],
            "employee": row["employee"],
            "type": row["type"],
            "amount": amt,
            "days": days,
            "per_day": per_day
        })
        seen_ids.append(row["claim_id"])   
        
    finally:
        print(f"Completed claim index {idx}")
        print("-----------------------------")
      
# 5. Summary at the end:
# Total claims attempted
# Number processed
# Skipped claims (with reasons)
# Errors (if any)
# Print sample processed claims
  
print("\n---------- SUMMARY ----------")
print(f"Total claims attempted: {len(claims)}")
print(f"Number processed: {len(processed)}")
print(f"Skipped claims: {len(skipped)}")

for s in skipped:
    print(f" - {s}")
    
print(f"Errors: {len(errors)}")
for e in errors:
    print(f" - {e}")

print("\nSample processed claims:")
for p in processed:
    print(p)
    

# output
# Completed claim index 0
# -----------------------------
# Completed claim index 1
# -----------------------------
# Completed claim index 2
# -----------------------------
# Completed claim index 3
# -----------------------------
# Completed claim index 4
# -----------------------------
# Completed claim index 5
# -----------------------------
# Completed claim index 6
# -----------------------------
# Completed claim index 7
# -----------------------------
# Completed claim index 8
# -----------------------------
# Warning: Zero amount in claim C1007    
# ------------------------------------
# Completed claim index 9
# -----------------------------

# ---------- SUMMARY ----------
# Total claims attempted: 10
# Number processed: 3
# Skipped claims: 7
#  - {'claim': 'C1002', 'reason': "could not convert string to float: 'abc'"}
#  - {'claim': None, 'reason': "Missing required field: claim_id in claim {'claim_id': None, 'employee': 'Kiran', 'type': 'Accommodation', 'amount': '4000', 'days': '2'}"}
#  - {'claim': 'C1003', 'reason': 'Days must be >= 1'}
#  - {'claim': 'C1004', 'reason': "Invalid expense type: Gifts in claim {'claim_id': 'C1004', 'employee': 'John', 'type': 'Gifts', 'amount': '200', 'days': '1'}"}
#  - {'claim': 'C1001', 'reason': 'Duplicate claim ID found: C1001'}
#  - {'claim': 'index_7', 'reason': "Missing required field: claim_id in claim {'employee': 'Ravi', 'type': 'Travel', 'amount': '700', 'days': '1'}"}
#  - {'claim': 'C1006', 'reason': "invalid literal for int() with base 10: 'two'"}
# Errors: 0

# Sample processed claims:
# {'claim_id': 'C1001', 'employee': 'Arun', 'type': 'Travel', 'amount': 1500.0, 'days': 3, 'per_day': 500.0}
# {'claim_id': 'C1005', 'employee': 'Nisha', 'type': 'Meals', 'amount': 1200.0, 'days': 2, 'per_day': 600.0}
# {'claim_id': 'C1007', 'employee': 'Anil', 'type': 'Travel', 'amount': 0.0, 'days': 1, 'per_day': 0.0}
