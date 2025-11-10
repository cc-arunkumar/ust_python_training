sales = [
 ("Laptop", 3),
 ("Mobile", 5),
 ("Tablet", 2),
 ("Mobile", 4),
 ("Laptop", 1)
]
sales_summary = {} 
for product, qty in sales:
 sales_summary[product] = sales_summary.get(product, 0) + qty
print(sales_summary)
for key,value in sales_summary.items():
    print(f"{key}-->{value}")

max_key = None
max_value = float('-inf')
for key, value in sales_summary.items():
    if value > max_value:
        max_value = value
        max_key = key

print("Highest Selling product name: ",max_key)


# {'Laptop': 4, 'Mobile': 9, 'Tablet': 2}
# Laptop-->4
# Mobile-->9
# Tablet-->2
# Highest Selling product name:  Mobile