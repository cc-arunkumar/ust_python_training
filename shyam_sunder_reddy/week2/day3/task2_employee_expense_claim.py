# #Error Handling Task
# Employee Expense Claim Processor (UST)
# Context
# UST employees submit expense claims (travel, meals, accommodation). You must
# write a small processor that validates claims, computes per-day cost for multi-day
# claims, detects duplicates, and never crashes the batch when some claims are
# bad.
# This focuses on exception handling: built-in exceptions and a few custom ones.
# Use try/except/else/finally and keep the code easy to follow.
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
claims = [
 {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"},
 {"claim_id": "C1002", "employee": "Riya", "type": "Meals", "amount": "abc", "days": "1"},#abc in amount
 {"claim_id": None, "employee": "Kiran", "type": "Accommodation", "amount": "4000", "days": "2"},#id
 {"claim_id": "C1003", "employee": "Mona", "type": "Travel", "amount": "900", "days": "0"},
 {"claim_id": "C1004", "employee": "John", "type": "Gifts", "amount": "200", "days": "1"}, #gift
 {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"}, # duplicate
 {"claim_id": "C1005", "employee": "Nisha", "type": "Meals", "amount": "1200", "days": "2"},
 {"employee": "Ravi", "type": "Travel", "amount": "700", "days": "1"}, # missing claim_id
 {"claim_id": "C1006", "employee": "Sona", "type": "Accommodation", "amount": "3000", "days": "two"}, # days invalid
 {"claim_id": "C1007", "employee": "Anil", "type": "Travel", "amount": "0","days": "1"}
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

procesed={}
skipped={}
errors=[]
required_fields=["claim_id","employee","type","amount"]
available_types=["travel","meals","accommodation"]
count=0

# 2. Validation rules (per claim):
for data in claims:
    try:
        # Required fields: claim_id , employee , type , amount , days . Missing or None → 
        # MissingFieldError .
        for key,value in data.items():
            if "claim_id" not in data:
                raise MissingFieldError("claim_id")
            if value is None:
                raise MissingFieldError(key)
            data[key]=value.strip()
            if value=="":
                raise MissingFieldError(key)
            data[key]=value.lower()
            
        # Allowed types: {"Travel", "Meals", "Accommodation"} ; else → InvalidExpenseTypeError .
        if data["type"] not in available_types:
            raise InvalidExpenseTypeError(data["type"])
    
        # amount must convert to float; if not → ValueError .
        data["amount"]=float(data["amount"])
        if data["amount"]==0:
            print("the amount is 0 for: ",data["claim_id"])
        # amount must convert to float; if not → ValueError .
        # days must convert to int; if not → TypeError or ValueError .
        # Error Handling Task 2
        # days must be >= 1; if 0 → this will cause ZeroDivisionError when you compute
        # per-day; handle it explicitly.
        # amount 0 is allowed but should warn.
        data["days"]=int(data["days"])
        if data["days"] <=0:
            raise ZeroDivisionError
        
        if data["claim_id"] in procesed:
            raise DuplicateClaimError
        
        
    except MissingFieldError as mf:
        # if mf=="claim_id":
        #     skipped[count]=f"Missing Field: id"
        # else :
        if "claim_id" not in data or data["claim_id"] is None:
            skipped[count]="index missing Field: id"
        elif mf=="claim_id":
            skipped[count]=f"Missing Field: id"
        else:
            skipped[data["claim_id"]]="missing Field:"
    
    
    except InvalidExpenseTypeError as ie:
        skipped[data["claim_id"]]=f"Allowed Expense Types are only [Travel,Meals,Accommodation] given: {ie}"
    
    except DuplicateClaimError as de:
        skipped[data["claim_id"]]=f"Duplicate values entered at row {count} in for {data["claim_id"]}"
    
    except ZeroDivisionError:
        skipped[data["claim_id"]]=f"division by zero at: {data["claim_id"]}"

    except TypeError:
        skipped[data["claim_id"]]=f"Format not supported at : {data["claim_id"]}"
    
    except ValueError:
        skipped[data["claim_id"]]="Enter the correct format"
        
    except Exception as e:
        errors.append(f"something unexpected happend: {e} at index {count}")
    
    #3. Processing:
    # Compute per_day = amount / days .
    # Store valid processed claims in processed list (as dicts including per_day).
    # Keep skipped list (claim_id or index + reason) for claims you skip due to
    # invalid input.
    # Keep errors list for unexpected failures
    else:
        data["per_day"]=float(data["amount"])/float(data["days"])
        procesed[data["claim_id"]]=data
    finally:
        print("processed line: ",count)
        count+=1
    
# 4. Flow:
# Use try / except for validation and calculation.
# Use else for the happy-path (after validation) to append to processed .
# Use finally to always print a short per-claim completion line.    
print("Total claims: ",len(claims))
print("Claims processed: ",len(procesed))
print("------------------------------")
print("skipped rows are: ")
for key,value in skipped.items():
    print(key,value)
print("------------------------------")
print("rows in which errors are present: ")
for err in errors:
    print(err)
print("------------------------------")
print("rows processed are: ")
for key,value in procesed.items():
    print(key,value)

#sample output
# processed line:  0
# processed line:  1
# processed line:  2
# processed line:  3
# processed line:  4
# processed line:  5
# processed line:  6
# processed line:  7
# processed line:  8
# the amount is 0 for:  c1007
# processed line:  9
# Total claims:  10
# Claims processed:  3
# ------------------------------
# skipped rows are:
# c1002 Enter the correct format
# 2 index missing Field: id
# c1003 division by zero at: c1003
# c1004 Allowed Expense Types are only [Travel,Meals,Accommodation] given: gifts
# c1001 Duplicate values entered at row 5 in for c1001
# 7 index missing Field: id
# c1006 Enter the correct format
# ------------------------------
# rows in which errors are present:
# ------------------------------
# rows processed are:
# c1001 {'claim_id': 'c1001', 'employee': 'arun', 'type': 'travel', 'amount': 1500.0, 'days': 3, 'per_day': 500.0}
# rows in which errors are present:
# ------------------------------
# rows processed are:
# c1001 {'claim_id': 'c1001', 'employee': 'arun', 'type': 'travel', 'amount': 1500.0, 'days': 3, 'per_day': 500.0}
# c1005 {'claim_id': 'c1005', 'employee': 'nisha', 'type': 'meals', 'amount': 1200.0, 'days': 2, 'per_day': 600.0}
# c1007 {'claim_id': 'c1007', 'employee': 'anil', 'type': 'travel', 'amouc1007 {'claim_id': 'c1007', 'employee': 'anil', 'type': 'travel', 'amount': 0.0, 'days': 1, 'per_day': 0.0}
