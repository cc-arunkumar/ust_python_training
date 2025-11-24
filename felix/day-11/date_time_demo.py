import datetime

# Get today's date
today = datetime.date.today()

# Extract year, month, day, and weekday
year = today.year        # Current year
month = today.month      # Current month
day = today.day          # Current day
weekday = today.weekday()  # Weekday as integer (Monday=0, Sunday=6)

# Print date components
print(today)
print(year)
print(month)
print(day)
print(weekday)

# Get weekday of a specific date
print(datetime.date(2025, 11, 10).weekday())

# Demonstrate timedelta objects
print(datetime.timedelta())            # Zero duration
print(datetime.timedelta(days=10))     # Duration of 10 days
print(datetime.timedelta(days=-5))     # Negative duration

# Calculate difference between two dates
last_day = datetime.date(2025, 12, 25)
print(last_day - today)  # Returns a timedelta object representing days until last_day

# Count the number of non-Sunday days between today and last_day
count = 0
current_date = datetime.date.today()
while current_date != last_day:
    if current_date.weekday() != 6:  # Skip Sundays
        count += 1
    current_date = current_date + datetime.timedelta(1)
print(count)

# Format dates in different string formats
print(today.strftime("%d-%m-%Y"))       # e.g., 24-11-2025
print(today.strftime("%A,%B %Y"))       # e.g., Monday,November 2025
print(today.strftime("%A,%B %y"))       # e.g., Monday,November 25
print(today.strftime("%A,%m %Y"))       # e.g., Monday,11 2025

# List of weekdays as names
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

# Print next 11 days with formatted date, weekday name, and weekday number
current_date = datetime.date.today()
for i in range(11):
    print(f"{current_date.strftime('%d-%m-%y')}, {days[i%7]} - {current_date.weekday()}")
    current_date = current_date + datetime.timedelta(1)
