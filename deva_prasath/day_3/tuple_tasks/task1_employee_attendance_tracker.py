# Task 1: Employee Attendance Tracker
# Your HR system stores each employee’s attendance record for a week as a tuple

attendance=(("E101","Deva",3),("E102","Raj",5),("E103","Gokul",7))
count=0
for i,j,k in attendance:
    if k>4:
        print("Attended more than 4 days: ",j)
for i,j,k in attendance:
    if k<4:
        count+=1
print("Present less than 4 days: ",count)
for i,j,k in attendance:
    maxi=0
    if k>maxi:
        maxi=k
print("Employee with highest attendance: ",j)

#Sample output

# Attended more than 4 days:  Raj
# Attended more than 4 days:  Gokul
# Present less than 4 days:  1
# Employee with highest attendance:  Gokul