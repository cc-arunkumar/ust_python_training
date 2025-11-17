# import datetime

# # date1=datetime.date.today()
# # print(date1)

# # print(date1.weekday())

# custom_date=datetime.date(2025,11,19)
# print(custom_date)
import datetime

today = datetime.date.today()
ten_days_data = today + datetime.timedelta(days=10)

print(ten_days_data)

day=datetime.date(2025,9,22)
print(day)

# day=datetime.day(22)
# print(day)

import datetime

today = datetime.date.today()
christmas = datetime.date(today.year, 12, 25)
days_until_christmas = (christmas - today).days

print(f"Days until Christmas: {days_until_christmas}")

counter = 0

for i in range(days_until_christmas):
    current_day = today + datetime.timedelta(days=i)
    if current_day.weekday() != 6:
        counter += 1  
print(counter)

print(today.strftime("%d-%m-%Y"))       
print(today.strftime("%d-%m-%y"))
# print(today.strftime("%d-%M-%y"))
# print(today.strftime("%d-%mon-%y"))
# print(today.strftime("%d-%Mon-%y"))

print(today.strftime("%A, %d %B %Y"))
print(today.strftime("%A, %d %m %Y"))
print(today.strftime("%d %B %Y"))

# day=["moday","tuesday","wednesday","thursday","friday","satarday","sunday"]

import datetime

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
today = datetime.date.today()

for i in range(10):  # next 10 days
    current_day = today + datetime.timedelta(days=i)
    print(f"{current_day.strftime('%d/%b/%y')}, {days[current_day.weekday()]}")
    
    
    
    
    
    