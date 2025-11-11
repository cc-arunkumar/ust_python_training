# Task 2: Product Sales Summary

sales = [
 ("Laptop", 3),
 ("Mobile", 5),
 ("Tablet", 2),
 ("Mobile", 4),
 ("Laptop", 1)
]

sales_summary={}
for key,val in sales:
    if key in sales_summary:
        sales_summary[key]+=val
    else:
        sales_summary[key]=val
max=0
for key,val in sales_summary.items():
    print(f"{key}->{val}")

    if val>max:
        max=val
        name=key
print("Hightest selling product: ",name) 

# Sample output

# Laptop->4
# Mobile->9
# Tablet->2

# Hightest selling product: Mobile

