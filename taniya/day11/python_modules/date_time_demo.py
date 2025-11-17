import datetime
# from datetime import date
today = datetime.date.today()
# print(today)
# print(f"today year is {today.year}")
# print(f"today month is {today.month}")

week=today.weekday()
# print(f"current weekday is {week}")

custom_date = datetime.date(2025,11,19)
# print(f"custom Date: {custom_date}")

week_day1=custom_date.weekday()
# print(week_day1)
# ten_days_later = today + datetime.timedelta(days=-5)
# print(ten_days_later)
last_date = datetime.date(2025,12,25)
# # diff = last_date - today
# # print(f"{diff.days}")
# count = 0
# current_day = today
# while current_day <= last_date:
#     if current_day.weekday() != 6:
#         count += 1
#     current_day += datetime.timedelta(days=1)
# print(f"total days : {count - 1}")
# todays=today.strftime("%d-%m-%y")
# print(todays)
# now = today.strftime("%A, %d %m %y")  
# print(now)

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(f"Today is: {days[today.weekday()]}")
for i in range(11):
    next_day = today + datetime.timedelta(days=i)
    format_date=datetime.date.strftime(next_day,"%d/%m/%Y")
    print(f"{format_date} is a {days[next_day.weekday()]}")
    
    




