import datetime  # Import the datetime module
from datetime import date  # Import date class from datetime module
from datetime import timedelta  # Import timedelta class for date manipulation

# Get today's date
today = datetime.date.today()
print(today)

# Print the year, month, and day from today's date
print(today.year)  
print(today.month)  
print(today.day)  

# Print the day of the week (0=Monday, 6=Sunday)
print(today.weekday())  

# Create a custom date (November 19, 2025)
c = datetime.date(2025, 11, 19)
print(c.weekday())  

# Add 10 days to today's date
ten_days_later = today + timedelta(days=10)
print(ten_days_later)  

# Subtract 10 days from today's date (Note: comment says 5 days, but code subtracts 10)
five_days_ago = today - timedelta(days=10)
print(five_days_ago) 

# Calculate the difference between today and December 25, 2025
last_date = date(2025, 12, 25)
diff = (last_date - today)  

# Create a specific date (September 22, 2025)
d = date(2025, 9, 22)
print(d)  

# Count the number of days (excluding Sundays) between today and the last_date
count = 0
for i in range(diff.days):  # Iterate over each day in the range
    current_day = today + timedelta(days=i)  # Get the current date by adding days
    if current_day.weekday() != 6:  # Check if the day is not a Sunday (6 = Sunday)
        count += 1  # Increment count if it's not a Sunday
print(f"Number of days excluding Sundays: {count}")  # Print the count of non-Sunday days

# Format today's date as "day-month-year" and print
a = today.strftime("%d-%m-%Y")
print(a)

# Format today's date as "Weekday day Month year" and print
b = today.strftime("%A%d%B%y")
print(b)

# Loop through the next 10 days and print each day's formatted date and weekday
for i in range(10):
    current_day = today + timedelta(days=i)  # Get the current day in the loop
    print(current_day.strftime("%d/%m/%y-%A"), current_day.weekday())  # Print formatted date and weekday


#Sample Output
# 2025-11-17
# 2025
# 11
# 17
# 0
# 2
# 2025-11-27
# 2025-11-07
# 2025-09-22
# Number of days excluding Sundays: 33
# 17-11-2025
# Monday17November25
# 17/11/25-Monday 0
# 18/11/25-Tuesday 1
# 19/11/25-Wednesday 2
# 20/11/25-Thursday 3
# 21/11/25-Friday 4
# 22/11/25-Saturday 5
# 23/11/25-Sunday 6
# 24/11/25-Monday 0
# 25/11/25-Tuesday 1
# 26/11/25-Wednesday 2