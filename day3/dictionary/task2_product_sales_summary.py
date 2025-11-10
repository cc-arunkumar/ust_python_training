# Task 2: Product Sales Summary
# Scenario:
# You work in the Sales Analytics team.
# You receive a list of daily sales transactions — each as a tuple: (product, quantity) .

sales=[
("Laptop",3),
("Mobile",5),
("Tablet",2),
("Mobile",4),
("Laptop",1)
]
sales_summary={}
high_selling_key=0
high_selling_value=""

for key,value in sales:
    if key in sales_summary:
        sales_summary[key]+=value
    else:
        sales_summary[key]=value

for product,quantity in sales_summary.items():
    print(f"{product} → {quantity}")
    if quantity>high_selling_key:
        high_selling_key=quantity
        high_selling_value=product

print(f"Highest Selling Product : {high_selling_value}")

# sample output:

# Laptop → 4
# Mobile → 9
# Tablet → 2
# Highest Selling Product : Mobile