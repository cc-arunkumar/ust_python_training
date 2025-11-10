# (branch_name, total_sales_amount
sales_data = (
 ("Chennai", 85000),
 ("Bangalore", 92000),
 ("Hyderabad", 78000),
 ("Pune", 102000),
 ("Delhi", 98000)
)
sum=0 
length=len(sales_data)
for branch,amount in sales_data:
    sum+=amount
    if amount>90000:
        print("sales above 90000",branch)
print(f"Average value: {sum/length:.2f}")
mn=float('inf') # taking the highest values
nme=""
for branch,amount in sales_data:
    if amount<mn:
        mn=amount
        nme=branch
print("The least amount branch :",nme)

newlist=list(sales_data) # converting into list 
for i in range(len(newlist)):
    if newlist[i][0]=="Pune":
        newlist[i]=("Pune",10500) # changing the Pune branch amount
print(newlist)
newtuple=tuple(newlist) # converting into tuple 
print(newtuple)

# ///sample execution 
# sales above 90000 Bangalore
# sales above 90000 Pune
# sales above 90000 Delhi
# Average value: 91000.0
# The least amount branch : Hyderabad
# [('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 10500), ('Delhi', 98000)]       
# (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 10500), ('Delhi', 98000))  
