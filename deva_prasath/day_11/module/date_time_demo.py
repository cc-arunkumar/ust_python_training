# import datetime #explicit
from datetime import date #implicit
from datetime import timedelta
today=date.today()
print("Today date:",today)
print("Today year:",today.year)
print("Today month:",today.month)
print("Today day:",today.day)
print("Today weekday:",today.weekday())
cus=date(2025,11,20)  #custom date format changes
print("Custom date",cus)


ten_days_later=today+timedelta(days=10)
print("Ten days Later:",ten_days_later)

ten_days_prev=today-timedelta(days=10)
print("Ten days previous:",ten_days_prev)

last_date=date(2025,12,25)
diff=last_date-today
print("Difference of days from christmas to today:",diff)




count = 0
for i in range(diff.days):
    current_day=today+timedelta(days=i)
    if current_day.weekday()!=6:  
        count += 1

print(f"Number of days excluding Sundays: {count}")

print(today.strftime("%d-%m-%y"))
print(today.strftime("%A,%d,%B,%Y"))
print(today.strftime("%A,%d,%m,%Y"))

print(today.strftime("%d,%m,%Y"))


for i in range(10):
    ten_days=today+timedelta(days=i)
    print(ten_days.strftime("%d-%m-%y"),ten_days.strftime("%A"),ten_days.weekday())
    
