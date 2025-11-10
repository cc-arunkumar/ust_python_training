# Task 2: Product Sales Summary


sales = [
 ("Laptop", 3),
 ("Mobile", 5),
 ("Tablet", 2),
 ("Mobile", 4),
 ("Laptop", 1)
]

sales_summary={}

for product, quantity in sales:
    if product in sales_summary:
        sales_summary[product]+=quantity
    else:
        sales_summary[product]=quantity

max_value=0
max_key="Laptop"

for key,value in sales_summary.items():
    if value>max_value:
        max_value=value
        max_key=key

    print(f"{key}->{value}")

print(f"The highest selling product is:{max_key}->{max_value}")

# EXPECTED OUTPUT:
# Laptop->4
# Mobile->9
# Tablet->2
# The highest selling product is:Mobile->9
