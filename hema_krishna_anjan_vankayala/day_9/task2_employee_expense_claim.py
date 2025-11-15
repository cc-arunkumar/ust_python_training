#Employee Expense Claim Processor (UST)
# Context
    # UST employees submit expense claims (travel, meals, accommodation). You must
    # write a small processor that validates claims, computes per-day cost for multi-day
    # claims, detects duplicates, and never crashes the batch when some claims are bad.
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

# Custom exception classes for specific error handling
class MissingFieldError(Exception):
    pass
class InvalidExpenseTypeError(Exception):
    pass
class DuplicateClaimError(Exception):
    pass 


# Required fields for each claim
required_list = [ 'claim_id' , 'employee' , 'type' , 'amount' , 'days']
# Allowed expense types
allowed_type = ["travel", "meals", "accommodation"]

# Tracking lists
processed_claim_id = []
processed_list = []
skipped_list = []
errors_list = []
counter = -1
for row in claims:
    try:
        counter += 1
        # Validate required fields
        for req in required_list:
            if 'claim_id' not in row or row[req] is None or row[req] == "":
                raise MissingFieldError
            
        # Validate expense type
        if row['type'].lower().strip() not in allowed_type:
            raise InvalidExpenseTypeError
        
        # Check for duplicate claim_id
        if row['claim_id']  in processed_claim_id:
            raise DuplicateClaimError
        processed_claim_id.append(row['claim_id'])
                
         # Convert amount to float
        row['amount'] = float(row['amount'])
        if row['amount']==0:
            print("Amount is 0 at",row['claim_id'])
            
         # Convert days to integer
        row['days'] = int(row['days'])
        if row['days']<=0:
            raise ZeroDivisionError
        
    # Handle specific exceptions with proper categorization
    except MissingFieldError:
        if "claim_id" not in row or row['claim_id'] is None or row['claim_id'] == "" :
            skipped_list.append([counter,'MissingFieldError'])
        else:  
            skipped_list.append([row['claim_id'],'MissingFieldError'])
    
    except InvalidExpenseTypeError:
        if "claim_id" not in row or row['claim_id'] is None or row['claim_id'] == "" :
            skipped_list.append([counter,'InvalidExpenseTypeError'])
        else:  
            skipped_list.append([row['claim_id'],'InvalidExpenseTypeError'])
    
    except DuplicateClaimError:
        if "claim_id" not in row or row['claim_id'] is None or row['claim_id'] == "" :
            skipped_list.append([counter,'DuplicateClaimError'])
        else:
            skipped_list.append([row['claim_id'],'DuplicateClaimError'])
            
    except TypeError:
        if "claim_id" not in row or row['claim_id'] is None or row['claim_id'] == "" :
            skipped_list.append([counter,'TypeError'])
        else:
            skipped_list.append([row['claim_id'],'TypeError'])
    
    except ValueError:
        if "claim_id" not in row or row['claim_id'] is None or row['claim_id'] == "" :
            skipped_list.append([counter,'ValueError'])
        else:
            skipped_list.append([row['claim_id'],'ValueError'])
            
    except ZeroDivisionError:
        if "claim_id" not in row or row['claim_id'] is None or row['claim_id'] == "" :
            skipped_list.append([counter,'ZeroDivisionError'])
        else:
            skipped_list.append([row['claim_id'],'ZeroDivisionError'])
            
    # Catch-all for unexpected exceptions
    except Exception as e:
        if 'claim_id' not in row.keys() or row['claim_id']== None or row['claim_id'] == "":
            errors_list.append([counter,e])
        else:
            errors_list.append([row['claim_id'],e])
            
    # If no exception, calculate per-day expense    
    else:
        row['per_day'] = row['amount']/row['days']
        processed_list.append(row)
        
    # Always print progress regardless of success/failure
    finally:
        print("processed Line:",counter+1)
        
# Final summary of processing
print("Number of Processed Lines:",len(processed_list))
print("Total Claims",len(claims))
print("Skipped List:",len(skipped_list))
print(skipped_list)
print("--------------------------")
print("Erros List:",len(errors_list))
print(errors_list)
print("--------------------------")
print("Processed List: ",len(processed_list))
for row in processed_list:
    print(row)
    
#Sample Output
# processed Line: 1
# processed Line: 2
# processed Line: 3
# processed Line: 4
# processed Line: 5
# processed Line: 6
# processed Line: 7
# processed Line: 8
# processed Line: 9
# Amount is 0 at C1007
# processed Line: 10
# Number of Processed Lines: 3
# Total Claims 10
# Skipped List: 7
# [['C1002', 'ValueError'], [2, 'MissingFieldError'], ['C1003', 'ZeroDivisionError'], ['C1004', 'InvalidExpenseTypeError'], ['C1001', 'DuplicateClaimError'], [7, 'MissingFieldError'], ['C1006', 'ValueError']]
# --------------------------
# Erros List: 0
# []
# --------------------------
# Processed List:  3
# {'claim_id': 'C1001', 'employee': 'Arun', 'type': 'Travel', 'amount': 1500.0, 'days': 3, 'per_day': 500.0}
# {'claim_id': 'C1005', 'employee': 'Nisha', 'type': 'Meals', 'amount': 1200.0, 'days': 2, 'per_day': 600.0}
# {'claim_id': 'C1007', 'employee': 'Anil', 'type': 'Travel', 'amount': 0.0, 'days': 1, 'per_day': 0.0}