from datetime import date

today = date.today()
print(today.year) #yyyy-mm-dd
print(today.month)
print(today.day)
print(today.weekday())



custom_date = date(2023, 12, 25)
print(custom_date)
# --------------------------------------------------------------------------------

from datetime import timedelta
ten_days_later = today + timedelta(days=10)
print(ten_days_later)

previous_days = today - timedelta(days = 5)
print(previous_days)

random_date = (date(2025,9,17))
print(random_date)

today = date.today()
christmas = date(2025, 12, 25)
current_day = today
days_count = 0

while current_day <= christmas:
    if current_day.weekday() != 6:
        days_count += 1
    current_day += timedelta(days=1)

print(f"Days left to Christmas excluding sundays: {days_count}")

format_date = today.strftime("%d-%m-%Y")
print(format_date)

format_date = today.strftime("%Mon-%m-%Y")
print(format_date)

s = today.strftime("%A, %d %B %Y")
print(s)

s = today.strftime("%A, %d %M %Y")
print(s)


days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for i in range(10):
    # day_name = days[today.weekday()]
    print(today.strftime(" %d/ %m/ %Y ,%A"),"-",today.weekday())
    today += timedelta(days=1)






