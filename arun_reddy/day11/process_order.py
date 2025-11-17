import csv
processedlist=[]
skippedlist=[]
valid_states= [
    "andhra pradesh",
    "arunachal pradesh",
    "assam",
    "bihar",
    "chhattisgarh",
    "goa",
    "gujarat",
    "haryana",
    "himachal pradesh",
    "jharkhand",
    "karnataka",
    "kerala",
    "madhya pradesh",
    "maharashtra",
    "manipur",
    "meghalaya",
    "mizoram",
    "nagaland",
    "odisha",
    "punjab",
    "rajasthan",
    "sikkim",
    "tamil nadu",
    "telangana",
    "tripura",
    "uttar pradesh",
    "uttarakhand",
    "west bengal"
]
required_fields=["order_id","customer_name","state","product","quantity","price_per_unit","status"]
validate=["SHIPPED","PENDING","CANCELLED","DELIVERED"]
class OrderRecord:
    def __init__(self,**kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)
    def validation(self):
        try:
            self.quantity=int(self.quantity)
            if int(self.quantity)==0:
                raise Exception
        except Exception as e:
            return [False,"Invalid quantity"]
        try:
           self.price_per_unit=int(self.price_per_unit)
           if int(self.price_per_unit)==0:
               raise Exception
           self.price_per_unit = abs(self.price_per_unit)
        except Exception:
            return [False,"Inavlid Price per unit"]
        if self.customer_name.strip()=='':
            return [False,"Invalid Customer Name"]
        if not self.state.lower() in valid_states:
            return [False,"Invalid state"]
        if self.status.upper() not in validate:
            return [False,"Invalid status"]
        
        return [True,"Valid"]

    
class OrderProcessor:
    def processing(self):
        with open("orders_raw.csv","r") as file:
            content=csv.DictReader(file)
            for row  in content:
                if '' in row.values():
                    row["reason"]="Empty Fields"
                    skippedlist.append(row)
                    continue
                orderrecord=OrderRecord(**row)
                flag,reason=orderrecord.validation()
                if flag:
                    row["totalcost"]=(int(row["quantity"])*(int(row["price_per_unit"])))
                    processedlist.append(row)
                else:
                    row["reason"]=reason
                    skippedlist.append(row)   

                      
                
                
order=OrderProcessor()    
order.processing()
with open("orders_processed.csv", "w", newline="") as file:
    # write processed rows using the expected headers
    headers = ["order_id", "customer_name", "state", "product", "quantity", "price_per_unit", "status"]
    content = csv.DictWriter(file, fieldnames=headers)
    content.writeheader()
    for row in processedlist:
        # ensure we pass a mapping matching the header names
        content.writerow({h: row.get(h, "") for h in headers})
with open("orders_skipped.csv","w",newline='') as file:
    headers = ["order_id", "customer_name", "state", "product", "quantity", "price_per_unit", "status","reason"]
    content = csv.DictWriter(file, fieldnames=headers)
    content.writeheader()
    for row in skippedlist:
        # ensure we pass a mapping matching the header names
        content.writerow({h: row.get(h, "") for h in headers})
    
print(len(skippedlist))
# 61
print(processedlist)
  
            