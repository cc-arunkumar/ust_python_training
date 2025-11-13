sales_data = (
 ("Chennai", 85000),
 ("Bangalore", 92000),
 ("Hyderabad", 78000),
 ("Pune", 102000),
 ("Delhi", 98000)
)

# Print all branches with sales above ₹90,000.

for branch_name, total_sales_amount in sales_data:
    if total_sales_amount>90000:
        print("sales above 90000",branch_name)

#  Find the average sales across all branches.

total_sales=0
length=len(sales_data)
for branch_name, total_sales_amount in sales_data:
    total_sales+=total_sales_amount

    avg=total_sales/length

print("average sales:",avg)

# dentify and print the branch with the lowest sales
sales=float('inf')
name=""

for branch_name,total_sales_amount in sales_data:
    if total_sales_amount<sales:
        sales=total_sales_amount
        name=branch_name
        print(f"name and sales of lowest branch:{branch_name},{sales}")





# . Convert this tuple data into a list of tuples and update Pune’s sales to 105000 ,
# then convert it back to a tuple and print the updated data.

new_list=list(sales_data)
for i in range(len(new_list)):
    if new_list[i][0] == "Pune":
        new_list[i] = ("Pune", 105000)

print("After changing the pune sales:",new_list)



# sample output
# sales above 90000 Bangalore
# sales above 90000 Pune
# sales above 90000 Delhi
# average sales: 91000.0
# name and sales of lowest branch:Chennai,85000
# name and sales of lowest branch:Hyderabad,78000
# After changing the pune sales: [('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000)]












# lowest_branch = min(sales_data, key=lambda x: x[1])
# print("\nBranch with the lowest sales:", lowest_branch[0], "with ₹", lowest_branch[1])


