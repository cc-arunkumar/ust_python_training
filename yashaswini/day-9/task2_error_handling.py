# Employee Expense Claim Processor (UST)


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
 {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "150", "days": "3"},
 {"claim_id": "C1002", "employee": "Riya", "type": "Meals", "amount": "abc", "days": "1"},
 {"claim_id": None, "employee": "Kiran", "type": "Accommodation", "amount": "4000", "days": "2"},
 {"claim_id": "C1003", "employee": "Mona", "type": "Travel", "amount": "900", "days": "0"},
 {"claim_id": "C1004", "employee": "John", "type": "Gifts", "amount": "200", "days": "1"},
 {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"}, # duplicate
 {"claim_id": "C1005", "employee": "Nisha", "type": "Meals", "amount": "1200", "days": "2"},
 {"employee": "Ravi", "type": "Travel", "amount": "700", "days": "1"},
 {"claim_id": "C1006", "employee": "Sona", "type": "Accommodation", "amount": "3000", "days": "two"}, # days invalid
 {"claim_id": "C1007", "employee": "Anil", "type": "Travel", "amount": "0", "days": "1"},
]

processed = {}         #to store validated claims
skipped_claims = []    #to store skipped claims
errors = []            #to store unexpected errors
required_feilds = ["claim_id" , "employee" , "type" , "amount" , "days"]
allowed_types = ["Travel", "Meals", "Accommodation"]

#custom exceptions
class MissingFieldError(Exception):
    pass
class InvalidExpenseTypeError(Exception):
    pass
class DuplicateClaimError(Exception):
    pass


def validate(item):
    try:
        # check each required field
        for value in required_feilds:
            if(value in item and len(str(item[value]).strip())>0 and item[value]!=None):
                
                # check duplicate claim_id
                if(item["claim_id"] in processed):
                    raise DuplicateClaimError
                
                # validating expense typ
                if(value == "type"):
                    if(item[value].lower().capitalize() not in allowed_types):
                        raise InvalidExpenseTypeError
                
                # validating amount
                if(value == "amount"):
                    if(int(item[value])==0):
                        print("Warning amount is zero!!")
                    elif(str(item[value]).isdigit()):
                        item[value]=float(int(item[value]))
                        
                # validating days and calculating per_day
                if(value == "days"):
                    if(int(item[value])<=0):
                        raise ZeroDivisionError
                    else:
                        per_day = int(item["amount"])//int(item[value])
            else:
                raise MissingFieldError
    
    
    #handling exceptions      
    except MissingFieldError:
        return False,f"{value} was missing for this row"
    
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
        #storing processed claims
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

counts=0

#iterating through claims
for data in claims:
    count,reason = validate(data)
    counts+=1
    if(not count):
        skipped_claims.append((data.get("claim_id",counts),reason))

# printing the output:
print(f"Total Claims : {len(claims)}\n")
print("****************************")

print(f"Skipped Claims : {len(skipped_claims)} (with reason) :\n")
print(skipped_claims)
print("****************************")

print(f"Processed Claims {len(processed)} :\n")
print(processed)
print("****************************")

print("Unexcepted Error :")
print(errors)


#o/p:
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
# Total Claims : 10

# ****************************
# Skipped Claims : 7 (with reason) :

# [('C1002', "Couldn't convert invalid amount format"), (None, 'claim_id was missing for this row'), ('C1003', 'Days cannot be zero'), ('C1004', 'Expense type doesnot match'), ('C1001', 'C1001 already exist'), (8, 'claim_id was 
# missing for this row'), ('C1006', "Couldn't convert invalid amount format")]
# ****************************
# Processed Claims 3 :

# {'C1001': {'employee': 'Arun', 'type': 'Travel', 'amount': 150.0, 'days': '3', 'per_day': 50}, 'C1005': {'employee': 'Nisha', 'type': 'Meals', 'amount': 1200.0, 'days': '2', 'per_day': 600}, 'C1007': {'employee': 'Anil', 'type': 'Travel', 'amount': '0', 'days': '1', 'per_day': 0}}
# ****************************
# Unexcepted Error :
# []