from datetime import date
from datetime import timedelta
today=date.today()

# print("today year",today.year)
# print("today month",today.month)
# print("today day", today.day)
# print(today.weekday())
# custom_date = datetime.date(2025,12,1)
# print(custom_date)

random_date=date(2025,9,2)
# ten_day_later=today-timedelta(2025,9,12)
# last=(date(2025, 12, 25)-today).days

# last = 0
# christmas=date(2025, 12, 25)

# while today <= christmas:
#     if today.weekday() != 6: 
#         last += 1
#     today+=timedelta(days=1)
# print("total days ramining except sundays:",last)

format_date=today.strftime("%d-%m-%y")
# format_date=today.strftime("%A, %d %m %y")
# format_date=today.strftime("%A, %d %B %y")
# format_date=today.strftime("%a %d %B %y")
# print("format in day,month,year :",format_date)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for _ in range(10):
    day_name = days[today.weekday()]
    print(f"{today.strftime("%d/%m/%Y")}, {day_name}-{today.weekday()}")
    today += timedelta(days=1)