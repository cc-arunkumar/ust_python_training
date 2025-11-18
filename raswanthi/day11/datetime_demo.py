# import datetime                          #explicit
from datetime import date                #implicit
from datetime import timedelta

today=date.today()
print(today)     #YYYY-MM-DD

# print(today.day)
# print(today.year)
# print(today.month)
# print(today.weekday())

# custom_date=date(2024,12,15)
# print(custom_date)

# print(today.day)
# print(today.year)
# print(today.month)
# print(today.weekday())

ten_Days_later=today+timedelta(days=10)
print("Ten days later",ten_Days_later)

five_days_back=today-timedelta(days=5)
print("Five days back",five_days_back)

random_date=date(2025,9,22)
ten_Days_later_random_date=random_date+timedelta(days=10)
print(ten_Days_later_random_date)

christmas = date(today.year, 12, 25)

current_day = today
days_count=0
while current_day < christmas:
    if current_day.weekday() != 6:   
        days_count+=1
    current_day += timedelta(days=1)
    
print(days_count)
print(today.strftime("%d-%m-%Y"))
print(today.strftime("%d-%Mon-%Y"))

print(today.strftime("%A, %d %B %Y"))
print(today.strftime("%A, %d %m %Y"))
print(today.strftime("%d %m %Y"))


for i in range(10):
    current = today + timedelta(days = i)
    format=current.strftime("%d-%m-%Y")      
    day_name = current.strftime("%A")                 
    weekday_num = current.weekday() 
    print(f"{format} - {day_name} - {weekday_num}")