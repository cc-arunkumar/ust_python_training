#Task2: Sales Recorder Analyzer

sales_data = (
 ("Chennai", 85000),
 ("Bangalore", 92000),
 ("Hyderabad", 78000),
 ("Pune", 102000),
 ("Delhi", 98000)
)
mi=0
cout=0
for branch_name,total_sales_amount in sales_data:
    if(total_sales_amount>90000):
        print("Branches with sales amount above Rs90,000: ",branch_name)
    if(cout==0):
        if(total_sales_amount>mi):
            mi=total_sales_amount
            cout+=1
    else:
        if(total_sales_amount<mi):
            mi=total_sales_amount
            cout+=1



for branch_name,total_sales_amount in sales_data:
    if(mi==total_sales_amount):
        print("Branch with lowest sales amount: ",branch_name)
list2=list(sales_data)
for i, (branch_name, total_sales_amount) in enumerate(list2):
    if branch_name == "Pune":
        list2[i] = ("Pune", 105000)
        break
tuple2=tuple(list2)
print(tuple2)

# Sample Execution
# Branches with sales amount above Rs90,000:  Bangalore
# Branches with sales amount above Rs90,000:  Pune
# Branches with sales amount above Rs90,000:  Delhi
# Branch with lowest sales amount:  Hyderabad
# (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))