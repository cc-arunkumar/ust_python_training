attendance = (
 ("E101", "John", 5),
 ("E102", "Priya", 3),
 ("E103", "Amit", 4),
 ("E104", "Neha", 2)
)
count = 0
highest_day = 0

for id,name,day in attendance:
    if (day>=4):
        print(f"{name}")
        count += 1

    if(day>highest_day):
        highest_day = day
        print(f"Employee with highest attendance :{name}({day} days)")
# print(count)
# print(highest_day)

    