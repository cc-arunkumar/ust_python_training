sales = [
 ("Laptop", 3),
 ("Mobile", 5),
 ("Tablet", 2),
 ("Mobile", 4),
 ("Laptop", 1)
]

sales_summary = {}
high_sales = 0
highest_sales = ""

for key,val in sales:
    if key in sales_summary:
        sales_summary[key] += val
    else:
        sales_summary[key] =val

for key, val in sales_summary.items():
    print(f"{key} --> {val}")
    if val>high_sales:
        high_sales = val
        highest_sales = key
print(f"{highest_sales} is the highest sales with {high_sales}")

