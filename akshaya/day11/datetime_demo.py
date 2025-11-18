# import datetime
from datetime import date
today=date.today()
print(today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
print("Weekday:", today.weekday())
# custom_date = date(2025, 11, 17)
# print(custom_date)



from datetime import timedelta
from datetime import date

today = date.today()

christmas_date = date(2025, 12, 25)

diff = christmas_date - today
valid_days_count = 0
current_date = today
while current_date <= christmas_date:
    if current_date.weekday() !=6:
        valid_days_count += 1
    current_date += timedelta(days=1)
    print(valid_days_count)


print(today.strftime("%d-%m-%Y"))
print(today.strftime("%d-%m-%y"))
print(today.strftime("%d-%mon-%Y"))
print(today.strftime("%A %d %B %Y"))
print(today.strftime("%A %d %B %y"))
print(today.strftime("%A %d %m %Y"))

days = []
for i in range(10):
    current_date = today+ timedelta(days=i)
    weekday_name = current_date.strftime("%A") 
    weekday_number = current_date.weekday() 
    days.append([current_date.strftime("%d/%m/%y"), weekday_name, weekday_number])
for day in days:
    print(day)

