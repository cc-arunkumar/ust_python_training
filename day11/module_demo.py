# import math
# from math import sqrt
a=2
b=5
c=8.2
d=-19
e=7.5
# print("sqaure",math.sqrt(a))
# print("pi",math.pi)
# print("pow",math.pow(a,b))
# print("floor",math.floor(c))
# print("ciel",math.ceil(c))
# print("trunc",math.trunc(c))
# print("fact",math.factorial(b))
# print("negtive",math.fabs(d))
# print("logs",math.log(a))
# print("round",round(e))


# import random
# # otp=random.randint(100000,999999)
# # print(otp)
# fruits={"banana","apple","kiwi","sapota","watermelon","pear","fig"}
# print("original fruits :",fruits)
# print("shuffle",random.shuffle(fruits))


# import random

# fruits = ["banana", "apple", "kiwi", "sapota", "watermelon", "pear", "fig"]  # use a list
# print("original fruits:", fruits)

# shuffle =random.shuffle(fruits)  
# print("shuffled fruits:", shuffle)

# choice=random.choice(fruits)
# print("choice",choice)


import datetime
from datetime import date
from datetime import timedelta
today=date.today()
# print(today)
# print("year",today.year)
# print("month",today.month)
# print("day",today.day)
# print("weekday",today.weekday())

# d=date(2025,11,20)
# print("weekday",d.weekday())

tendays_later=today+datetime.timedelta(days=10)
# print("10 days later",tendays_later)
five_days_back=today+datetime.timedelta(days=-5)
# print("five days",five_days_back)
last_date=date(2025,12,25)
five_days_from_last_date = last_date - timedelta(days=5)
# print("Five days before Christmas:", five_days_from_last_date)


days_left=0
current=today
while current <= last_date:
    if current.weekday() != 6:  
        days_left+=1
    current+=timedelta(days=1)
# print("days left till cristmas excluding sunday",days_left)



d=today.strftime(" %d %m %Y")
# print(d)


days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
current_date = date.today()
for i in range(10):
    day_date = current_date + datetime.timedelta(days=i)
    day_code = day_date.weekday()
    print(f"{day_date.strftime('%Y-%m-%d ,%A-')}, {day_code}")

