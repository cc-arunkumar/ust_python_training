# # # date and time module
# # # import datetime

# # from datetime import date

# # today = date.today()
# # # print("Today's date:", today)

# # # year = today.year
# # # month = today.month
# # # day = today.day

# # # print("Year:", year)
# # # print("Month:", month)
# # # print("Day:", day)
# # weekday = today.weekday()  
# # print("Weekday number:", weekday)

# from datetime import datetime, timedelta

# today = datetime.today()
# ten_days_later = today + timedelta(days=10)

# print("Today's date:", today)
# print("Date 10 days later:", ten_days_later)

# five_days_previous=today -timedelta(days=10)
# print(five_days_previous)


# from datetime import date
# random_date = date(2025, 9, 22)
# print(random_date)



# from datetime import date
# today = date.today()
# last_day = date(2025, 12, 25)
# difference = last_day - today
# print(difference)


# from datetime import date, timedelta
# today = date.today()
# last_day = date(2025, 12, 25)
# count_days = 0
# current = today
# while current <= last_day:
#     if current.weekday() != 6:
#         count_days += 1
#     current += timedelta(days=1)
# print(f"Days without sunday{count_days}")

# from datetime import date, timedelta
# today=date.today()
# today.strftime("%d-%m-%y")
# print(today)

# from datetime import date, timedelta
# today=date.today()
# today.strftime("%d-%m-%y")
# print(today)

# from datetime import date
# today = date.today()
# today1 = today.strftime("%a %d %b %y")
# print(today1)

# from datetime import date
# today = date.today()
# weekday = today.weekday()
# output = today.strftime(f"%d-%m-%y,%A:{weekday}")
# print(output)

from datetime import date, timedelta
today = date.today()
for i in range(10):
    next_day = today + timedelta(days=i)
    weekday = next_day.weekday()  
    output = next_day.strftime(f"%d-%m-%y,%A:{weekday}")
    print(output)



