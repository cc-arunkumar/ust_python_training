# Custom Exceptions
class MissingFieldError(Exception):
    pass

class InvalidExpenseTypeError(Exception):
    pass

class DuplicateClaimError(Exception):
    pass

# Dataset
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

# Required fields
required_fields = ["claim_id", "employee", "type", "amount", "days"]

# Valid expense types
valid_types = ["Travel", "Meals", "Accommodation"]

# Lists for tracking output
skipped_claims = []
error_claims = []
approved_claims = {}

# Counters
index_count = 0
skipped_count = 0
processed_count = 0

# Looping all claims
for claim in claims:
    try:
        # Check missing fields
        for f in required_fields:
            if f not in claim or claim[f] is None:
                raise MissingFieldError("Required field missing")

        # Validate expense type
        if claim["type"] not in valid_types:
            raise InvalidExpenseTypeError("Invalid Expense Type")

        # Check duplicate claim ID
        if claim["claim_id"] in approved_claims:
            raise DuplicateClaimError("Duplicate Claim ID")

        # Convert amount
        claim["amount"] = float(claim["amount"])
        if claim["amount"] == 0:
            print("Warning: Amount is 0")

        # Convert days
        claim["days"] = int(claim["days"])
        if claim["days"] == 0:
            raise ZeroDivisionError("Days cannot be zero")

        # Calculate per-day
        per_day = claim["amount"] / claim["days"]

    except MissingFieldError as m:
        skipped_count += 1
        skipped_claims.append([claim.get("claim_id", index_count), m])

    except InvalidExpenseTypeError as i:
        skipped_count += 1
        skipped_claims.append([claim.get("claim_id", index_count), i])

    except DuplicateClaimError as d:
        skipped_count += 1
        skipped_claims.append([claim.get("claim_id", index_count), d])

    except ValueError as v:
        skipped_count += 1
        skipped_claims.append([claim.get("claim_id", index_count), v])

    except TypeError as t:
        skipped_count += 1
        skipped_claims.append([claim.get("claim_id", index_count), t])

    except ZeroDivisionError as z:
        skipped_count += 1
        skipped_claims.append([claim.get("claim_id", index_count), z])

    except Exception as e:
        error_claims.append([claim.get("claim_id", index_count), e])

    else:
        processed_count += 1
        temp = {}
        for k, v in claim.items():
            if k != "claim_id":
                temp[k] = v
        approved_claims[claim["claim_id"]] = temp

    finally:
        index_count += 1
        print(f"{index_count} claim attempted")
        print("------------------------")

# Summary
print("Total Claims Attempted:", index_count)
print("Processed:", processed_count)
print("Skipped:", skipped_count)
print("==============")
print("Skipped Claims:")
for s in skipped_claims:
    print(s)

print("Errors:")
print(error_claims)

print("Approved Claims:")
for c in approved_claims:
    print(c, ":", approved_claims[c])

# sample output:
# 1 claim attempted
# ------------------------
# 2 claim attempted
# ------------------------
# 3 claim attempted
# ------------------------
# 4 claim attempted
# ------------------------
# 5 claim attempted
# ------------------------
# 6 claim attempted
# ------------------------
# 7 claim attempted
# ------------------------
# 8 claim attempted
# ------------------------
# 9 claim attempted
# ------------------------
# Warning: Amount is 0
# 10 claim attempted
# ------------------------
# Total Claims Attempted: 10
# Processed: 3
# Skipped: 7
# ==============
# Skipped Claims:
# ['C1002', ValueError("could not convert string to float: 'abc'")]
# [None, MissingFieldError('Required field missing')]
# ['C1003', ZeroDivisionError('Days cannot be zero')]
# ['C1004', InvalidExpenseTypeError('Invalid Expense Type')]
# ['C1001', DuplicateClaimError('Duplicate Claim ID')]
# [7, MissingFieldError('Required field missing')]
# ['C1006', ValueError("invalid literal for int() with base 10: 'two'")]
# Errors:
# []
# Approved Claims:
# C1001 : {'employee': 'Arun', 'type': 'Travel', 'amount': 1500.0, 'days': 3}
# C1005 : {'employee': 'Nisha', 'type': 'Meals', 'amount': 1200.0, 'days': 2}
# C1007 : {'employee': 'Anil', 'type': 'Travel', 'amount': 0.0, 'days': 1}
