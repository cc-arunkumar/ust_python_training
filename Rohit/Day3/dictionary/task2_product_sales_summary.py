from random import sample


sales = [
 ("Laptop", 3),
 ("Mobile", 5),
 ("Tablet", 2),
 ("Mobile", 4),
 ("Laptop", 1)
]

sales_summary = dict()
for item in sales:
    first, second = item
    if first in sales_summary:
        sales_summary[first] += second
    else:
        sales_summary[first] = second

print(sales_summary)

min=-1
name =''
for item in sales_summary:
    print(item)
    val = sales_summary.get(item)
    if min<val:
        min=val
        name=item


print(min," ", name)

# ============= sample output=============================
# {'Laptop': 4, 'Mobile': 9, 'Tablet': 2}
# Laptop
# Mobile
# Tablet
# 9   Mobile