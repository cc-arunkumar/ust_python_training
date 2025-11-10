#Task 2: Sales Record Analyzer

#Code
sales_data=(
    ("Chennai",85000),
    ("Banglore",92000),
    ("Hyderabad", 78000),
    ("Pune", 102000),
    ("Delhi", 98000)
)
sum=0
count=0
lowest = 0  
lowest_branch = ""

for branch_name, total_sales_amount in sales_data:
    if(total_sales_amount>90000):
        print("Branches above 90,000 are : ",branch_name)
        sum+=total_sales_amount
        count+=1
avg_sales = sum/count
print("Total Avg : ",avg_sales)
for branch_name, total_sales_amount in sales_data:
    if(total_sales_amount<lowest):
        lowest = total_sales_amount
        lowest_branch=branch_name
        print(lowest)

#Converting tuple to sales 
sales_list = list(sales_data)
for i in range(len(sales_list)):
    if sales_list[i][0] == "Pune":
        sales_list[i] = ("Pune", 105000)
        break

sales_data = tuple(sales_list)
print("Updated Sales Data:", sales_data)

# #Sample Output
# Branches above 90,000 are :  Banglore
# Branches above 90,000 are :  Pune
# Branches above 90,000 are :  Delhi
# Total Avg :  97333.33333333333
# Updated Sales Data: (('Chennai', 85000), ('Banglore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))



    
