#Task 2: Product Sales Summary
sales = [
 ("Laptop", 3),
 ("Mobile", 5),
 ("Tablet", 2),
 ("Mobile", 4),
 ("Laptop", 1)
]

sales_summary = {}
for i in sales:
    if i[0] not in sales_summary.keys():
        sales_summary[i[0]]= i[1]
    else:
        val = sales_summary.get(i[0])
        sales_summary[i[0]] = val + i[1]

name=""
maxi=0
for j in list(sales_summary.items()):
    if maxi<j[1]:
        maxi=j[1]
        name=j[0]
    print(f"{j[0]} -> {j[1]}")

print("Highest:",name,"->",maxi)

#Sample Output
# Laptop -> 4
# Mobile -> 9
# Tablet -> 2
# Highest: Mobile -> 9