# product Sales Summary
sales = [("Laptop", 3),("Mobile", 5),("Tablet", 2),("Mobile", 4),("Laptop", 1)]

sales_summary = {}

for product, quantity in sales:
    if product in sales_summary:
        sales_summary[product] += quantity
    else:
        sales_summary[product] = quantity

for product, total_quantity in sales_summary.items():
    print(f"{product} -> {total_quantity}")

highest_selling = max(sales_summary.items(), key=lambda x: x[1])
print(f"\nHighest selling product: {highest_selling[0]} → {highest_selling[1]}")

# Laptop -> 4
# Mobile -> 9
# Tablet -> 2

# Highest selling product: Mobile → 9