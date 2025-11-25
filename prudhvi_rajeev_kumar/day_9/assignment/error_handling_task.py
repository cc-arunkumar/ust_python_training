#Employee Expense Claim Processor (UST)
# Context:-
# UST employees submit expense claims (travel, meals, accommodation). You must
# write a small processor that validates claims, computes per-day cost for multi-day
# claims, detects duplicates, and never crashes the batch when some claims are bad.
# This focuses on exception handling: built-in exceptions and a few custom ones.
# Use try/except/else/finally and keep the code easy to follow.


#Creating the MissingFieldError class for raising exception for missing fields
class MissingFieldError(Exception):
    pass

#Creating the InvalidExpenseTypeError class for raising exception for invalid expense types
class InvalidExpenseTypeError(Exception):
    pass

#Creating the DuplicateClaimError class for raising exception for duplicate claim IDs
class DuplicateClaimError(Exception):
    pass

#The Dataset of expense claims to be processed:
claims = [
    {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"},
    {"claim_id": "C1002", "employee": "Riya", "type": "Meals", "amount": "abc", "days": "1"},
    {"claim_id": None, "employee": "Kiran", "type": "Accommodation", "amount": "4000", "days": "2"},
    {"claim_id": "C1003", "employee": "Mona", "type": "Travel", "amount": "900", "days": "0"},
    {"claim_id": "C1004", "employee": "John", "type": "Gifts", "amount": "200", "days": "1"},
    {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"}, 
    {"claim_id": "C1005", "employee": "Nisha", "type": "Meals", "amount": "1200", "days": "2"},
    {"employee": "Ravi", "type": "Travel", "amount": "700", "days": "1"},
    {"claim_id": "C1006", "employee": "Sona", "type": "Accommodation", "amount": "3000", "days": "two"}, 
    {"claim_id": "C1007", "employee": "Anil", "type": "Travel", "amount": "0", "days": "1"},
]

#The only allowed expense types
allowed_types = ["Travel", "Meals", "Accommodation"]

# Empty Lists to hold processed, skipped, and error claims
processed_data = []
skipped_data = []
error_data = []
seen_id = set()

# Processing each claim in the dataset
count = 1
for claim in claims:
    print(f"Processing Claim #{count}")
    
    # Using try except to handle various exceptions during claim processing
    try:
        required_fields = {"claim_id", "employee", "type", "amount", "days"}
        # Checking for missing fields
        for field in required_fields:
            if field not in claim or claim[field] is None:
                raise MissingFieldError(f"Missing field: {field}")

        cid = claim["claim_id"]

        # Checking for duplicate claim IDs
        if cid in seen_id:
            raise DuplicateClaimError(f"Duplicate claim ID: {cid}")
        seen_id.add(cid)

        # Checking for valid expense type
        if claim["type"] not in allowed_types:
            raise InvalidExpenseTypeError(f"Invalid expense type: {claim['type']}")

        # Validating and converting amount and days
        try:
            amount = float(claim["amount"])
        except Exception:
            raise ValueError(f"Invalid amount value: {claim['amount']}")
        if amount == 0:
            print("Warning: Amount is Zero!")

        try:
            days = int(claim["days"])
        except Exception:
            raise ValueError("Days must be numeric!")
        if days < 1:
            raise ZeroDivisionError("Days must be >= 1")

        per_day = amount / days

    # Handling specific exceptions and categorizing claims accordingly
    except (MissingFieldError, InvalidExpenseTypeError, DuplicateClaimError, ValueError, ZeroDivisionError) as e:
        skipped_data.append({"claim": claim, "error": str(e)})
        print(f"Skipped -> {e}")

    except Exception as e:
        error_data.append({"claim": claim, "error": str(e)})
        print(f"Error -> {e}")

    # If no exceptions, the claim is processed successfully
    else:
        claim["amount"] = amount
        claim["days"] = days
        claim["per_day"] = per_day
        processed_data.append(claim)
        print("Processed Successfully!")

    # Finally block to indicate completion of processing for each claim
    finally:
        print("Completed Task.\n")
    count += 1


# Printing the summary of processing
print("============== SUMMARY ==============")
print(f"Total Claims Attempted : {len(claims)}")
print(f"Valid Claims Processed : {len(processed_data)}")
print(f"Total Skipped          : {len(skipped_data)}")
print(f"Total Errors Occurred  : {len(error_data)}")
print("\nSample Processed Claims:")
for c in processed_data:
    print(c)

#Sample Output:
# Processing Claim #1
# Processed Successfully!
# Completed Task.

# Processing Claim #2
# Skipped -> Invalid amount value: abc
# Completed Task.

# Processing Claim #3
# Skipped -> Missing field: claim_id
# Completed Task.

# Processing Claim #4
# Skipped -> Days must be >= 1
# Completed Task.

# Processing Claim #5
# Skipped -> Invalid expense type: Gifts
# Completed Task.

# Processing Claim #6
# Skipped -> Duplicate claim ID: C1001
# Completed Task.

# Processing Claim #7
# Processed Successfully!
# Completed Task.

# Processing Claim #8
# Skipped -> Missing field: claim_id
# Completed Task.

# Processing Claim #9
# Skipped -> Days must be numeric!
# Completed Task.

# Processing Claim #10
# Warning: Amount is Zero!
# Processed Successfully!
# Completed Task.

# ============== SUMMARY ==============
# Total Claims Attempted : 10
# Valid Claims Processed : 3
# Total Skipped          : 7
# Total Errors Occurred  : 0

# Sample Processed Claims:
# {'claim_id': 'C1001', 'employee': 'Arun', 'type': 'Travel', 'amount': 1500.0, 'days': 3, 'per_day': 500.0}
# {'claim_id': 'C1005', 'employee': 'Nisha', 'type': 'Meals', 'amount': 1200.0, 'days': 2, 'per_day': 600.0}
# {'claim_id': 'C1007', 'employee': 'Anil', 'type': 'Travel', 'amount': 0.0, 'days': 1, 'per_day': 0.0}

