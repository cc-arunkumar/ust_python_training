sales = [
 ("Laptop", 3),
 ("Mobile", 5),
 ("Tablet", 2),
 ("Mobile", 4),
 ("Laptop", 1)
]
sales_summary = {}
for product, quantity in sales:
    sales_summary[product] = sales_summary.get(product, 0) + quantity
print(sales_summary)

for product, quantity in sales_summary.items():
    print(f"{product} -> {quantity}")

max = 0
for product, quantity in sales_summary.items():
    if quantity > max:
        max = quantity
print(max)



