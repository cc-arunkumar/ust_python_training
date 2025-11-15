# Task: Employee Expense Claim Processor (UST)

class MissingFieldError(Exception):
    pass

class InvalidExpenseTypeError(Exception):
    pass

class DuplicateClaimError(Exception):
    pass


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
]

required_fields = ["claim_id", "employee", "type", "amount", "days"]
allowed_types = {"Travel", "Meals", "Accommodation"}

processed = []
skipped_list = []
error_list = []
seen_claim_ids = set()

count = 0

for idx, claim in enumerate(claims, start=1):
    try:
        # 1. Check required fields
        for field in required_fields:
            if field not in claim or claim[field] is None:
                raise MissingFieldError(f"Missing field: {field}")

        # 2. Check expense type
        if claim["type"] not in allowed_types:
            raise InvalidExpenseTypeError(f"Invalid type: {claim['type']}")

        # 3. Check duplicate claim_id
        if claim["claim_id"] in seen_claim_ids:
            raise DuplicateClaimError(f"Duplicate claim_id: {claim['claim_id']}")
        seen_claim_ids.add(claim["claim_id"])

        # 4. Convert amount and days
        amount = float(claim["amount"])
        days = int(claim["days"])

        if days <= 0:
            raise ZeroDivisionError("Days must be >= 1")

        per_day = amount / days

        if amount == 0:
            print(f" Warning: Claim {claim['claim_id']} has zero amount")

    except MissingFieldError as e:
        skipped_list.append((claim.get("claim_id", f"index-{idx}"), str(e)))
    except InvalidExpenseTypeError as e:
        skipped_list.append((claim.get("claim_id", f"index-{idx}"), str(e)))
    except DuplicateClaimError as e:
        skipped_list.append((claim.get("claim_id", f"index-{idx}"), str(e)))
    except ValueError as e:
        skipped_list.append((claim.get("claim_id", f"index-{idx}"), "Invalid amount format"))
    except TypeError as e:
        skipped_list.append((claim.get("claim_id", f"index-{idx}"), "Days must be integer"))
    except ZeroDivisionError as e:
        skipped_list.append((claim.get("claim_id", f"index-{idx}"), str(e)))
    except Exception as e:
        error_list.append((claim.get("claim_id", f"index-{idx}"), str(e)))
    else:
        # Happy path → add processed claim
        processed.append({
            **claim,
            "amount": amount,
            "days": days,
            "per_day": per_day
        })
    finally:
        count += 1
        print(f" Finished processing claim {claim.get('claim_id', f'index-{idx}')}")

# --- Summary Report ---
print(" Summary Report")
print("Total claims attempted:", count)
print("Number processed:", len(processed))
print("Skipped claims:", skipped_list)
print("Errors:", error_list)
print("Sample processed claims:", processed)

#Sample Execution
# Finished processing claim C1001
#  Finished processing claim C1002
#  Finished processing claim None
#  Finished processing claim C1003
#  Finished processing claim C1004
#  Finished processing claim C1001
#  Finished processing claim C1005
#  Finished processing claim index-8
#  Finished processing claim C1006
#  Warning: Claim C1007 has zero amount
#  Finished processing claim C1007
#  Summary Report
# Total claims attempted: 10
# Number processed: 3
# Skipped claims: [('C1002', 'Invalid amount/days format'), (None, 'Missing field: claim_id'), ('C1003', 'Days must be >= 1'), ('C1004', 'Invalid type: Gifts'), ('C1001', 'Duplicate claim_id: C1001'), ('index-8', 'Missing field: claim_id'), ('C1006', 'Invalid amount/days format')]
# Errors: []
# Sample processed claims: [{'claim_id': 'C1001', 'employee': 'Arun', 'type': 'Travel', 'amount': 1500.0, 'days': 3, 'per_day': 500.0}, {'claim_id': 'C1005', 'employee': 'Nisha', 'type': 'Meals', 'amount': 1200.0, 'days': 2, 'per_day': 600.0}, {'claim_id': 'C1007', 'employee': 'Anil', 'type': 'Travel', 'amount': 0.0, 'days': 1, 'per_day': 
# 0.0}]
