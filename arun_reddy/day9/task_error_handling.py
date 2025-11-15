#Error Handling Task
# Employee Expense Claim Processor (UST)
# Context
# UST employees submit expense claims (travel, meals, accommodation). You must
# write a small processor that validates claims, computes per-day cost for multi-day
# claims, detects duplicates, and never crashes the batch when some claims are
# bad.
# This focuses on exception handling: built-in exceptions and a few custom ones.
# Use try/except/else/finally and keep the code easy to follow.
claims = [
 {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"},
 {"claim_id": "C1002", "employee": "Riya", "type": "Meals", "amount": "abc", "days": "1"},
 {"claim_id": None, "employee": "Kiran", "type": "Accommodation", "amount": "4000", "days": "2"},
 {"claim_id": "C1003", "employee": "Mona", "type": "Travel", "amount": "900", "days": "0"},
 {"claim_id": "C1004", "employee": "John", "type": "Gifts", "amount": "200", "days": "1"},
 {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"}, # duplicate
 {"claim_id": "C1005", "employee": "Nisha", "type": "Meals", "amount": "1200", "days": "2"},
 {"employee": "Ravi", "type": "Travel", "amount": "700", "days": "1"}, # missing claim_id
 {"claim_id": "C1006", "employee": "Sona", "type": "Accommodation", "amoErunt": "3000", "days": "two"}, # days invalid
 {"claim_id": "C1007", "employee": "Anil", "type": "Travel", "amount": "0", "days": "1"},
]
class MissingFieldsError(Exception):
    pass
class InvalidFieldsError(Exception):
    pass
class DuplicateClaimError(Exception):
    pass
errorlist=[]
skippedlist=[]
processedlist={}
types=["accomodation","meals","travel"]
# declaring the required fields
requiredfields=["claim_id","employee","type","amount","days"]
#iterating over the claims 
for items in claims:
    try:
        # checking if evryfiled is present in the required fields
        for req in requiredfields:
            if req not in items or items[req]==None or items[req]=="":
                raise MissingFieldsError()
        if items["type"].lower() not in types:
            raise InvalidFieldsError()
        if items["days"].isdigit()==False:
            raise InvalidFieldsError()      
        if items["days"]=="0":
            raise ZeroDivisionError()
        if items["amount"]=="0":
            print("Warning......") 
        items["amount"]=float(items["amount"])
        if processedlist.get(items["claim_id"]):
            raise DuplicateClaimError()
    except MissingFieldsError as mfe:
        skippedlist.append([items,mfe])
    except InvalidFieldsError as ife:
        skippedlist.append([items,ife])
    except ZeroDivisionError as zde:
        errorlist.append([items,zde])
    except DuplicateClaimError as dce:
        skippedlist.append([items,dce])
    except ValueError as ve:
        errorlist.append(items)
    except TypeError as te:
        errorlist.append(items)
    except Exception as e:
        errorlist.append(e)
    else:
        processedlist[items["claim_id"]]=[items["employee"],items["type"],float(items["amount"]),int(items["days"])]
    finally:
        print("The claim is Evaluated....")
            
print(f"The total claims of the data:{len(claims)}")
print("The proccessedlsit of teh data is ........")
for item,value in processedlist.items():
    print(f"{item} {value}")
print("========================================================")
print(f"Th elength of teh proccessed list :{len(processedlist)}")
print("The skippedlist of teh data with misssing fields...")
for item in skippedlist:
    print(item)
print(f"the skipped list is {len(skippedlist)}")
print("========================================================")
print(f"The error list is")
for i in errorlist:
    print(i)


# sample execution
# The claim is Evaluated....
# The claim is Evaluated....
# The claim is Evaluated....
# The claim is Evaluated....
# The claim is Evaluated....
# The claim is Evaluated....
# The claim is Evaluated....
# Warning......
# The claim is Evaluated....
# The total claims of the data:10
# The proccessedlsit of teh data is ........
# C1001 ['Arun', 'Travel', 1500.0, 3]
# C1005 ['Nisha', 'Meals', 1200.0, 2]
# C1007 ['Anil', 'Travel', 0.0, 1]
# ========================================================
# Th elength of teh proccessed list :3
# The skippedlist of teh data with misssing fields...
# [{'claim_id': None, 'employee': 'Kiran', 'type': 'Accommodation', 'amount': '4000', 'days': '2'}, MissingFieldsError()]
# [{'claim_id': 'C1004', 'employee': 'John', 'type': 'Gifts', 'amount': '200', 'days': '1'}, InvalidFieldsError()]
# [{'claim_id': 'C1001', 'employee': 'Arun', 'type': 'Travel', 'amount': 1500.0, 'days': '3'}, DuplicateClaimError()]
# [{'employee': 'Ravi', 'type': 'Travel', 'amount': '700', 'days': '1'}, MissingFieldsError()]
# [{'claim_id': 'C1006', 'employee': 'Sona', 'type': 'Accommodation', 'amoErunt': '3000', 'days': 'two'}, MissingFieldsError()]
# the skipped list is 5
# ========================================================
# The error list is
# {'claim_id': 'C1002', 'employee': 'Riya', 'type': 'Meals', 'amount': 'abc', 'days': '1'}
# [{'claim_id': 'C1003', 'employee': 'Mona', 'type': 'Travel', 'amount': '900', 'days': '0'}, ZeroDivisionError()]
