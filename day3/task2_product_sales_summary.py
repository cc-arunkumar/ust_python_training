#product sales summary

sales_analytics={"Laptop":3,"Mobile":5,"Tablet":2,"Mobile":4,"Laptop": 1}
sales_summary={}
for product,quantity in sales_analytics.items():
    print(product,"->",quantity)
for product,quantity in sales_analytics.items():
    highest_selling=max(sales_analytics,key=sales_analytics.get)
print("highest selling product name:",highest_selling)

#sample output
# Laptop -> 1
# Mobile -> 4
# Tablet -> 2
# highest selling product name: Mobile