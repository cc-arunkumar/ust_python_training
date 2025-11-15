#Task : Employee Claim Expense 

# List of claims with different issues (missing fields, invalid values, duplicates, etc.)
claims = [
    {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"},
    {"claim_id": "C1002", "employee": "Riya", "type": "Meals", "amount": "abc", "days": "1"},  # invalid amount
    {"claim_id": None, "employee": "Kiran", "type": "Accommodation", "amount": "4000", "days": "2"},  # missing claim_id
    {"claim_id": "C1003", "employee": "Mona", "type": "Travel", "amount": "900", "days": "0"},  # days = 0
    {"claim_id": "C1004", "employee": "John", "type": "Gifts", "amount": "200", "days": "1"},  # invalid type
    {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"}, # duplicate claim_id
    {"claim_id": "C1005", "employee": "Nisha", "type": "Meals", "amount": "1200", "days": "2"}, # valid
    {"employee": "Ravi", "type": "Travel", "amount": "700", "days": "1"}, # missing claim_id
    {"claim_id": "C1006", "employee": "Sona", "type": "Accommodation", "amount": "3000", "days": "two"}, # invalid days format
    {"claim_id": "C1007", "employee": "Anil", "type": "Travel", "amount": "0", "days": "1"}, # amount = 0 (warning only)
]

# Dictionary to store successfully processed claims
processed_list = {}

# List to store skipped claims with reasons
skipped_row = []

# List to store unexpected errors
error = []

# Required fields that must exist in every claim
required_fields = {"claim_id", "employee", "type", "amount", "days"}

# Allowed expense types (Meals must be plural to match input data)
allowed_types = {"Travel", "Meals", "Accommodation"}

# Custom exception classes for different validation errors
class MissingFieldError(Exception):
    pass

class InvalidExepenseType(Exception):
    pass

class DuplicateClaimError(Exception):
    pass

# Function to validate each claim
def validate(item):
    try:
        # Loop through all required fields
        for val in required_fields:
            # Check if field exists, is not empty, and not None
            if(val in item and len(str(item[val]).strip()) > 0 and item[val] != None):

                # Check for duplicate claim_id
                if(item["claim_id"] in processed_list):
                    raise DuplicateClaimError

                # Validate expense type
                if(val == "type"):
                    if(item[val].lower().capitalize() not in allowed_types):
                        raise InvalidExepenseType

                # Validate amount
                if(val == "amount"):
                    if(int(item[val]) == 0):  # amount is zero → warning only
                        print("Warning amount is zero!!")
                    elif(str(item[val]).isdigit()):  # convert valid numeric string to float
                        item[val] = float(int(item[val]))

                # Validate days
                if(val == "days"):
                    if(int(item[val]) <= 0):  # days must be > 0
                        raise ZeroDivisionError
                    else:
                        # Calculate per-day expense
                        per_day = int(item["amount"]) // int(item[val])
            else:
                # If any required field is missing
                raise MissingFieldError

    # Handle different exceptions with specific messages
    except MissingFieldError:
        return False, f"{val} is missing from required field "
    except InvalidExepenseType:
        return False, "Expense Type doesnot match"
    except ZeroDivisionError:
        return False, "Days cannot be Zero"
    except DuplicateClaimError:
        return False, "Duplicate claim_id id is found !!"
    except ValueError:
        return False, "Cannot convert invalid amount"
    except Exception:
        error.append(str(Exception))
        return False, str(Exception)

    else:
        # If validation passes, store claim in processed_list
        processed_list[item["claim_id"]] = {
            "employee": item["employee"],
            "type": item["type"],
            "amount": item["amount"],
            "days": item["days"],
            "per_day": per_day
        }

    finally:
        # Always print completion message
        print("Claim Process Completion")

    return True, "Success"

# Process all claims
count = 0
for data in claims:
    con, stmt = validate(data)  # validate each claim
    count += 1
    if(not con):  # if validation failed, add to skipped list
        skipped_row.append((data.get("claim_id", count), stmt))

# Final summary output
print(f"Total claims : {len(claims)}")
print("========================")
print(f"Skipped Claims {len(skipped_row)} with reason :")
print(skipped_row)
print("========================")
print(f"Processed Claims {len(processed_list)} :")
print(processed_list)
print("========================")
print("Unexpected Error :")
print(error)

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
# [('C1002', 'Cannot convert invalid amount'), (None, 'claim_id is missing from required field '), ('C1003', 'Days 
# cannot be Zero'), ('C1004', 'Expense Type doesnot match'), ('C1001', 'Duplicate claim_id id is found !!'), (8, "<class 'Exception'>"), ('C1006', 'Cannot convert invalid amount')]
# ========================
# Processed Claims 3 :
# {'C1001': {'employee': 'Arun', 'type': 'Travel', 'amount': 1500.0, 'days': '3', 'per_day': 500}, 'C1005': {'employee': 'Nisha', 'type': 'Meals', 'amount': 1200.0, 'days': '2', 'per_day': 600}, 'C1007': {'employee': 'Anil', 'type': 'Travel', 'amount': '0', 'days': '1', 'per_day': 0}}
# ========================
# Unexpected Error :
# ["<class 'Exception'>"]
