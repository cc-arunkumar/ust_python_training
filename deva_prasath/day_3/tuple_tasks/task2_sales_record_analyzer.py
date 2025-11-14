# Sales Record Analyzer

# Your company stores weekly sales data as tuples.


sales_data = (
 ("Chennai", 85000),
 ("Bangalore", 92000),
 ("Hyderabad", 78000),
 ("Pune", 102000),
 ("Delhi", 98000)
)


sum,count=0,0
for i,j in sales_data:
    if j>90000:
        print("Sales above 90000:",i)
    sum+=j
    count+=1

print("Average sales across all branches: ",(sum/count)*100)

lowest=sales_data[0]
for branch in sales_data:
    if branch[1]<lowest[1]:
        lowest=branch

print(f"Branch with the lowest sales: {lowest[0]}")
li1=list(sales_data)
for i in li1:
    li2=list(i)
    if li2[0]=="Pune":
        li2[1]=105000    
    print(tuple(li2))


#Sample output

# Sales above 90000: Bangalore
# Sales above 90000: Pune
# Sales above 90000: Delhi
# Average sales across all branches:  9100000.0
# Branch with the lowest sales: Hyderabad
# ('Chennai', 85000)
# ('Bangalore', 92000)
# ('Hyderabad', 78000)
# ('Pune', 105000)
# ('Delhi', 98000)