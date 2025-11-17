import datetime
from datetime import timedelta

today=datetime.date.today()
# year=today.year()
# month=today.month()
# print(year)

# print(today)
# print(year)
# print(month)

# print(today.weekday())
# custom_date=datetime.date(2025,11,18)
# print(custom_date.weekday())


# print(f"10 Days later : {today+timedelta(days=10)}")
# print(f"5 Days before : {today+timedelta(days=-5)}")

"""last_day=datetime.date(2025,12,25)
cnt=0
cur_date=today
while cur_date<last_day:
    if cur_date.weekday()!=6:
        cnt+=1
    cur_date += datetime.timedelta(days=1)

print(f"Days to Christmas: {cnt}")"""


# random_date=datetime.date(2025,9,22)
# print(random_date)

# tdy=today.strftime("%D-%M-%Y")
# print(tdy)

# tdy=today.strftime("%A,%D,%M,%Y")
# print(tdy)


days=["Monday","Tuesday","Wednesday","Thursday","Friday","Satuday","Sunday"]
tdy=today.strftime("%A,%D,%M,%Y")

for i in range(7):
    cur_day=today+timedelta(days=i)
    date_str=cur_day.strftime("%d-%m-%y")
    week_day=cur_day.strftime("%A")
    print(f"{date_str},{week_day},{week_day}")
