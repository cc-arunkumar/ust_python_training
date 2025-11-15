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

# Actual dataset
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
# Initializing global variables
processed = {}
skipped = []
errors = []
# Creating custom exceptions
class MissingFieldError(Exception):
    pass
class InvalidExpenseTypeError(Exception):
    pass
class DuplicateClaimError(Exception):
    pass

# defining validation function as per the requirements
def Validation(row):
    required_fields = [ "claim_id" , "employee" , "type" , "amount" , "days" ]
    allowed_types = {"Travel", "Meals", "Accommodation"}
    per_day=0
    try:
        for fields in required_fields:
            # checking field exists or not
            if fields in row and len(str(row[fields]).strip())>0 and row[fields]!=None:
                # checking for duplication
                if fields == "claim_id" and row[fields] in processed:
                    raise DuplicateClaimError(f"Claim id: {row[fields]} already exists!")
                # checking for valid type
                if fields == "type":
                    if row["type"].lower().capitalize() not in allowed_types:
                        raise InvalidExpenseTypeError("Invalid type for expense is provided!")
                # Converting amount to float
                if fields == "amount":
                    if int(row[fields])<=0:
                        print("Warning: amount is less than or equal to Zero")
                    elif(str(row[fields]).isdigit()):
                        row[fields]=float(int(row[fields]))
                # Calculating perday after Converting it into int
                if fields == "days":
                    if int(row[fields])>=1:
                        row[fields]=int(row[fields])
                        per_day = int(row["amount"])/row["days"]
                    else:
                        raise ZeroDivisionError("Days value is Zero!")
            else:
                raise MissingFieldError
    # If missing field exists
    except MissingFieldError:
        return False,f"{fields} was missing for this row"
    # if invalid type exists
    except InvalidExpenseTypeError as e:
        return False,str(e)
    # if duplication exists
    except DuplicateClaimError as e:
        return False,str(e)
    except TypeError as e:
        return False,str(e)
    except ValueError as e:
        return False,str(e)
    except ZeroDivisionError as e:
        return False,str(e)
    except Exception as e:
        # if unexpected error forms appending in error list
        errors.append(str(e))
        return False,"Unexpected error occured!"
    else:
        # Validation complete and pushed into precessed dictionary
        processed[row["claim_id"]] = {
            "employee":row["employee"],
            "type":row["type"],
            "amount":row["amount"],
            "days":row["days"],
            "per_day":per_day
        }

    finally:
        print("Claim process completed!")

    return True,"Validated"

for row in claims:
    cond,statement = Validation(row)
    if cond:
        print(statement)
    else:
        # If any exception or validation is not complete then pushed into skipped list
        skipped.append((row.get("claim_id"),statement))

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

# Output
# Claim process completed!
# Validated
# Claim process completed!
# Claim process completed!
# Claim process completed!
# Claim process completed!
# Claim process completed!
# Claim process completed!
# Validated
# Claim process completed!
# Claim process completed!
# Warning: amount is less than or equal to Zero
# Claim process completed!
# Validated
# Total claims : 10
# ========================
# Skipped Claims 7 with reason :
# [('C1002', "invalid literal for int() with base 10: 'abc'"), (None, 'claim_id was missing for this row'), ('C1003', 'Days value is Zero!'), ('C1004', 'Invalid type for expense is provided!'), ('C1001', 'Claim id: C1001 already exists!'), (None, 'claim_id was missing for this row'), ('C1006', "invalid literal for int() with base 10: 'two'")]
# ========================
# Processed Claims 3 :
# {'C1001': {'employee': 'Arun', 'type': 'Travel', 'amount': 1500.0, 'days': 3, 'per_day': 500.0}, 'C1005': {'employee': 'Nisha', 'type': 'Meals', 'amount': 1200.0, 'days': 2, 'per_day': 600.0}, 'C1007': {'employee': 'Anil', 'type': 'Travel', 'amount': '0', 'days': 1, 'per_day': 0.0}}
# ========================
# Unexcepted Error :
# []