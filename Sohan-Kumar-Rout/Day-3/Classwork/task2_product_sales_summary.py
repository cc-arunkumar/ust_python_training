#Task 2: Product Sales Summary

#Code 
sales = [
 ("Laptop", 3),
 ("Mobile", 5),
 ("Tablet", 2),
 ("Mobile", 4),
 ("Laptop", 1)
]

sales_summary={}
highest=0
highest_name=""
for product,quantity in sales:
    if product in sales_summary:
        sales_summary[product]+=quantity
    else:
        sales_summary[product]=quantity

for product , quantity in sales_summary.items():
    if(quantity>highest):
        highest=quantity
        highest_name=product
for product, quantity in sales_summary.items():
    print(f"{product} : {quantity}")
print(f"\nHighest Selling Product name: {highest_name} ({highest} units)")

#Output
# Laptop : 4
# Mobile : 9
# Tablet : 2
# Highest Selling Product name: Mobile (9 units)
        

