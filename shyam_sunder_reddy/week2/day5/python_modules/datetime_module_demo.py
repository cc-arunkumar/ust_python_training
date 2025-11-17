import datetime
from datetime import date
from datetime import timedelta

# print("Today :",date.today())
# print("Today :",date.today().year)
# print("Today :",date.today().month)
# print("Today :",date.today().day)
# print(date.today().weekday())
# d=date(2027,9,17)
# print(d)
# print(d.weekday())

#Sample output
# Today : 2025-11-17
# Today : 2025
# Today : 11
# Today : 17
# 0
# 2027-09-17
# 4

# d=date.today()
# print("Today",d)
# print("Future",d+timedelta(days=10))
# print("past",d+timedelta(days=-10))

# ld=date(2025,12,25)
# td=date.today()
# x=0
# y=0
# while(td<ld):
#     if(td.weekday()!=6):
#         x+=1
#     else:
#         print("sunday:",td)
#         y+=1 
#     td+=timedelta(days=1)
# print("total working days :",x,"sundays :",y)

# today=date.today()
# print(today.strftime("%d-%m-%y"))
# print(today.strftime("%D"))
# print(today.strftime("%A,%d %B %Y"))
# print(today.strftime("%d %B %Y"))

today=date.today()
x=0
while(x<10):
    print(f"{today.strftime("%D")},{today.strftime("%A")} : {today.weekday()}")
    today+=timedelta(days=1)
    x+=1
    