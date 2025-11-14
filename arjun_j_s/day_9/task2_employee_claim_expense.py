# Employee Expense Claim Processor (UST)
# Context
# UST employees submit expense claims (travel, meals, accommodation). You must
# write a small processor that validates claims, computes per-day cost for multi-day
# claims, detects duplicates, and never crashes the batch when some claims are
# bad.
# This focuses on exception handling: built-in exceptions and a few custom ones.
# Use try/except/else/finally and keep the code easy to follow.

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

processed={}
skipped = []
errors = []
required = ["claim_id" , "employee" , "type" , "amount" , "days"]
allowed_types = ["Travel", "Meals", "Accommodation"]

class MissingFieldError(Exception):
    pass

class InvalidExpenseTypeError(Exception):
    pass

class DuplicateClaimError(Exception):
    pass

def validate(item):
    try:
        for val in required:
            if(val in item and len(str(item[val]).strip())>0 and item[val]!=None):

                if(item["claim_id"] in processed):
                    raise DuplicateClaimError
                
                if(val == "type"):
                    if(item[val].lower().capitalize() not in allowed_types):
                        raise InvalidExpenseTypeError
                    
                if(val == "amount"):
                    if(int(item[val])==0):
                        print("Warning amount is zero!!")
                    elif(str(item[val]).isdigit()):
                        item[val]=float(int(item[val]))

                if(val == "days"):
                    if(int(item[val])<=0):
                        raise ZeroDivisionError
                    else:
                        per_day = int(item["amount"])//int(item[val])
            else:
                raise MissingFieldError
            
    except MissingFieldError:
        return False,f"{val} was missing for this row"
    
    except InvalidExpenseTypeError:
        return False,f"Expense type doesnot match"
    
    except DuplicateClaimError:
        return False,f"{item["claim_id"]} already exist"
    
    except ZeroDivisionError:
        return False,f"Days cannot be zero"
    
    except ValueError:
        return False,f"Couldn't convert invalid amount format"
    
    except Exception as e:
        errors.append(str(e))
        return False,str(e)
    
    else:
        processed[item["claim_id"]] = {
            "employee":item["employee"],
            "type":item["type"],
            "amount":item["amount"],
            "days":item["days"],
            "per_day":per_day
        }
        
    finally:
        print("Claim Process Completion")

    return True,"Success"

count=0
for data in claims:
    con,stmt = validate(data)
    count+=1
    if(not con):
        skipped.append((data.get("claim_id",count),stmt))

print(f"Total claims : {len(claims)}")
print("========================")
print(f"Skipped Claims {len(skipped)} with reason :")
print(skipped)
print("========================")
print(f"Processed Claims {len(processed)} :")
print(processed)
print("========================")
print("Unexcepted Error :")
print(errors)


#Output
# Claim Process Completion
# Claim Process Completion
# Claim Process Completion
# Claim Process Completion
# Claim Process Completion
# Claim Process Completion
# Claim Process Completion
# Claim Process Completion
# Claim Process Completion
# Warning amount is zero!!
# Claim Process Completion
# Total claims : 10
# ========================
# Skipped Claims 7 with reason :
# [('C1002', "Couldn't convert invalid amount format"), (None, 'claim_id was missing for this row'), ('C1003', 'Days cannot be zero'), ('C1004', 'Expense type doesnot match'), ('C1001', 'C1001 already exist'), (8, 'claim_id was 
# missing for this row'), ('C1006', "Couldn't convert invalid amount format")]
# ========================
# Processed Claims 3 :
# {'C1001': {'employee': 'Arun', 'type': 'Travel', 'amount': 1500.0, 'days': '3', 'per_day': 500}, 'C1005': {'employee': 'Nisha', 'type': 'Meals', 'amount': 1200.0, 'days': '2', 'per_day': 600}, 'C1007': {'employee': 'Anil', 'type': 'Travel', 'amount': '0', 'days': '1', 'per_day': 0}}
# ========================
# Unexcepted Error :
# []

