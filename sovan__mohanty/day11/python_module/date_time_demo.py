from datetime import date
from datetime import timedelta
today=date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())

cust_date=date(2025,10,18)
print(cust_date)

ten_days_later=today+timedelta(days=10)
print(ten_days_later)

cust=date(2025,9,5)
print(cust)

# count=1
# last_day=date(2025,11,16)
# while today!=last_day:
#     if(today.weekday()==6):
#         continue
#     else:
#         count+=1
#     today=today+timedelta(days=1)
# print(count)

from datetime import datetime, timedelta

# today = datetime.today().date()
# last_day = datetime(2025, 12, 30).date()
# days_count = 0

# current = today
# while current <= last_day:
#     if current.weekday() != 6:  # weekday() returns 6 for Sunday
#         days_count += 1
#     current += timedelta(days=1)

# print("Days excluding Sundays:", days_count)


print(today.strftime("%d-%m-%Y"))
print(today.strftime(" %d %m %Y"))


for i in range(0,11):
    today=today+timedelta(days=1)
    print(f"{today.strftime("%d/%m/%y")},{today.strftime("%A")} : {today.weekday()}")

#Sample Execution  
#2025-11-17
# 2025
# 11  
# 17  
# 0
# 2025-10-18
# 2025-11-27
# 2025-09-05
# 17-11-2025
#  17 11 2025
# 18/11/25,Tuesday : 1
# 19/11/25,Wednesday : 2
# 20/11/25,Thursday : 3
# 21/11/25,Friday : 4
# 22/11/25,Saturday : 5
# 23/11/25,Sunday : 6
# 24/11/25,Monday : 0
# 25/11/25,Tuesday : 1
# 26/11/25,Wednesday : 2
# 27/11/25,Thursday : 3
# 28/11/25,Friday : 4