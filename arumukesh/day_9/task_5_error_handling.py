class InvalidExpenseTypeError(Exception):
    pass
class MissingFieldError(Exception):
    pass
class DuplicateClaimError(Exception):
    pass



processed_rows=[]
skipped_rows={}

claims = [
 {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"},
 {"claim_id": "C1002", "employee": "Riya", "type": "Meals", "amount": "abc", "days": "1"},
 {"claim_id": None, "employee": "Kiran", "type": "Accommodation", "amount": "4000", "days": "2"},
 {"claim_id": "C1003", "employee": "Mona", "type": "Travel", "amount": "900", "days": "0"},
 {"claim_id": "C1004", "employee": "John", "type": "Gifts", "amount": "200", "days": "1"},
 {"claim_id": "C1001", "employee": "Arun", "type": "Travel", "amount": "1500", "days": "3"},
 {"claim_id": "C1005", "employee": "Nisha", "type": "Meals", "amount": "1200", "days": "2"},
 {"employee":"Ravi", "type": "Travel", "amount": "700", "days": "1"},
 {"claim_id": "C1006", "employee": "Sona", "type": "Accommodation", "amount": "3000", "days": "two"},
 {"claim_id": "C1007", "employee": "Anil", "type": "Travel", "amount": "0", "days": "1"},
]
required_fields=["claim_id","employee","type","days"]
valid_types=["Travel", "Meals", "Accommodation"]
error_list=[]
c=0

try:
    for data in claims:
        try:

            # handling the missing fields
            for key,value in data.items():
                if key not in required_fields or value==None or value.strip():
                    raise MissingFieldError(f"Missing field{key}")
            # handling invalid types
            if data["type"] not in valid_types:
                raise InvalidExpenseTypeError("Not entered valid expense")
            # converting the amount to float,if string , ValueError will be raised automaticlly
            data["amount"]=float(data["amount"])
            data["days"]=int(data["days"])
            # Handling ZeroDivisionError explicitly
            if data["days"]<1:
                raise ZeroDivisionError("Enter valid day value")
            # Only alerting the user in case of 0 amount
            if data["amount"]==0:
                print(f"{data["claim_id"]} has enter a zero amount" )
            if data["claim_id"] in processed_rows:
                raise DuplicateClaimError("Duplicate claim_id found")

            processed_rows[data["claim_id"]] = data
        
                

            
    #   handling all the raised exceptions   
        except InvalidExpenseTypeError as e:
            row_key = data.get("claim_id", f"ROW_{c}")
            skipped_rows[row_key] = str(e)
        except MissingFieldError as e:
            row_key = data.get("claim_id", f"ROW_{c}")
            skipped_rows[row_key] = str(e)
        except ZeroDivisionError as e:
            row_key = data.get("claim_id", f"ROW_{c}")
            skipped_rows[row_key] = str(e)
        except ValueError as e:
            row_key = data.get("claim_id", f"ROW_{c}")
            skipped_rows[row_key] = str(e)
        except DuplicateClaimError as e:
            row_key = data.get("claim_id", f"ROW_{c}")
            skipped_rows[row_key] = str(e)

        except Exception:
            row_key = data.get("claim_id", f"ROW_{c}")
            skipped_rows[row_key] = "Unknown exception"
            error_list.append(row_key)
        finally:
            c+=1
    
finally:
    print(skipped_rows)
    print(processed_rows)
    print("Number of processed rows",c)
    print("number of skipped rows:",len(skipped_rows))



        
# ======Output====        
        

# {'C1001': 'Missing fieldclaim_id', 'C1002': 'Missing fieldclaim_id', None: 'Missing fieldclaim_id', 'C1003': 'Missing fieldclaim_id', 'C1004': 'Missing fieldclaim_id', 'C1005': 'Missing fieldclaim_id', 'ROW_7': 'Missing fieldemployee', 'C1006': 'Missing fieldclaim_id', 'C1007': 'Missing fieldclaim_id'}
# []
# Number of processed rows 10
# number of skipped rows: 9