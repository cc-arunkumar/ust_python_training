import csv 

#Validating Required Fields and Conversion of Bill Amounts to Float
with open('ust_healthcare_visits.csv','r') as file:
    li=[]
    csv_reader = csv.DictReader(file)
    value_types_for_payment = ["paid","pending","unpaid"]
    required_fields = ['patient_id','name','visit_date','billed_amount','payment_status']
    
    for row in csv_reader:
    
        if(row['patient_id']=="" or row['name']=="" or row['visit_date']=="" or row['billed_amount']=="" or row['payment_status']==""):
            print(f"Incomplete Details for the {row['patient_id']}")
            continue
            
        ld = {}
        for key,value in row.items():
            ##Removing Whitespaces for String Type
            if  isinstance(value,str):
                ld[key]=value.strip()
            else:
                ld[key] = value
                
            #Check for the Tile Case in 'payment_status'
            if key=="payment_status" and value in value_types_for_payment:
                ld[key] = value[0].upper() + value[1:]
            
            #Check for the Null Values in follow_up_required
            if key=='follow_up_required' and value=="":
                ld[key] = "No"
            
            if key=="follow_up_required" and value in ['yes','no']:
                if value=='yes':
                    ld[key] = "Yes"
                else:
                    ld[key] = "No"
        
        li.append(ld)
        
#Rewrite the Cleaned and Normalized Data into the csv file
with open('ust_healthcare_visits.csv','w',newline='') as file:
    
    header = ['patient_id','name','dob','gender','contact','provider_id','provider_name','department','visit_date','visit_type','diagnosis_codes','procedure_codes','billed_amount','insurance_provider','insurance_id','payment_status','discharge_date','follow_up_required','notes']
    csv_writer = csv.DictWriter(file, fieldnames=header)
    
    csv_writer.writeheader()
    
    csv_writer.writerows(li)  
        
        
with open('ust_healthcare_visits.csv','r') as file:
    csv_reader = csv.DictReader(file)
    pending_list = []    

    for row in csv_reader:
    
        if row['payment_status'] != "Paid":
            pending_list.append(row)

#Create A pending_payments.csv
with open("bigdata_pending_payments.csv",'w',newline="") as file:
    
    #create fieldnames list
    header = ['patient_id','name','dob','gender','contact','provider_id','provider_name','department','visit_date','visit_type','diagnosis_codes','procedure_codes','billed_amount','insurance_provider','insurance_id','payment_status','discharge_date','follow_up_required','notes']
    
    #Create Dictwriter Object
    csv_writer = csv.DictWriter(file,fieldnames=header)
    
    #Write fieldnames in Header
    csv_writer.writeheader()
    
    #Write all rows in csv file
    csv_writer.writerows(pending_list)

#To Generate Patient Summary CSV File

with open('ust_healthcare_visits.csv','r') as file:
    dict = {}
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        if row['patient_id'] not in dict.keys():
            li={}
            li['name'] = row['name']
            li['visits_count'] = 1
            li['billed_amount'] == float(row['billed_amount'])
            if row['payment_status'] != 'Paid':
                li['has_pending_status'] = True 
            else:
                li['has_pending_status']= False
                
            dict[row['patient_id']] = li 
        else:
            dict[row['patient_id']]['visits_count'] += 1 
            dict[row['patient_id']]['total_bill'] = dict.get(row['patient_id'])['total_bill'] + float(dict[row['patient_id']]['total_bill'])
            
            if dict[row['patient_id']]['has_pending_status'] or dict.get(row['patient_id']):
                dict[row['patient_id']]['has_pending_status'] = True 
    

li_dict = []
for key,value in dict.items():
    new_li = []
    new_li.append(key)
    for key1,value1 in value.items():
        new_li.append(value1)
    li_dict.append(new_li)


with open('bigdata_patient_summary.csv','w',newline="") as file:
    summary_header = ['patient_id','name','total_visits','total_billed','has_pending_payment']
    csv_write = csv.writer(file)
    csv_write.writerow(summary_header)
    csv_write.writerows(li_dict)
