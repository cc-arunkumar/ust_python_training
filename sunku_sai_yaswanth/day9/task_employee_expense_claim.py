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
# Custom exception classes
class MissingFieldError(Exception):
    pass

class InvalidExpenseTypeError(Exception):
    pass

class DuplicateClaimError(Exception):
    pass

keys = ["claim_id", "employee", "type", "amount", "days"]
allowed_types = ["Travel", "Meals", "Accommodation"]
processed = []
skipped = []
error = []

claim_ids = set()
ind = 0


for claim in claims:
    try:
        for key in keys:
            if key not in claim or claim[key] is None:
                raise MissingFieldError(f"Missing key '{key}' in claim")
        if claim["type"] not in allowed_types:
            raise InvalidExpenseTypeError(f"Invalid expense type '{claim['type']}' in claim ")
        if claim["claim_id"] in claim_ids:
            raise DuplicateClaimError(f"Duplicate claim_id '{claim['claim_id']}' found in claim ")
        claim_ids.add(claim["claim_id"])
        
        claim["amount"] = float(claim["amount"])
        if claim["amount"] == 0:
            print(f"Warning: Amount is 0 for claim {claim['claim_id']}")
        
        
        claim["days"] = int(claim["days"])
        if claim["days"] <= 0:
            raise ValueError(f"Days must be greater than zero in claim ")
        per_day = claim["amount"] / claim["days"]
        claim["per_day"] = per_day
        
    except (MissingFieldError, InvalidExpenseTypeError, DuplicateClaimError, ValueError, ZeroDivisionError) as e:
        skipped.append({"claim_id": claim.get("claim_id", ind), "reason": str(e)})
    
    except Exception as e:
        error.append({"claim_id": claim.get("claim_id", ind), "error": str([ind, e])})
    else:
        processed.append(claim)
    
    finally:
        ind += 1
        print(f"Claim {ind} finished.")
print(f"Total claims attempted: {len(claims)}")
print(f"Number of processed claims: {len(processed)}")
print(f"Number of skipped claims: {len(skipped)}")
print("Processed claims:")
for processed_claim in processed:
    print(processed_claim)
    
print("Skipped claims:")
for skipped_claim in skipped:
    print(skipped_claim)

print("Errors:")
for err in error:
    print(err)
    

# output
# Claim 1 finished.
# Claim 2 finished.
# Claim 3 finished.
# Claim 4 finished.
# Claim 5 finished.
# Claim 6 finished.
# Claim 7 finished.
# Claim 8 finished.
# Claim 9 finished.
# Warning: Amount is 0 for claim C1007
# Claim 10 finished.
# Total claims attempted: 10
# Number of processed claims: 3
# Number of skipped claims: 7
# Processed claims:
# {'claim_id': 'C1001', 'employee': 'Arun', 'type': 'Travel', 'amount': 1500.0, 'days': 3, 'per_day': 500.0}
# {'claim_id': 'C1005', 'employee': 'Nisha', 'type': 'Meals', 'amount': 1200.0, 'days': 2, 'per_day': 600.0}
# {'claim_id': 'C1007', 'employee': 'Anil', 'type': 'Travel', 'amount': 0.0, 'days': 1, 'per_day': 0.0}
# Skipped claims:
# {'claim_id': 'C1002', 'reason': "could not convert string to float: 'abc'"}
# {'claim_id': None, 'reason': "Missing key 'claim_id' in claim"}
# {'claim_id': 'C1003', 'reason': 'Days must be greater than zero in claim '}
# {'claim_id': 'C1004', 'reason': "Invalid expense type 'Gifts' in claim "}
# {'claim_id': 'C1001', 'reason': "Duplicate claim_id 'C1001' found in claim "}
# {'claim_id': 7, 'reason': "Missing key 'claim_id' in claim"}
# {'claim_id': 'C1006', 'reason': "invalid literal for int() with base 10: 'two'"}
# Errors: