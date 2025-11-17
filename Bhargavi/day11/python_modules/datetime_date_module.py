# exploring about datetime module
import datetime
from datetime import date
from datetime import timedelta

# Print today's date and specific date components
print("Today:", date.today())
print("Year:", date.today().year)
print("Month:", date.today().month)
print("Day:", date.today().day)
print("Weekday (0=Monday, 6=Sunday):", date.today().weekday())

# Example for creating a specific date and getting weekday
d = date(2027, 9, 17)
print("Specific date:", d)
print("Weekday of specific date:", d.weekday())

# Working with timedelta for future and past dates
d = date.today()
print("Today:", d)
print("Future (10 days later):", d + timedelta(days=10))
print("Past (10 days ago):", d + timedelta(days=-10))

# Example: Calculate working days and Sundays between two dates
ld = date(2025, 12, 25)
td = date.today()
x = 0
y = 0
while td < ld:
    if td.weekday() != 6:  # If not Sunday (6)
        x += 1
    else:
        print("Sunday:", td)
        y += 1
    td += timedelta(days=1)
print("Total working days:", x, "Sundays:", y)

# Example: Using strftime for formatting dates
today = date.today()
print("Formatted Date 1:", today.strftime("%d-%m-%y"))
print("Formatted Date 2:", today.strftime("%D"))
print("Formatted Date 3:", today.strftime("%A, %d %B %Y"))
print("Formatted Date 4:", today.strftime("%d %B %Y"))

# Example: Loop through the next 10 days and print each day's date and weekday
today = date.today()
x = 0
while x < 10:
    print(f"{today.strftime('%D')}, {today.strftime('%A')} : {today.weekday()}")
    today += timedelta(days=1)
    x += 1

#output
# python_modules/datetime_date_module.py
# Today: 2025-11-17
# Year: 2025
# Month: 11
# Day: 17
# Weekday (0=Monday, 6=Sunday): 0   
# Specific date: 2027-09-17
# Weekday of specific date: 4       
# Today: 2025-11-17
# Future (10 days later): 2025-11-27
# Past (10 days ago): 2025-11-07    
# Sunday: 2025-11-23
# Sunday: 2025-11-30
# Sunday: 2025-12-07
# Sunday: 2025-12-14
# Sunday: 2025-12-21
# Total working days: 33 Sundays: 5
# Formatted Date 1: 17-11-25
# Formatted Date 2: 11/17/25
# Formatted Date 3: Monday, 17 November 2025
# Formatted Date 4: 17 November 2025
# 11/17/25, Monday : 0
# 11/18/25, Tuesday : 1
# 11/19/25, Wednesday : 2
# 11/20/25, Thursday : 3
# 11/21/25, Friday : 4
# 11/22/25, Saturday : 5
# 11/23/25, Sunday : 6
# 11/24/25, Monday : 0
# 11/25/25, Tuesday : 1
# 11/26/25, Wednesday : 2