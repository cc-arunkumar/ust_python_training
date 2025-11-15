
# Error Handling Task
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

# creating Custom exceptions
class MissingFieldError(Exception):
    pass


class InvalidExpenseTypeError(Exception):
    pass


class DuplicateClaimError(Exception):
    pass

# The fields should be required in the data
required_field = ["claim_id","employee","type","amount","days"]

# Type that can be allowed
allowed_types = ["Travel", "Meals", "Accommodation"]

# list for storing skipped data
skipped = []

# list for storig error data
error = []

# Dictionary for storing processed data
processed = {} 

ind = 0     # For counting index and number of data checked
skip = 0    # For counting skipped datas
pro = 0     # For counting processed data

# looping through all claims
for data in claims:
    try:
        # looping through key value pairs in each claims
        for field in required_field:
            if field not in data or data[field] == None:
                raise MissingFieldError("Required Field is missing")
            
        # Checking the type is allowed or not
        if data['type'] not in allowed_types:
            raise InvalidExpenseTypeError("Invalid Expense type")
        
        # Checking if there any duplicate claim ids
        if data["claim_id"] in processed:
            raise DuplicateClaimError
        
        # Comverting amount into float
        data["amount"] = float(data["amount"])
        
        if data["amount"] == 0:
            print("Warning: Amount is 0")
        
        # Converting days into integer
        data["days"] = int(data["days"])
        
        # If days = 0 then throw ZeroDivisionError explicitly
        if data["days"] == 0:
            raise ZeroDivisionError
        
        if data["days"] >= 1:
            per_day = data["amount"]/data["days"]
        
    # Catching MissingFieldError
    except MissingFieldError as m:
        skip += 1
        if "claim_id" in data and data["claim_id"] != None:
            skipped.append([data["claim_id"],m])
        else:
            skipped.append([ind,m])
            
    # Catching InvalidExpenseTypeError
    except InvalidExpenseTypeError as inval:
        skip += 1
        if "claim_id" in data:
            skipped.append([data["claim_id"],inval])
        else:
            skipped.append([ind,inval])

    # Catching DuplicateClaimError            
    except DuplicateClaimError as d:
        skip += 1
        if "claim_id" in data:
            skipped.append([data["claim_id"],d])
        else:
            skipped.append([ind,d])
            
    # Catching ValueError           
    except ValueError as v:
        skip += 1
        if "claim_id" in data:
            skipped.append([data["claim_id"],v])
        else:
            skipped.append([ind,v])
            
    # Catching TypeError          
    except TypeError as t:
        skip += 1
        if "claim_id" in data:
            skipped.append([data["claim_id"],t])
        else:
            skipped.append([ind,t])
            
    # Catching ZeroDivisionError         
    except ZeroDivisionError as z:
        skip += 1
        if "claim_id" in data:
            skipped.append([data["claim_id"],z])
        else:
            skipped.append([ind,z])
            
    # Exception other than custum and default    
    except Exception:
        error.append(data)
            
    # If no exception caught the the data will processed
    else:
        pro += 1
        d = {}
        for key,value in data.items():
            if key != "claim_id":
                d[key] = value
        processed[data['claim_id']] = d
        
    finally:
        ind += 1
        print(f"{ind} claim attempted")
        print("-----------------------")
        
print("Total Claims attempted: ",ind)
print("Number Processed :",pro)
print("Number Skipped: ",skip)
print("=======================")
print("Skipped claims:")
for i in skipped:
    print(i)
print("Error:")
print(error)
print("Processed claims:")
for i in processed:
    print(i,":",processed[i])


#output
# 1 claim attempted
# -----------------------
# 2 claim attempted      
# -----------------------
# 3 claim attempted      
# -----------------------
# 4 claim attempted      
# -----------------------
# 5 claim attempted
# -----------------------
# 6 claim attempted
# -----------------------
# 7 claim attempted
# -----------------------
# 8 claim attempted
# -----------------------
# 9 claim attempted
# -----------------------
# Warning: Amount is 0
# 10 claim attempted
# -----------------------
# Total Claims attempted:  10
# Number Processed : 3
# Number Skipped:  7
# =======================
# Skipped claims:
# ['C1002', ValueError("could not convert string to float: 'abc'")]
# [2, MissingFieldError('Required Field is missing')]
# ['C1003', ZeroDivisionError()]
# ['C1004', InvalidExpenseTypeError('Invalid Expense type')]
# ['C1001', DuplicateClaimError()]
# [7, MissingFieldError('Required Field is missing')]
# ['C1006', ValueError("invalid literal for int() with base 10: 'two'")]
# Error:
# []
# Processed claims:
# C1001 : {'employee': 'Arun', 'type': 'Travel', 'amount': 1500.0, 'days': 3}
# C1005 : {'employee': 'Nisha', 'type': 'Meals', 'amount': 1200.0, 'days': 2}
# C1007 : {'employee': 'Anil', 'type': 'Travel', 'amount': 0.0, 'days': 1}