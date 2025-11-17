import os,csv,datetime,math

current_path = "C:/Users/Administrator/Desktop/ust_python_training-1/felix/day-11/ust_order_processing"

if os.path.exists(current_path):
    print("ust_order_processing Diarectory already exists")
else:
    os.mkdir(current_path)
    print("ust_order_processing created")
    

input = "input"
input_path = os.path.join(current_path,input)
if os.path.exists(input_path):
    print("input Diarectory already exists")
else:
    os.mkdir(input_path)
    print("input Diarectory created")
    
output = "output"
output_path = os.path.join(current_path,output)
if os.path.exists(output_path):
    print("output Diarectory already exists")
else:
    os.mkdir(output_path)
    print("output Diarectory created")
    
in_file = "orders.csv"
input_file = os.path.join(input_path,in_file)

processed_path = "processed.csv"
skipped_path = "skipped.csv"
if os.path.exists(os.path.join(output_path,processed_path)):
    print("processed.csv already exist")
else:
    with open(os.path.join(output_path,processed_path),"w") as file:
        pass
    
if os.path.exists(os.path.join(output_path,skipped_path)):
    print("skipped.csv already exist")
else:
    with open(os.path.join(output_path,skipped_path),"w") as file:
        pass
    
logs_path = os.path.join(current_path,"logs")
if os.path.exists(logs_path):
    print("logs Diarectory already exists")
else:
    os.mkdir(logs_path)
    print("logs created")
    
excicution_log = os.path.join(logs_path,"excicution_log.txt")
if os.path.exists(excicution_log):
    print("excicution_log.txt already exist")
else:
    with open(excicution_log,"w") as file:
        pass
    
skipped = 0
processed = 0




class QuantityError(Exception):
    pass
class UnitPriceError(Exception):
    pass
class DateInvalidError(Exception):
    pass
class DateInFutureError(Exception):
    pass




with open(input_file,"r") as file:
    data = csv.DictReader(file)
    header = data.fieldnames
    for item in data:
        try:
            if int(item["quantity"])<=0:
                raise QuantityError
            
            if int(item["unit_price"])<=0:
                raise UnitPriceError
            
            if datetime.date.fromisoformat(item["order_date"]):
                today = datetime.date.today()
                
                if datetime.date.strptime(item["order_date"],"%Y-%m-%d")>today:
                    raise Exception
                
            order_date = datetime.date.strptime(item["order_date"],"%Y-%m-%d")

            total_cost = math.ceil(int(item["quantity"]) * int(item["unit_price"]))
            item["total_cost"] = total_cost

            
            
            delivery_date = order_date + datetime.timedelta(5)
            
            if delivery_date.weekday() == 6:
                delivery_date = order_date + datetime.timedelta(1)
            item["delivery_date"] = delivery_date
                
            
        except QuantityError as q:
            skipped += 1
            with open(os.path.join(output_path,skipped_path),"a",newline="") as file:
                writer = csv.writer(file)
                writer.writerow(item.values())
            with open(excicution_log,"a",newline="") as file:
                file.writelines(f"{datetime.date.today()} Warning: quantity less than Zero\n")
            
                
        except UnitPriceError as u:
            skipped += 1
            with open(os.path.join(output_path,skipped_path),"a",newline="") as file:
                writer = csv.writer(file)
                writer.writerow(item.values())
            with open(excicution_log,"a",newline="") as file:
                file.writelines(f"{datetime.date.today()} Warning: unit price must be greater than zero\n")
                
        except ValueError as v:
            skipped += 1
            with open(os.path.join(output_path,skipped_path),"a",newline="") as file:
                writer = csv.writer(file)
                writer.writerow(item.values())
            with open(excicution_log,"a",newline="") as file:
                file.writelines(f"{datetime.date.today()} Warning: {v}\n")
                
        except Exception as e:
            skipped += 1
            with open(os.path.join(output_path,skipped_path),"a",newline="") as file:
                writer = csv.writer(file)
                writer.writerow(item.values())
            with open(excicution_log,"a",newline="") as file:
                file.writelines(f"{datetime.date.today()} Warning: {e}\n")
                
        else:
            processed += 1
            with open(os.path.join(output_path,processed_path),"a",newline="") as file:
                writer = csv.writer(file)
                writer.writerow(item.values())
            with open(excicution_log,"a",newline="") as file:
                file.writelines(f"{datetime.date.today()} INFO order {item["order_id"]} processed successfully\n")
                
print(skipped,processed)