"""
UST employees submit expense claims (travel, meals, accommodation). You must
write a small processor that validates claims, computes per-day cost for multi-day
claims, detects duplicates, and never crashes the batch when some claims are
bad.
This focuses on exception handling: built-in exceptions and a few custom ones.
Use try/except/else/finally and keep the code easy to follow.
"""

class MissingFieldError(Exception):
    pass

class InvalidExpenseTypeError(Exception):
    pass

class DuplicateClaimError(Exception):
    pass

#Details
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
 {"claim_id": "C1007", "employee": "Anil", "type": "Travel", "amount": "0","days": "1"},
]


# Allowed types in type to check
ALLOWED_TYPES={"Travel","Accommodation","Meals"}

# Storing the rows according to errors
processed_list=[]
skipped_list=[]
error_list=[]
missed_types=[]

required_fields=["claim_id","employee","type","amount","days"]

#To see the Duplicate row is counting
visited_claim_id=set()


#Iterating the each rowd in Claim_Id

for index, claim in enumerate(claims):

    print(f"Running the row {index}")

    try: # trying all the possible error giving codes
        
        # Check row size is 5
        if len(claim)!=5:
            raise MissingFieldError("Roaw does not have 5 fields")
        
        # Check required fields exist & not None
        for field in required_fields:
            if field not in claim or claim[field] is None:
                raise MissingFieldError(f"Missing or None Fiels {field}")
        
        claim_id=claim["claim_id"]

        # Check for duplicated Claim IDs
        if claim_id in visited_claim_id:
            raise DuplicateClaimError(f"Claim Id Already Visited {claim_id}")
        
        #Check valid Expense type
        if claim["type"] not in ALLOWED_TYPES:
            missed_types.append(claim["type"])
            raise InvalidExpenseTypeError(f"Invalid Type Error {claim[type]}")
        
        #amount conversion to float
        try:
            amount=float(claim[amount])
        except:
            raise ValueError("Amount is not Numeric")
        
        #Warning for amount if it is 0
        if amount==0:
            print("Warning : amount is 0")
        
        #Convert to days
        try:
            days=int(claim["days"])
        except:
            raise TypeError("Day entered is not Numeric")
        
        #Days must be greater than 0
        if days==0:
            raise ZeroDivisionError("Days = 0, Enter greater than 0")
        
        #Computing per Day
        per_day=amount/days
    
    # Exceptions
    except (MissingFieldError,InvalidExpenseTypeError,DuplicateClaimError,ValueError,TypeError,ZeroDivisionError) as e:
        skipped_list.append({"claim":claim.get("claim_id", f"index-{index}"), "reason":str(e)})
        print("Skipped Due to error :",e)

    except Exception as unexpected:
        error_list.append(str(unexpected))
        print("Unexpected error :",unexpected)
    
    else:

        # Processing Sucessfully
        processed_list.append({
            "claim_id":claim_id,
            "employee":claim["employee"],
            "type":claim["type"],
            "amount":amount,
            "days":days,
            "per_day":per_day
        })

        # marking as seen (ID)
        visited_claim_id.add(claim_id)

        print("Processed Sucessfully")
        

    finally:
        print("Completed this Claim ID")


print("SUMMARY")
print("Total claims attempted:", len(claims))
print("Processed:", len(processed_list))
print("Skipped:", len(skipped_list))
print("Errors:", len(error_list))

print("\nSkipped list:")
for s in skipped_list:
    print(s)

print("\nErrors list:")
for e in error_list:
    print(e)

print("\nSample processed rows:")
for p in processed_list[:3]:
    print(p)

print("\nInvalid types captured:", missed_types)



"""
SAMPLE OUTPUT

Running the row 0
Skipped Due to error : Amount is not Numeric
Completed this Claim ID
Running the row 1
Skipped Due to error : Amount is not Numeric
Completed this Claim ID
Running the row 2
Skipped Due to error : Missing or None Fiels claim_id
Completed this Claim ID
Running the row 3
Skipped Due to error : Amount is not Numeric
Completed this Claim ID
Running the row 4
Unexpected error : <class 'type'>
Completed this Claim ID
Running the row 5
Skipped Due to error : Amount is not Numeric
Completed this Claim ID
Running the row 6
Skipped Due to error : Amount is not Numeric
Completed this Claim ID
Running the row 7
Skipped Due to error : Roaw does not have 5 fields
Completed this Claim ID
Running the row 8
Skipped Due to error : Amount is not Numeric
Completed this Claim ID
Running the row 9
Skipped Due to error : Amount is not Numeric
Completed this Claim ID
SUMMARY
Total claims attempted: 10
Processed: 0
Skipped: 9
Errors: 1

Skipped list:
{'claim': 'C1001', 'reason': 'Amount is not Numeric'}
{'claim': 'C1002', 'reason': 'Amount is not Numeric'}
{'claim': None, 'reason': 'Missing or None Fiels claim_id'}
{'claim': 'C1003', 'reason': 'Amount is not Numeric'}
{'claim': 'C1001', 'reason': 'Amount is not Numeric'}
{'claim': 'C1005', 'reason': 'Amount is not Numeric'}
{'claim': 'index-7', 'reason': 'Roaw does not have 5 fields'}
{'claim': 'C1006', 'reason': 'Amount is not Numeric'}
{'claim': 'C1007', 'reason': 'Amount is not Numeric'}

Errors list:
<class 'type'>

Sample processed rows:

Invalid types captured: ['Gifts']
"""