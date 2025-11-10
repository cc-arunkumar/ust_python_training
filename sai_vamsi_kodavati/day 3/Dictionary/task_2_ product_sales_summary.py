# TASK 2 -  Product Sales Summary

sales = [("Laptop", 3),("Mobile", 5),("Tablet", 2),("Mobile", 4),("Laptop", 1)]

sales_summary = {}

for product,quantity in sales:
    if product in sales_summary:
        sales_summary[product] += quantity
    else:
        sales_summary[product] = quantity

print(sales_summary)
    
print("Highest selling product:",max(sales_summary,key=sales_summary.get))

# --------------------------------------------------------------------------

# Sample Output
# {'Laptop': 4, 'Mobile': 9, 'Tablet': 2}
# Highest selling product: Mobile


