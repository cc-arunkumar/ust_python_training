# import datetime
from datetime import date, timedelta as delta   # Import date and timedelta classes

# Print today's date components
print(date.today().day)       # Day of the month
print(date.today().year)      # Current year
print(date.today().month)     # Current month
print(date.today())           # Full date (YYYY-MM-DD)
print(date.today().weekday()) # Day of week (0=Monday, 6=Sunday)

# Define a custom date
custom_date = date(2025, 11, 17)

# Print details of custom_date
print("Custom date:", custom_date)
print("Year:", custom_date.year)
print("Month:", custom_date.month)
print("Day:", custom_date.day)
print("Day:", custom_date.weekday())   # Day of week for custom_date

# Add and subtract 10 days
print("10 days later", custom_date + delta(days=10))
print("10 days ago", custom_date - delta(days=10))

# Define last_day as same as custom_date
last_day = date(2025, 11, 17)

# Difference in days between last_day and custom_date
print("days until last day:", (last_day - custom_date).days)

# Remove all Sundays between last_day and custom_date
current_date = last_day
while current_date <= custom_date:  
    if current_date.weekday() != 6:   # Skip Sundays
        print(current_date)
    current_date += delta(days=1)
print("Total days:", (last_day - custom_date).days)

# Print formatted dates for 10 consecutive days starting from custom_date
for i in range(10):
    print(custom_date.strftime("%d-%m-%Y"), " ", custom_date.strftime("%A"), ":", custom_date.weekday()) 
    custom_date += delta(days=1)

# ==================sample output=========================
# 24
# 2025
# 11
# 2025-11-24
# 0
# Custom date: 2025-11-17
# Year: 2025
# Month: 11
# Day: 17
# Day: 0
# 10 days later 2025-11-27
# 10 days ago 2025-11-07
# days until last day: 0
# 2025-11-17
# Total days: 0
# 17-11-2025   Monday : 0
# 18-11-2025   Tuesday : 1
# 19-11-2025   Wednesday : 2
# 20-11-2025   Thursday : 3
# 21-11-2025   Friday : 4
# 22-11-2025   Saturday : 5
# 23-11-2025   Sunday : 6
# 24-11-2025   Monday : 0
# 25-11-2025   Tuesday : 1
# 26-11-2025   Wednesday : 2
