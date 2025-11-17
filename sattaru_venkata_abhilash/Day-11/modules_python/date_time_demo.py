import datetime
from datetime import date, timedelta

# Get today's date
today = date.today()
print("Today's full date is:", today)
print("This year is:", today.year)
print("This month is:", today.month)
print("Today's weekday number (Mon=0):", today.weekday())

# Create a custom specific date
custom_date = date(2025, 11, 17)
print("Custom date created:", custom_date)

# Add 10 days to today's date
ten_days_later = today + timedelta(days=10)
print("Date after adding 10 days:", ten_days_later)

# Add 5 days to today's date
ten_days_later = today + timedelta(days=5)
print("Date after adding 5 days:", ten_days_later)

# Subtract 5 days (negative timedelta)
ten_days_later = today + timedelta(days=-5)
print("Date after subtracting 5 days:", ten_days_later)

# Print another random date
random_date = date(2025, 9, 22)
print("Random example date:", random_date)

# Calculate days from today to Christmas (excluding Sundays)
today = date.today()
christmas = date(today.year, 12, 26)

current = today
without_sundays = []

while current <= christmas:
    if current.weekday() != 6:   # Not Sunday
        without_sundays.append(current)
    current += timedelta(days=1)

print("Total days until Christmas (excluding Sundays):", len(without_sundays))

# Date formatting examples
format = today.strftime("%d-%m-%Y")
print("Formatted date (DD-MM-YYYY):", format)

format = today.strftime("%d-%m-%y")
print("Formatted date (DD-MM-YY):", format)

format = today.strftime("%d-%M-%y")   # %M = minutes
print("Formatted date with minutes (DD-Min-YY):", format)

format = today.strftime("%d-%m-%y")
print("Formatted again (DD-MM-YY):", format)

format = today.strftime("%A, %d, %B, %y")
print("Formatted full date with weekday and month name:", format)

# List of day names
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Print next 10000 days
for i in range(10000):
    current = today + timedelta(days=i)
    
    date_format = current.strftime("%d/%m/%y")
    day_name = current.strftime("%A")
    day_index = days.index(day_name)
    
    print(f"Date: {date_format} | Day: {day_name} | Index: {day_index}")


# sample outputs:
# Today's full date is: 2025-11-17
# This year is: 2025
# This month is: 11
# Today's weekday number (Mon=0): 0
# Custom date created: 2025-11-17
# Date after adding 10 days: 2025-11-27
# Date after adding 5 days: 2025-11-22
# Date after subtracting 5 days: 2025-11-12
# Random example date: 2025-09-22
# Total days until Christmas (excluding Sundays): 39
# Formatted date (DD-MM-YYYY): 17-11-2025
# Formatted date (DD-MM-YY): 17-11-25
# Formatted date with minutes (DD-Min-YY): 17-11-25
# Formatted again (DD-MM-YY): 17-11-25
# Formatted full date with weekday and month name: Monday, 17, November, 25
# Date: 17/11/25 | Day: Monday | Index: 0
