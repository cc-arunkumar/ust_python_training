# import math
# from math import sqrt
# a=2
# b=5
# c=8.2
# d=10
# e=7.2
# f=7.8
# g=7.4
# print("sqaure",math.sqrt(a))
# print("pi",math.pi)
# print("pow",math.pow(a,b))
# print("floor",math.floor(c))
# print("ciel",math.ceil(c))
# print("trunc",math.trunc(c))
# print("factorial",math.factorial(b))
# print("logs",math.log(d))
# print("round",round(e))
# print("round",round(f))



# import random
# num = random.randint(1, 10)
# print("Random number:", num)


# import random
# otp = random.randint(100000, 999999)
# print(otp)


# import random
# fruits={"Apple","Banana","Jackfruit"}
# # random.shuffle(fruits)
# # print(shuffle)

# random.choice(fruits)
# print("choice",fruits)



# from datetime import date
# from datetime import timedelta
# today = date.today()
# print("Today's date:", today)
# print("Year:", today.year)
# print("Month:", today.month)
# print("Day:", today.day)
# print("weekday:", today.weekday())
# d=date(2025,11,20)
# print("weekday:",d.weekday())


# from datetime import date, timedelta
# today = date.today()
# print("Today's date:", today)
# after_ten_days = today + timedelta(days=10)
# print(after_ten_days)
# random_date=date(2025,9,22)



# from datetime import date, timedelta
# today = date.today()
# days_left=0
# current=today
# last_date=date(2025,12,25)
# while current<=last_date:
#     if current.weekday()!=6:
#         days_left+=1
#     current+=timedelta(days=1)
# print("days left:",days_left)

# t=today.strftime("%d-%m-%y")
# t=today.strftime(" %d %m %Y")
# print(t)

from datetime import date, timedelta
today = date.today()
count = 0
for i in range(10):
    d = today + timedelta(days=i)
    print(d.strftime("%d/%m/%y,%A:") + str(count))
    count += 1
