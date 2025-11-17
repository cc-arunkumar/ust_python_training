# import datetime
from datetime import date,timedelta as delta

print(date.today().day)
print(date.today().year)
print(date.today().month)
print(date.today())
print(date.today().weekday())


custom_date = date(2025, 11, 17)

print("Custom date:", custom_date)
print("Year:", custom_date.year)
print("Month:", custom_date.month)
print("Day:", custom_date.day)
print("Day:", custom_date.weekday())
print("10 days later", custom_date + delta(days=10))
print("10 days ago", custom_date - delta(days=10))
last_day = date(2025,11,17 )

print("days until last day:", ( last_day-custom_date).days)

"remove all sunday from last date to custom date"
current_date = last_day
while current_date <= custom_date:  
    # print("Checking date:", current_date.weekday())
    if current_date.weekday() != 6:  
        print(current_date)
    current_date += delta(days=1)
print("Total days:", ( last_day-custom_date).days)

# custom_date.strftime("%A, %m %Y")
# print(custom_date.strftime("%A, %d %m %Y"))  # e.g.,


for i in range(10):
    print(custom_date.strftime("%d-%m-%Y")," ",custom_date.strftime("%A"),":", custom_date.weekday()) 
    custom_date += delta(days=1)

