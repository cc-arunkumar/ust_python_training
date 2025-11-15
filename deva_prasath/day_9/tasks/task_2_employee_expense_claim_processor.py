# Error Handling Task
#  Employee Expense Claim Processor (UST)
#  Context
#  UST employees submit expense claims (travel, meals, accommodation). You must 
# write a small processor that validates claims, computes per-day cost for multi-day 
# claims, detects duplicates, and never crashes the batch when some claims are 
# bad.
#  This focuses on exception handling: built-in exceptions and a few custom ones. 
# Use 
# try/except/else/finally and keep the code easy to follow.


#for handling regex
import re
claims = [
    {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"},
    {"claim_id": "C1002", "employee": "Riya", "type": "Meals", "amount": "abc", "days": "1"},
    {"claim_id": None, "employee": "Kiran", "type": "Accommodation", "amount": "4000", "days": "2"},
    {"claim_id": "C1003", "employee": "Mona", "type": "Travel", "amount": "900", "days": "0"},
    {"claim_id": "C1004", "employee": "John", "type": "Gifts", "amount": "200", "days": "1"},
    {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"},  # duplicate
    {"claim_id": "C1005", "employee": "Nisha", "type": "Meals", "amount": "1200", "days": "2"},
    {"employee": "Ravi", "type": "Travel", "amount": "700", "days": "1"},  # missing claim_id
    {"claim_id": "C1006", "employee": "Sona", "type": "Accommodation", "amount": "3000", "days": "two"},  # days invalid
    {"claim_id": "C1007", "employee": "Anil", "type": "Travel", "amount": "0", "days": "1"},
    {"claim_id": " ", "employee": "Anil", "type": "Travel", "amount": "0", "days": "1"},
]

#custom exception
class MissingFieldError(Exception):
    pass

#custom exception

class InvalidExpenseTypeError(Exception):
    pass

#custom exception

class DuplicateClaimError(Exception):
    pass

#custom exception

class InvalidClaimIDError(Exception):
    pass

#creating a list of required fields,allowed types and empty lists for storing everything
required_fields = ["claim_id", "employee", "type", "amount", "days"]
allowed_types = ["Travel", "Meals", "Accommodation"]
exception_error = []
skipped_list = []
processed_list = []
seen_claims = set()

#regex pattern to handle whitespaces
claim_id_pattern=r"^\S+$"

#iterating throught the data
for i in range(len(claims)):
    #try block start
    try:
        #the first row
        row = claims[i]
        
        #iterating data in the required fields
        for data in required_fields:
            if data not in row or row.get(data) is None:
                #raising exception
                raise MissingFieldError(f"{data} is missing")
            
        #allowed type exception
        if row.get("type") not in allowed_types:
            raise InvalidExpenseTypeError(f"Invalid expense type: {row.get('type')}")
        
        #whitespaces exception
        if not re.match(claim_id_pattern, row["claim_id"]):
            raise InvalidClaimIDError("Invalid claim_id: must not be empty or just spaces")

        #duplicate exception
        if row["claim_id"] in seen_claims:
            raise DuplicateClaimError(f"This claim is already present")
        seen_claims.add(row["claim_id"])

        #value error exception
        try:
            amount = float(row["amount"])
            if amount == 0:
                print(f"Warning: Claim has amount= 0")
        except ValueError:
            raise ValueError("Amount should be numeric value")
        
        #value error exception
        try:
            days = int(row["days"])
        except ValueError:
            raise ValueError("Days should be numeric value")

        #zero division error
        if days <= 0:
            raise ZeroDivisionError("Days cannot be zero or negative")

        per_day= amount/days
        #storing the per dy also
        row["per_day"]= per_day
        
    #handling multiple exceptions
    
    except (MissingFieldError, InvalidExpenseTypeError, DuplicateClaimError, ValueError, ZeroDivisionError,InvalidClaimIDError) as e:
        #appending to the skipped list as a dict
        skipped_list.append({row.get("claim_id"): str(e)})

    except Exception as e:
        #any other exception other than custom exception
        exception_error.append(str(e))
    
    else:
        #storing processed list
        processed_list.append(row)
        
    finally:
        print(f"Processed claim {row.get('claim_id')}")


#summary of the stored data

print(f"Total claims attempted: {len(claims)}")
print(f"Number processed: {len(processed_list)}")
print("Skipped claims:")
for i in skipped_list:
    print(i)
print(f"Errors: {exception_error}")
print("Sample processed claims:")
for i in processed_list:  
    print(i)



#Sample output

# Processed claim C1001
# Processed claim C1002
# Processed claim None 
# Processed claim C1003
# Processed claim C1004
# Processed claim C1001
# Processed claim C1005
# Processed claim None 
# Processed claim C1006
# Warning: Claim has amount= 0
# Processed claim C1007
# Processed claim
# Total claims attempted: 11
# Number processed: 3
# Skipped claims:
# {'C1002': 'Amount should be numeric value'}
# {None: 'claim_id is missing'}
# {'C1003': 'Days cannot be zero or negative'}
# {'C1004': 'Invalid expense type: Gifts'}
# {'C1001': 'This claim is already present'}
# {None: 'claim_id is missing'}
# {'C1006': 'Days should be numeric value'}
# {' ': 'Invalid claim_id: must not be empty or just spaces'}
# Errors: []
# Sample processed claims:
# {'claim_id': 'C1001', 'employee': 'Arun', 'type': 'Travel', 'amount': '1500', 'days': '3', 'per_day': 500.0}
# {'claim_id': 'C1005', 'employee': 'Nisha', 'type': 'Meals', 'amount': '1200', 'days': '2', 'per_day': 600.0}
# {'claim_id': 'C1007', 'employee': 'Anil', 'type': 'Travel', 'amount': '0', 'days': '1', 'per_day': 0.0