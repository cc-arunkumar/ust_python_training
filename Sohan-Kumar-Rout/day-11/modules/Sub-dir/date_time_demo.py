from datetime import timedelta
from datetime import date

Today=date.today()
print(Today.year)

print("Today Month is  :",Today.month)
print("Today day is : ",Today.day)
print("Today weekDay is : ",Today.weekday())
custum_date =date(2025,11,17)
print("Custum Date : ",custum_date)

#Time delta

Tendays_later = Today + timedelta(days=10)
Tendays_prev = Today - timedelta(days=5)
last_day = date(2025,12,25)
today = date.today()
diff = last_day - today

print("Ten days later is : ",Tendays_later)
print("Ten days before is :",Tendays_prev)
print("Difference is : ",diff)

        

random_date=date(2025,1,22)
print(random_date)

# from datetime import date, timedelta

today = date.today()

christmas = date(today.year, 12, 25)

days_count = 0
current_day = today

while current_day <= christmas:
    if current_day.weekday() != 6:   
        days_count += 1
    current_day += timedelta(days=1)

print(f"Total days chritmas: {days_count}")


print(today.strftime(" %d %m %y"))
print(today.strftime("%A, %d %B %y"))
print(today.strftime(" %d %m %y"))
print(today.strftime("%d %m %Y",))

for day in range(0,11):
    Today = Today+timedelta(days=1)
    print(f"{Today.strftime("%d/%m/%y")},{Today.strftime("%A")}, :{Today.weekday()} ")
    
    
#Output
# 2025
# Today Month is  : 11
# Today day is :  17
# Today weekDay is :  0
# Custum Date :  2025-11-17
# Ten days later is :  2025-11-27
# Ten days before is : 2025-11-12
# Difference is :  38 days, 0:00:00
# 2025-01-22
# Total days chritmas: 34
#  17 11 25
# Monday, 17 November 25
#  17 11 25
# 17 11 2025
# 18/11/25,Tuesday, :1
# 19/11/25,Wednesday, :2
# 20/11/25,Thursday, :3
# 21/11/25,Friday, :4
# 22/11/25,Saturday, :5
# 23/11/25,Sunday, :6
# 24/11/25,Monday, :0
# 25/11/25,Tuesday, :1
# 26/11/25,Wednesday, :2
# 27/11/25,Thursday, :3
# 28/11/25,Friday, :4
    








