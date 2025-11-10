# Assignment 3 — Online Order Fulfilment Report
# Scenario:
# UST’s e-commerce division tracks daily customer orders.


orders=[
("O1001","Neha","Bangalore","Laptop",2),
("O1002","Arjun","Chennai","Mobile",3),
("O1003","Ravi","Delhi","Laptop",1),
("O1004","Fatima","Bangalore","Tablet",2),
("O1005","Vikram","Mumbai","Mobile",5),
("O1006","Neha","Bangalore","Laptop",1)
]


order_ids=set()
product_qty={}
customer_total={}
cities=set()

for oid,cust,city,prod,qty in orders:
    if oid not in order_ids:
        order_ids.add(oid)
        product_qty[prod]=product_qty.get(prod,0)+qty
        customer_total[cust]=customer_total.get(cust,0)+qty
        cities.add(city)

print("Total Quantity per Product:",product_qty)
print("Unique Cities:",cities)

max_qty=max(customer_total.values())
top_customers=[c for c,q in customer_total.items() if q==max_qty]
print("Top Customers:",top_customers)

new_order=("O1007","Fatima","Delhi","Tablet",3)
oid,cust,city,prod,qty=new_order
if oid not in order_ids:
    order_ids.add(oid)
    product_qty[prod]=product_qty.get(prod,0)+qty
    customer_total[cust]=customer_total.get(cust,0)+qty
    cities.add(city)

print("Updated Product Totals:",product_qty)
print("Updated Top Customers:",[c for c,q in customer_total.items() if q==max(customer_total.values())])

# sample output:

# Total Quantity per Product: {'Laptop': 4, 'Mobile': 8, 'Tablet': 2}
# Unique Cities: {'Delhi', 'Mumbai', 'Bangalore', 'Chennai'}
# Top Customers: ['Vikram']
# Updated Product Totals: {'Laptop': 4, 'Mobile': 8, 'Tablet': 5}
# Updated Top Customers: ['Fatima', 'Vikram']