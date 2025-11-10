#Task 1: Employee Attendance Tracker
attendance = (
 ("E101", "John", 5),
 ("E102", "Priya", 3),
 ("E103", "Amit", 4),
 ("E104", "Neha", 2)
)
count=0
maxi=attendance[0][2]
maxi_name = attendance[0][1]
for empid,name,days in attendance:
    if(days>=4):
        print(name)
    if(days<4):
        count+=1
    if(days>maxi):
        maxi=days
        maxi_name=name
print(count)
print(f"Employee with highest attendance:{maxi_name}({maxi}days)")
#Output
# John
# Amit
# 2
# Employee with highest attendance:John(5days)