sales = [
 ("Laptop", 3),
 ("Mobile", 5),
 ("Tablet", 2),
 ("Mobile", 4),
 ("Laptop", 1)
]

sales_summary = {}

for i in sales:
    sales_summary[i[0]] = sales_summary.get(i[0],0) + i[1]

max = 0
item = ""
for i in sales_summary:
    print(f"{i} -> {sales_summary[i]}")
    if sales_summary[i] > max:
        max = sales_summary[i]
        item = i
print("highest selling product name: ",item)

# output

# Laptop -> 4
# Mobile -> 9
# Tablet -> 2
# highest selling product name:  Mobile