claims = [{"claim_id": "C1001", "employee": "Arun",  "type": "Travel",    "amount": "1500", "days": "3"},
{"claim_id": "C1002", "employee": "Riya",  "type": "Meals",     "amount": "abc",  "days": "1"},
 {"claim_id": None, "employee": "Kiran", "type": "Accommodation", "amount": "4000", "days": "2"},
 {"claim_id": "C1003", "employee": "Mona",  "type": "Travel","amount": "900",  "days": "0"},
 {"claim_id": "C1004", "employee": "John",  "type": "Gifts","amount": "200",  "days": "1"},
 {"claim_id": "C1001", "employee": "Arun",  "type": "Travel","amount": "1500", "days": "3"},  # duplicate
 {"claim_id": "C1005", "employee": "Nisha", "type": "Meals","amount": "1200", "days": "2"},
 {"employee": "Ravi",   "type": "Travel",   "amount": "700","days": "1"},  # missing claim_id
 {"claim_id": "C1006", "employee": "Sona",  "type": "Accommodation","amount": "3000", "days": "two"},  # days invalid
 {"claim_id": "C1007", "employee": "Anil",  "type": "Travel","amount": "0","days": "1"},
 ]

class MissingFieldError(Exception):
    pass

class InvalidExpenseTypeError(Exception):
    pass

class DuplicateClaimError(Exception):
    pass


processed=[]
skipped=[]
error=[]
unique_id=[]
seen_ids=set()

req_claim=["claim_id", "employee", "type", "amount", "days"]
allowed_types={"Travel", "Meals", "Accommodation"}
idx=0
for row in claims:
    try:
        for field in req_claim:
            if field not in row or row[field] is None:
                raise MissingFieldError(f"Missing required field: {field} in claim {row}")
            
        if row["claim_id"]  in seen_ids:
            raise DuplicateClaimError(f"Duplicate claim ID found: {row['claim_id']}")
        seen_ids.add(row["claim_id"])

        if row["type"] not in allowed_types:
            raise InvalidExpenseTypeError(f"Invalid expense type: {row['type']} in claim {row}")
        
        amt=float(row["amount"])
        days=int(row["days"])

        if days <= 0:
            raise ValueError(f"Days must be positive integer in claim {row}")
        
        if amt==0:
            print(f"Warning: Zero amount in claim {row}")
        
        if days<=0:
            raise ZeroDivisionError(f"Days must be positive integer in claim {row}")
        per_day = amt / days


    except(MissingFieldError, InvalidExpenseTypeError, DuplicateClaimError, ValueError, ZeroDivisionError) as e:
        
        skipped.append({"claim": row.get("claim_id", f"index_{idx}"), "reason": str(e)})
    except Exception as e:
        error.append({"claim": row.get("claim_id", f"index_{idx}"), "error": str(e)})
    else:
        
        processed.append(row)
        seen_ids.add(row["claim_id"])
    finally:
        print(f"Completed claim index {idx}")
    idx += 1

print("\n--- Summary ---")
print(f"Total claims attempted: {len(claims)}")
print(f"Number processed: {len(processed)}")
print(f"Skipped claims: {skipped}")
print(f"Errors: {error}")
print("\nSample processed claims:")
for c in processed[:5]:
    print(c)


        
# Completed claim index 0
# Completed claim index 1
# Completed claim index 2
# Completed claim index 3
# Completed claim index 4
# Completed claim index 5
# Completed claim index 6
# Completed claim index 7
# Completed claim index 8
# Warning: Zero amount in claim {'claim_id': 'C1007', 'employee': 'Anil', 'type': 'Travel', 'amount': '0', 'days': '1'}
# Completed claim index 9

# --- Summary ---
# Total claims attempted: 10
# Number processed: 3
# Skipped claims: [{'claim': 'C1002', 'reason': "could not convert string to float: 'abc'"}, {'claim': None, 'reason': "Missing required field: claim_id in claim {'claim_id': None, 'employee': 'Kiran', 'type': 'Accommodation', 'amount': '4000', 'days': '2'}"}, {'claim': 'C1003', 'reason': "Days 
# must be positive integer in claim {'claim_id': 'C1003', 'employee': 'Mona', 'type': 'Travel', 'amount': '900', 'days': '0'}"}, {'claim': 'C1004', 'reason': "Invalid expense type: Gifts in claim {'claim_id': 'C1004', 'employee': 'John', 'type': 'Gifts', 'amount': '200', 'days': '1'}"}, {'claim': 'C1001', 'reason': 'Duplicate claim ID found: C1001'}, {'claim': 'index_7', 'reason': "Missing required field: claim_id in claim {'employee': 'Ravi', 'type': 'Travel', 'amount': '700', 'days': '1'}"}, {'claim': 'C1006', 'reason': "invalid literal for int() with base 10: 'two'"}]
# Errors: []

# Sample processed claims:
# {'claim_id': 'C1001', 'employee': 'Arun', 'type': 'Travel', 'amount': '1500', 'days': '3'}        
# {'claim_id': 'C1005', 'employee': 'Nisha', 'type': 'Meals', 'amount': '1200', 'days': '2'}        
# {'claim_id': 'C1007', 'employee': 'Anil', 'type': 'Travel', 'amount': '0', 'days': '1'}
        

