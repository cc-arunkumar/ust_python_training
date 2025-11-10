#Task 2: Product Sales Summary
sales = [
 ("Laptop", 3),
 ("Mobile", 5),
 ("Tablet", 2),
 ("Mobile", 4),
 ("Laptop", 1)
]
sales_summary={}
max=0
name=""
for(str,n) in sales:
    if(max<n):
        name=str
        max=n
    print(str,"->",n)

print("Highest Selling product: ",name,"->",max)

#Sample output
# Laptop -> 3
# Mobile -> 5
# Tablet -> 2
# Mobile -> 4
# Laptop -> 1
# Highest Selling product:  Mobile -> 5