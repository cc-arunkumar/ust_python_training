from datetime import date,timedelta
today=date.today()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)
# print(today.weekday())


custom_date = date(2025, 11, 18)
print("Custom date:",custom_date)
print("year:",custom_date.year)
print("month:",custom_date.month)
print("day:",custom_date.day)
print("weekday:",custom_date.weekday())


ten_days_later=today + timedelta(days=10)
print("Today + 10 days:",ten_days_later)

ten_days_earlier=today - timedelta(days=10)
print("Today - 10 days:",ten_days_earlier)

last_day=date(2025,12,25)
days_until_last_day=(last_day - today).days
print("Days until 25th Dec 2025:",days_until_last_day)

any_day=date(2025,9,2)
print("Any day:",any_day)

days_until_last_day=0
current_day = today
while current_day <= last_day:
    if current_day.weekday() != 6:  
        days_until_last_day += 1
    current_day += timedelta(days=1)
print("Working days until 25th Dec 2025:",days_until_last_day)

print(today.strftime("%d-%m-%Y"))
print(today.strftime("%Y"))
print(today.strftime("%mon"))
print(today.strftime("%d"))

print(today.strftime("%A, %d %B %y "))
print(today.strftime("%A, %d %m %y "))
print(today.strftime("%A  %m %y "))

for i in range(10):
    future_date = today + timedelta(days=i)
    print(future_date.strftime("%d/%m/%Y"),",", future_date.strftime("%A"),":", future_date.weekday())



