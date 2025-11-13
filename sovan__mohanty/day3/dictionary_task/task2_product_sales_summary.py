#Task 2: Product Sales Summary
sales = [
 ("Laptop", 3),
 ("Mobile", 5),
 ("Tablet", 2),
 ("Mobile", 4),
 ("Laptop", 1)
]
sales_summary = {}
sum_laptop=0
sum_mobile=0
sum_tablet=0
for tools,quantity in sales:
    if(tools=="Laptop"):
        sum_laptop=sum_laptop+quantity
    elif(tools=="Mobile"):
        sum_mobile=sum_mobile+quantity
    elif(tools=="Tablet"):
        sum_tablet=sum_tablet+quantity
print("Laptop---->",sum_laptop)
print("Mobile--->",sum_mobile)
print("Tablet---->",sum_tablet)
high=0
if(sum_laptop>high):
    high=sum_laptop
if(sum_mobile>high):
    high=sum_mobile
if(sum_tablet>high):
    high=sum_tablet
if(high==sum_laptop):
    print("Highest product selling is Laptop: ",high)
elif(high==sum_mobile):
    print("Highest product selling is Mobile: ",high)
else:
    print("Highest product selling is Tablet: ",high)

#Sample Executions
# Laptop----> 4
# Mobile---> 9
# Tablet----> 2
# Highest product selling is Mobile:  9


