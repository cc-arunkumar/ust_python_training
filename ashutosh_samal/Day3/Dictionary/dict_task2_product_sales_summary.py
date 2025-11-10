#Task 2: Product Sales Summary

sales = [("Laptop", 3),("Mobile", 5),("Tablet", 2),("Mobile", 4),("Laptop", 1)]
sales_summary={}

for product,quantity in sales:
    sales_summary[product]= sales_summary.get(product, 0) + quantity

for product,quantity in sales_summary.items():
    print(f"{product}→{quantity}")

highest_sell_prod = max(sales_summary.items(),key=lambda x:x[1])
print(f"Highest selling product is: {highest_sell_prod[0]} and {highest_sell_prod[1]} quantity")


#Sample Execution
# Laptop→4
# Mobile→9
# Tablet→2
# Highest selling product is: Mobile and 9 quantity