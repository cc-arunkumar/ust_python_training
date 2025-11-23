claims = [
 {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"},
 {"claim_id": "C1002", "employee": "Riya", "type": "Meals", "amount": "abc", "days": "1"},
 {"claim_id": None, "employee": "Kiran", "type": "Accommodation", "amount": "4000", "days": "2"},
 {"claim_id": "C1003", "employee": "Mona", "type": "Travel", "amount": "900", "days": "0"},
 {"claim_id": "C1004", "employee": "John", "type": "Gifts", "amount": "200", "days": "1"},
 {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"},  # duplicate
 {"claim_id": "C1005", "employee": "Nisha", "type": "Meals", "amount": "1200", "days": "2"},
 {"employee": "Ravi", "type": "Travel", "amount": "700", "days": "1"},  # missing claim_id
 {"claim_id": "C1006", "employee": "Sona", "type": "Accommodation", "Amount": "3000", "days": "two"},  # days invalid + wrong key
 {"claim_id": "C1007", "employee": "Anil", "type": "Travel", "amount": "0", "days": "1"},
]


# ---- Custom Exceptions ----
class MissingFieldError(Exception):
    pass


class InvalidExpenseTypeError(Exception):
    pass


class DuplicateClaimError(Exception):
    pass


processed_list = []
skipped_list = []
error_list = []
processed_ids = set()

allowed_types = {"travel", "meals", "accommodation"}

for claim in claims:
    try:
        # 1. Check required fields
        required_fields = ["claim_id", "employee", "type", "amount", "days"]
        for field in required_fields:
            if field not in claim or claim[field] is None or str(claim[field]).strip() == "":
                raise MissingFieldError(f"Missing or empty field: {field}")

        # 2. Duplicate check
        cid = claim["claim_id"]
        if cid in processed_ids:
            raise DuplicateClaimError(f"Duplicate claim_id: {cid}")

        # 3. Expense type check
        ctype = claim["type"].lower()
        if ctype not in allowed_types:
            raise InvalidExpenseTypeError(f"Invalid expense type: {claim['type']}")

        # 4. Amount check (key might be 'Amount' by mistake)
        amount_str = claim.get("amount") or claim.get("Amount")
        if amount_str is None:
            raise MissingFieldError("Missing amount field")

        amount = float(amount_str)
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        # 5. Days check
        days = int(claim["days"])
        if days <= 0:
            raise ZeroDivisionError("Days must be greater than zero")

        # 6. Per-day calculation
        per_day = amount / days
        claim["per_day"] = per_day

        # 7. Mark as processed
        processed_list.append(claim)
        processed_ids.add(cid)

    except MissingFieldError as e:
        skipped_list.append(f"{e} | claim: {claim}")
        error_list.append(str(e))
    except InvalidExpenseTypeError as e:
        skipped_list.append(f"{e} | type: {claim.get('type')}")
        error_list.append(str(e))
    except DuplicateClaimError as e:
        skipped_list.append(f"{e} | claim_id: {claim.get('claim_id')}")
        error_list.append(str(e))
    except ValueError as e:
        skipped_list.append(f"ValueError ({e}) | claim_id: {claim.get('claim_id')}")
        error_list.append(str(e))
    except ZeroDivisionError as e:
        skipped_list.append(f"ZeroDivisionError ({e}) | claim_id: {claim.get('claim_id')}")
        error_list.append(str(e))
    except Exception as e:
        skipped_list.append(f"UnexpectedError ({e}) | claim: {claim}")
        error_list.append(str(e))


print("Processed list:")
for c in processed_list:
    print(c)

print("\nSkipped list:")
for s in skipped_list:
    print(s)

print("\nError list:")
for e in error_list:
    print(e)

# # Sample output
# Processed list:
# {'claim_id': 'C1001', 'employee': 'Arun', 'type': 'Travel', 'amount': '1500', 'days': '3', 'per_day': 500.0}
# {'claim_id': 'C1005', 'employee': 'Nisha', 'type': 'Meals', 'amount': '1200', 'days': '2', 'per_day': 600.0}

# Skipped list:
# ', 'days': '2'}
# ZeroDivisionError (Days must be greater than zero) | claim_id: C1003
# Invalid expense type: Gifts | type: Gifts
# Duplicate claim_id: C1001 | claim_id: C1001
# Missing or empty field: claim_id | claim: {'employee': 'Ravi', 'type': 'Travel', 'amount': '700', 'days': '1'}
# Missing or empty field: amount | claim: {'claim_id': 'C1006', 'employee': 'Sona', 'type': 'Accommodation', 'Amount': '3000', 'days': 'two'}
# ValueError (Amount must be greater than zero) | claim_id: C1007

# Error list:
# could not convert string to float: 'abc'
# Missing or empty field: claim_id
# Days must be greater than zero
# Invalid expense type: Gifts
# Duplicate claim_id: C1001
# Missing or empty field: claim_id
# Missing or empty field: amount
# Amount must be greater than zero