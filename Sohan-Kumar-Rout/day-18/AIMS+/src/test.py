from datetime import date, datetime

print(datetime.today().strftime("%A-"))
print(datetime.today().weekday())
print(datetime.today().strftime("%B"))
print(datetime.today().strftime("%A-"),datetime.today().weekday(),datetime.today().strftime(":%B"))