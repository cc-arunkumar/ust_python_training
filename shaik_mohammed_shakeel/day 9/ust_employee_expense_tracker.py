# Error Handling Task
# Employee Expense Claim Processor (UST)
# Context
# UST employees submit expense claims (travel, meals, accommodation). You must
# write a small processor that validates claims, computes per-day cost for multi-day
# claims, detects duplicates, and never crashes the batch when some claims are
# bad.
# This focuses on exception handling: built-in exceptions and a few custom ones.
# Use try/except/else/finally and keep the code easy to follow.



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


# Requirements
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
# 3. Processing:
# Compute per_day = amount / days .
# Store valid processed claims in processed list (as dicts including per_day).
# Keep skipped list (claim_id or index + reason) for claims you skip due to
# invalid input.
# Keep errors list for unexpected failures.


alloted_types={"Travel", "Meals", "Accommodation"}
required_fields=["claim_id" , "employee" , "type" , "amount" , "days"]
processed=[]
skipped=[]
error=[]
total=0
extra_id=set()
for row in claims:


    try:    
        total+=1

         # Strip whitespace from string values
        row={key: val.strip() if isinstance(val, str) else val for key, val in row.items()}

        # Check required fields 
        try:
            for field in required_fields:
                if field not in row or row[field] is None:
                    raise MissingFieldError(f"{field} if missing")
                
        except MissingFieldError as e:
            skipped.append(row)
            print(e)  
            continue

        # Validate expense type 
        try:
            if row["type"] not in alloted_types:
                raise InvalidExpenseTypeError(f"{row['type']} is not in mentioned alloted type")
            
        except InvalidExpenseTypeError as e:
            skipped.append(row)
            print(row["claim_id"],e)
            continue

        # Check for duplicate claim_id  
        try:
            if row["claim_id"] in extra_id:
                raise DuplicateClaimError(f"{row['claim_id']} is already exists")
            else:
                extra_id.add(row["claim_id"])

        except DuplicateClaimError as e:
            skipped.append(row)
            print(row["claim_id"],e)
            continue
        

        # Validate amount
        try:
            amount=float(row["amount"])
        except ValueError:
            print(row["claim_id"],"The given amount is invalid",row["amount"])
            skipped.append(row)
            continue
        

        # Validate days
        try:
            days=int(row["days"])
        except ValueError:
            skipped.append(row)
            print(row["claim_id"],"Days must be numeric")
            continue

        # Check amounte less than zero or not
        if amount<=0:
            print(f"{row['claim_id']} Warning! The amount must be greater than zero")

        # Id day=0 throw an exception
        try:
            per_day = amount / days
        except ZeroDivisionError:
            skipped.append(row)
            print("Days cannot be zero")
            continue

    # Generic Exception
    except Exception:
        error.append(row)
        print("Unexpected error occurs")
    
    # If no exception occurs add processed claim
    else:
        processed.append({
            **row,
            "amount": amount,
            "days": days,
            "per_day": round(per_day, 2)
        })


# Summary at the end:
# Total claims attempted
# Number processed
# Skipped claims (with reasons)
# Errors (if any)
# Print sample processed claims

print("-----------")
print("Total claims attempted:", total)
print("Processed:", len(processed))
print("Skipped:", len(skipped))
print("Errors:", len(error))
print("processed claims are: \n")
for p in processed:
    print(p)


#Sample Output
# C1002 The given amount is invalid abc
# claim_id if missing
# Days cannot be zero
# C1004 Gifts is not in mentioned alloted type
# C1001 C1001 is already exists
# claim_id if missing
# C1006 Days must be numeric
# C1007 Warning! The amount must be greater than zero
# -----------
# Total claims attempted: 10
# Processed: 3
# Skipped: 7
# Errors: 0
# processed claims are:

# {'claim_id': 'C1001', 'employee': 'Arun', 'type': 'Travel', 'amount': 1500.0, 'days': 3, 'per_day': 500.0}
# {'claim_id': 'C1005', 'employee': 'Nisha', 'type': 'Meals', 'amount': 1200.0, 'days': 2, 'per_day': 600.0}
# {'claim_id': 'C1007', 'employee': 'Anil', 'type': 'Travel', 'amount': 0.0, 'days': 1, 'per_day': 0.0}
# PS C:\Users\303397\Desktop\Training\shaik_mohammed_shakeel> 