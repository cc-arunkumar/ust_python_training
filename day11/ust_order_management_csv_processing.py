import csv


class OrderRecord:
    validstates=["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
        "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
        "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
        "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
        "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
        "Uttar Pradesh", "Uttarakhand", "West Bengal"]
    def __init__(self,order_id,customer_name,state,product,quantity,price_per_unit,status):
        self.order_id=order_id
        self.customer_name=customer_name
        self.state=state
        self.product=product
        self.quantity=quantity
        self.price_per_unit=price_per_unit
        self.status=status
        
    def validate(self):
        #Checking quantity is positive
        if self.order_id.strip()=="" or self.customer_name.strip()=="" or self.state.strip()=="" or self.product.strip()=="" or self.quantity.strip()=="" or self.price_per_unit.strip()=="" or self.status.strip()=="":
            self.reason="Missing Values"
            return False
        
        #checking for quantity
        try:
            self.quantity=int(self.quantity)
            if self.quantity<=0:
                raise Exception
        except:
            self.reason="Invalid Quantity"
            return False
        
        #checking for price_per_unit
        try:
            self.price_per_unit=int(self.price_per_unit)
        except:
            self.reason="Invalid Price per Unit"
            return False
        if self.price_per_unit<0:
                self.price_per_unit=abs(self.price_per_unit)
        
        
        #checking for customer_name
        self.customer_name=self.customer_name.strip()
        if self.customer_name=="":
            self.reason="Invalid Customer Name"
            return False
        
        #checking for valid state
        if self.state not in OrderRecord.validstates:
            self.reason="Invalid State"
            return False
        
        #calculating total amount
        self.total_amount=self.quantity*self.price_per_unit
        
        #standardizing status
        self.status=self.status.strip().upper()
        
        return True
        
        
    
class OrderProcessor:
    processeddata=[]
    skippeddata=[]
    def reading(self):
        with open("orders_raw.csv","r") as file:
            dictreader=csv.DictReader(file)
            for row in dictreader:
                order=OrderRecord(row["order_id"],row["customer_name"],row["state"],row["product"],row["quantity"],row["price_per_unit"],row["status"])
                if order.validate(): 
                    record={
                        "order_id":order.order_id,
                        "customer_name":order.customer_name,
                        "state":order.state,
                        "product":order.product,
                        "quantity":order.quantity,
                        "price_per_unit":order.price_per_unit,
                        "total_amount":order.total_amount,
                        "status":order.status
                    }                  
                    OrderProcessor.processeddata.append(record)
                else:
                    record={
                        "order_id":order.order_id,
                        "customer_name":order.customer_name,
                        "state":order.state,
                        "product":order.product,
                        "quantity":order.quantity,
                        "price_per_unit":order.price_per_unit,
                        "status":order.status,
                        "error_reason":order.reason
                    }   
                    OrderProcessor.skippeddata.append(record)
    
        with open("orders_processed.csv","w",newline="") as file:
            headers=["order_id","customer_name","state","product","quantity","price_per_unit","total_amount","status"]
            writer=csv.DictWriter(file,fieldnames=headers)
            writer.writeheader()
            writer.writerows(OrderProcessor.processeddata)
        with open("orders_skipped.csv","w",newline="") as file:
            headers=["order_id","customer_name","state","product","quantity","price_per_unit","status","error_reason"]
            writer=csv.DictWriter(file,fieldnames=headers)
            writer.writeheader()
            
            writer.writerows(OrderProcessor.skippeddata)
        print("completed all operations") 
        print("*******************************************")
        print("skipper: ",len(OrderProcessor.skippeddata))
        print("Processed :",len(OrderProcessor.processeddata))
            
x=OrderProcessor()
x.reading()