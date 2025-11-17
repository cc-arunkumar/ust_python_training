from datetime import date,timedelta

# print(date.today().year)
# print(date.today().month)
# print(date.today().day)
# print(date.today().weekday())
# print(date(2002,8,21).weekday())
# print(date.today() + timedelta(days=10))
# print(date.today() - timedelta(days=5))
last_day = date(2025,12,25)
current_day = date.today()
# print(current_day.strftime("%d-%m-%y"))
# print(current_day.strftime("%A,%d %B %y"))
# count=0

# while True:
#     if(current_day==last_day):
#         break
#     if(current_day.weekday()!=6):
#         count+=1
#     current_day+=timedelta(days=1)
# print(count)
# L=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

# for i in range(11):
#     print(f"{current_day.strftime("%d/%m/%y")} : {L[current_day.weekday()]} : {current_day.weekday()}")
#     current_day+=timedelta(days=1)
da = "2025-01-34"
date.fromisoformat(da)