from datetime import date 
from datetime import timedelta


today=date.today()
print(today)

print("year:",today.year)
print("month:",today.month)
print(today.day)

print(today.weekday())
# today.date(yyyy,mm,dd)

ten_days_later=today+timedelta(days=10)
print(ten_days_later)

five_days_ago=today+timedelta(days=-5)
print(five_days_ago)


today = date.today()
last_day = date(2025, 12, 25)

count = 0
present = today

while present < last_day:
    if present.weekday() == 6:    
        count += 1
    present += timedelta(days=1)

total_days=last_day-today
print(total_days)
print("sunday:",count)


print(today.strftime("%d-%mon-%y"))
print(today.strftime("%d-%m-%y"))
print(today.strftime("%d-%Mon-%y"))

print(today.strftime("%A, %d %B %Y"))
print(today.strftime("%A, %d %B %y"))

print(today.strftime("%d %m %Y"))




# day=date(2025,9,01)--------->
print(day)

day=date(2025,9,1)
print(day)

7/11/2025-Monday-0

for i in range(0,10):
     c = today + timedelta(days=i)
    #  print(c)
     print(c.strftime(f"%d/%m/%Y-%A-{today.weekday()+i}"))


