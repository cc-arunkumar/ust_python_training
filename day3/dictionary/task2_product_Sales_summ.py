sales = [
 ("Laptop", 3),
 ("Mobile", 5),
 ("Tablet", 2),
 ("Mobile", 4),
 ("Laptop", 1)
]

sales_summary={}
for product,quantity in sales:
    sales_summary[product] = sales_summary.get(product,0)+quantity

for product,quantity in sales_summary.items():
    print(f"{product}->{quantity}")

max_sale_product = max(sales_summary, key=sales_summary.get)
max_quantity = sales_summary[max_sale_product]

print(f"Maximum sales: {max_sale_product} -> {max_quantity}")

