#Task 2: Product Sales Summary
sales = [
 ("Laptop", 3),
 ("Mobile", 5),
 ("Tablet", 2),
 ("Mobile", 4),
 ("Laptop", 1)
]
sales_summary = {}
for name,qty in sales:
    if(name not in sales_summary):
        sales_summary[name]=0
    sales_summary[name]+=qty

maxi=0
maxi_name=''
for i in sales_summary:
    if(sales_summary.get(i)>maxi):
        maxi=sales_summary.get(i)
        maxi_name=i
    print(f"{i}->{sales_summary.get(i)}")

print(f"Max is : {maxi_name} , Qty : {maxi}")

#Output
# Laptop->4
# Mobile->9
# Tablet->2
# Max is : Mobile , Qty : 9


