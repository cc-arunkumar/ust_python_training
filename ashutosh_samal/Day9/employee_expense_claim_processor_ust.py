#Task Employee Expense Claim Processor (UST)

# Custom Exceptions
class MissingFieldError(Exception):
    pass

class InvalidExpenseTypeError(Exception):
    pass

class DuplicateClaimError(Exception):
    pass

# List of allowed expense types
allowed_types = {"Travel", "Meals", "Accommodation"}

# Sample dataset of claims
claims = [
    {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"},
    {"claim_id": "C1002", "employee": "Riya", "type": "Meals", "amount": "abc", "days": "1"},
    {"claim_id": None, "employee": "Kiran", "type": "Accommodation", "amount": "4000", "days": "2"},
    {"claim_id": "C1003", "employee": "Mona", "type": "Travel", "amount": "900", "days": "0"},
    {"claim_id": "C1004", "employee": "John", "type": "Gifts", "amount": "200", "days": "1"},
    {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"},  # duplicate
    {"claim_id": "C1005", "employee": "Nisha", "type": "Meals", "amount": "1200", "days": "2"},
    {"employee": "Ravi", "type": "Travel", "amount": "700", "days": "1"},  # missing claim_id
    {"claim_id": "C1006", "employee": "Sona", "type": "Accommodation", "amount": "3000", "days": "two"},  # non-numeric days
    {"claim_id": "C1007", "employee": "Anil", "type": "Travel", "amount": "0", "days": "1"},
]

# Helper function to process claims

processed = []
skipped = []
errors = []
claim_ids = set()

for claim in claims:
    try:
        # Check for missing fields
        if not all(key in claim and claim[key] is not None for key in ["claim_id", "employee", "type", "amount", "days"]):
            raise MissingFieldError(f"Missing required field in claim: {claim}")
        
        # Check for duplicate claim_id
        if claim["claim_id"] in claim_ids:
            raise DuplicateClaimError(f"Duplicate claim_id found: {claim['claim_id']}")
        claim_ids.add(claim["claim_id"])

        # Validate expense type
        if claim["type"] not in allowed_types:
            raise InvalidExpenseTypeError(f"Invalid expense type: {claim['type']}")

        # Convert amount and days to proper types
        amount = float(claim["amount"])
        days = int(claim["days"])

        # Validate days (must be >= 1)
        if days <= 0:
            raise ZeroDivisionError("Days cannot be zero or negative.")

        # Compute per day cost
        per_day = amount / days

    except MissingFieldError as e:
        skipped.append((claim, f"Missing field: {str(e)}"))
    except InvalidExpenseTypeError as e:
        skipped.append((claim["claim_id"], f"Invalid expense type: {str(e)}"))
    except DuplicateClaimError as e:
        skipped.append((claim["claim_id"], f"Duplicate claim: {str(e)}"))
    except ValueError as e:
        skipped.append((claim["claim_id"], f"Invalid value: {str(e)}"))
    except ZeroDivisionError as e:
        skipped.append((claim["claim_id"], f"Invalid days: {str(e)}"))
    except Exception as e:
        errors.append(f"Unexpected error for claim {claim['claim_id']}: {str(e)}")
    else:
        # If no exception occurred, add the valid claim with per_day cost
        claim["per_day"] = per_day
        processed.append(claim)
    finally:
        print(f"Processed claim {claim.get('claim_id', 'N/A')}")

# Summary
print("\nSummary:")
print(f"Total claims attempted: {len(claims)}")
print(f"Claims processed: {len(processed)}")
print("Skipped claims:")
for skipped_claim in skipped:
    print(f"  - {skipped_claim[0]}: {skipped_claim[1]}")
print("Errors:")
for error in errors:
    print(f"  - {error}")
print("\nSample processed claims:")
for claim in processed[:3]:  # Show a few samples
    print(claim)
    

#Sample Execution
# Processed claim C1001
# Processed claim C1002
# Processed claim None
# Processed claim C1003
# Processed claim C1004
# Processed claim C1001
# Processed claim C1005
# Processed claim N/A
# Processed claim C1006
# Processed claim C1007

# Summary:
# Total claims attempted: 10
# Claims processed: 3
# Skipped claims:
#   - C1002: Invalid value: could not convert string to float: 'abc'
#   - {'claim_id': None, 'employee': 'Kiran', 'type': 'Accommodation', 'amount': '4000', 'days': '2'}: Missing field: Missing required field in claim: {'claim_id': None, 'employee': 'Kiran', 'type': 'Accommodation', 'amount': 
# '4000', 'days': '2'}
#   - C1003: Invalid days: Days cannot be zero or negative.
#   - C1004: Invalid expense type: Invalid expense type: Gifts
#   - C1001: Duplicate claim: Duplicate claim_id found: C1001
#   - {'employee': 'Ravi', 'type': 'Travel', 'amount': '700', 'days': '1'}: Missing field: Missing required field 
# in claim: {'employee': 'Ravi', 'type': 'Travel', 'amount': '700', 'days': '1'}
#   - C1006: Invalid value: invalid literal for int() with base 10: 'two'
# Errors:

# Sample processed claims:
# {'claim_id': 'C1001', 'employee': 'Arun', 'type': 'Travel', 'amount': '1500', 'days': '3', 'per_day': 500.0}    
# {'claim_id': 'C1005', 'employee': 'Nisha', 'type': 'Meals', 'amount': '1200', 'days': '2', 'per_day': 600.0}    
# {'claim_id': 'C1007', 'employee': 'Anil', 'type': 'Travel', 'amount': '0', 'days': '1', 'per_day': 0.0}