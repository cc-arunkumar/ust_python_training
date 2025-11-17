import datetime
# today = datetime.date.today().strftime("%Y-%m-%d")
# print(f"Today's date is {today}")
#print todays year and month
today = datetime.date.today()   
# print(f"Current Year is {today.year}")
# print(f"Current Month is {today.month}")

# week = today.weekday()
# print(f"Current Weekday is {week}")
#writing a custom date
# custom_date = datetime.date(2025, 11, 19)
# print(f"Custom Date: {custom_date}")

# weekday1 = custom_date.weekday()
# print(weekday1)


# new = today + datetime.timedelta(days = -5)
# print(new)
# last_day = 2025-12-25
# diff = last_day - today
# print(diff)

day = datetime.date(2025, 12, 25)
diff = day - today
print(f"Days remaining for 2025-12-25: {diff.days} days")

#I want to remove all the sundays fromtoday till 2025-12-25
# sundays = 0 
# current_date = today
# while current_date <= day:
#     if current_date.weekday() == 6:
#         sundays += 1
#     current_date += datetime.timedelta(days=1)
# print(f"Total Sundays between {today} and {day}: {sundays}")
# print(f"Total days between {today} and {day}: {diff.days}")

# count = 0
# current_date = today
# while current_date <= day:
#     if current_date.weekday() != 6:
#         count += 1
#     current_date += datetime.timedelta(days=1)
# print(f"Total days : {count-1}")

# string_time = datetime.date.strftime(today, "%d-%m-%Y")

# print(string_time)

# new_string = datetime.date.strftime(today, "%d %m %y")
# print(new_string)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f"Today is: {days[today.weekday()]}")
for i in range(11):
    next_day = today + datetime.timedelta(days=i)
    formatted_date = datetime.date.strftime(next_day, "%d/%m/%Y")
    print(f"{formatted_date} is a {days[next_day.weekday()]}")