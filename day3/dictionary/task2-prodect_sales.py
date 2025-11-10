# Task 2: Product Sales Summary
sales = [
 ("Laptop", 3),
 ("Mobile", 5),
 ("Tablet", 2),
 ("Mobile", 4),
 ("Laptop", 1)
]


sales_summary={}
for key,val in sales:
    if key in sales_summary:
        sales_summary[key]+=val
    else:
        sales_summary[key]=val

maximum=0
for key,value in sales_summary.items():
    print(f"{key}->{val}")

    if value>maximum:
        max=value
        name=key
print("Hightest selling product: ",name) 

# sample output
# Laptop->1
# Mobile->1
# Tablet->1
# Hightest selling product:  Tablet





# max_product = max(total, key=tot/oduct} ({total[max_product]})")

    
 