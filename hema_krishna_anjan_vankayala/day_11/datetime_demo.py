from datetime import date 
today = date.today()
# print("Today's date:", today)
# print("TOday Year:", today.year)
# print("Today's Month:", today.month)
# print("Today's Day:", today.day)
# print("Today's Weekday (0-Mon..6-Sun):", today.weekday())
# print(date(2025, 11, 18).weekday())
# print("Current Date and Time:",datetime.now())

from datetime import timedelta
# tensdays_later = today + timedelta(days=10)
# print("Date after 10 days:", tensdays_later)

# fivedays_ago = today - timedelta(days=5)
# print("Date 5 days ago:", fivedays_ago)
# counter =0 
# last_day = date(2025,12,25)
today = date.today()
# while (today!=last_day):
#     if today.weekday()==6:
#         print(today)
#         counter += 1 
#     today = today + timedelta(days=1)
# print("Number of Sundays until 25th Dec 2025:", counter)
# print("Number of working days", (date(2025,12,25)-date.today()).days - counter)

# print(today.strftime("%A,%d %m %y"))

days = []
today = date.today()
for i in range(10):
    days.append(f"{today.strftime("%D, %A : ")} {today.weekday()}")
    today  = today + timedelta(days=1)
    print(f"{today.strftime("%D, %A : ")} {today.weekday()}")