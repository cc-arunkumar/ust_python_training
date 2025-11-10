sales = [
 ("Laptop", 3),
 ("Mobile", 5),
 ("Tablet", 2),
 ("Mobile", 4),
 ("Laptop", 1)
]
# Empty dictinary
sales_summary = {} 

for device,num in sales:
    if sales_summary.get(device):
        sales_summary[device]+=num
    else:
        sales_summary[device]=num

mxprice=0
name=""
for dev,nm in sales_summary.items():
    print(f"{dev}->{nm}")
    if nm>mxprice:
        mxprice=nm
        name=dev
print(f"{name}{mxprice}")

