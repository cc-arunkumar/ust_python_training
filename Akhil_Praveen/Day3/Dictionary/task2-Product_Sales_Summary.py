sales = [
 ("Laptop", 3),
 ("Mobile", 5),
 ("Tablet", 2),
 ("Mobile", 4),
 ("Laptop", 1)
]
sales_summary = {}
max_q=0
max_pr=""
for product, quantity in sales:
    if product in sales_summary:
        sales_summary[product]+=quantity
    else:
        sales_summary[product]=quantity
    if max_q<quantity:
        max_q=quantity
        max_pr=product
for i in sales_summary:
    print(f"{i} -> {sales_summary[i]}")

# Laptop -> 4
# Mobile -> 9
# Tablet -> 2