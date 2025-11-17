import datetime

today = datetime.date.today()
year = today.year
month = today.month
day = today.day
weekday = today.weekday()
print(today)
print(year)
print(month)
print(day)
print(weekday)
print(datetime.date(2025,11,10).weekday())
print(datetime.timedelta())
print(datetime.timedelta(days = 10))
print(datetime.timedelta(days = -5))
last_day = datetime.date(2025,12,25)
print(last_day-today)
count = 0
current_date = datetime.date.today()
while current_date!=last_day:
    if current_date.weekday()!=6:
        count+=1
    current_date = current_date+datetime.timedelta(1)
print(count)

print(today.strftime("%d-%m-%Y"))
print(today.strftime("%A,%B %Y"))
print(today.strftime("%A,%B %y"))
print(today.strftime("%A,%m %Y"))

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

current_date = datetime.date.today()
for i in range(11):
    print(f"{current_date.strftime("%d-%m-%y")}, {days[i%7]} - {current_date.weekday()}")
    current_date = current_date+datetime.timedelta(1)
    
