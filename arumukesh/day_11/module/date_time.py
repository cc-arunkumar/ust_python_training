from datetime import date,timedelta

print(date.today().day)

print(date.today().weekday())

custom = date(2003,3,11)
print(custom.weekday())


print(date.today() + timedelta(days=10))
print(date.today() - timedelta(days=5))
print(date(2025,12,25) - date.today())
print(date(2003,3,1))
last = date(2025,12,25)
today = date.today()
count = 0
start = today.weekday()
for i in range((last- today).days//7):
    if start==6:
        start=0
    else:
        count+=1
        start+=1
        
print(count)
print((last - today).days-count)

print(today.strftime("%A"))
l = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for i in range(11):
    print(f"{today.strftime("%d/%m/%y")}:{l[today.weekday()]}:{today.weekday()}")
    today += timedelta(days=1)
    
dates = "2025-12-03"
if  date.fromisoformat(dates):
    print(True)
 
if date.strptime(dates,"%Y-%m-%d")<date.today():    
    print(True)
# if dates<date.today():
#     print(True)
# if dates.weekday():
#     print(True) 
# else:
#     print(False)