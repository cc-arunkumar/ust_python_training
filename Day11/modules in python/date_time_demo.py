# from datetime import date

# today = date.today()
# print(today)

# cur_year = today.year
# print(cur_year)
# cur_month = today.month
# print(cur_month)
# cur_date = today.day
# print(cur_date)

# week = today.weekday()
# print(week)

# custom_date = date(2025,11,22)
# print(custom_date.weekday())

# from datetime import date, timedelta

# today = date.today()  # Get today's date
# ten_days_later = today + timedelta(days=10)

# print(f"Today's date: {today}")
# print(f"Date after 10 days: {ten_days_later}")

# from datetime import date, timedelta

# today = date.today()
# last_day = date(2025, 12, 31)

# days_later = last_day - today
# print(days_later)

# count = 0
# cur_day = today

# while cur_day <= last_day:
#     if cur_day.weekday() != 6:  # Skip Sundays
#         count += 1
#     cur_day += timedelta(days=1)  # Move to next day

# print(count)

# ran_date = date(2025,9,28)
# print(ran_date)



#---string format type---

# from datetime import date

# today = date.today()
# formatted = today.strftime("%d-%m-%Y")  # day-month-year
# print(formatted)

# new = today.strftime("%A, %d %B %Y")  # Full weekday name, day, full month name, year
# print(new)
# new = today.strftime("%A %D %B %Y")
# print(new)
from datetime import date, timedelta

today = date.today()
ten_days_later = today + timedelta(days=10)

for i in range((ten_days_later - today).days + 1):  # +1 to include last day
    day = today + timedelta(days=i)
    print(f"{day.strftime('%Y/%m/%d')}, {day.strftime('%A')}, {day.weekday()}")








