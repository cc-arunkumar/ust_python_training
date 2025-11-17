
import datetime
from datetime import date, time, datetime as dt, timedelta

current_day = datetime.date.today()
print(f"Today's date: {current_day}")


year = current_day.year
month = current_day.month
day = current_day.day

print(f"Year:  {year}")
print(f"Month: {month}")
print(f"Day:   {day}")
day_of_week_num = current_day.weekday()
print(f"Day of week: {day_of_week_num}")
print(datetime.date(2025,11,17).weekday())

print(datetime.timedelta())

print(datetime.timedelta(days=10))
print(datetime.timedelta(days=-5))
last_day=date(2025,12,25)
diff=last_day-datetime.date.today()
print(diff)


count=0
current_day=datetime.date.today()
while current_day!=last_day:
    if current_day.weekday()!=6:
        count+=1
    current_day=current_day+timedelta(1)
print(f"days {count}")
# required_date=date(2025,9,25)
# print(required_date) 
print(datetime.date.today().strftime("%d-%m-%Y"))
print(datetime.date.today().strftime("%A,%d %B %Y"))
print(datetime.date.today().strftime("%A,%d %m %y"))
print(datetime.date.today().strftime("%d %m %y"))


days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
current=datetime.date.today()
count=10
while count:
    print(f"{current.strftime("%d %m %y")}/{days[current.weekday()]}/{current.weekday()}")
    current=current+timedelta(1)
    count-=1
    


