#Task 1: Employee Attendance Tracker
attendance = (
 ("E101", "John", 5),
 ("E102", "Priya", 3),
 ("E103", "Amit", 4),
 ("E104", "Neha", 2)
)

employees_more_than_4days = [i[1] for i in attendance if i[2] >= 4]
print("Employees with more than 4 days attendance:", employees_more_than_4days)

count_less_than_4 = len(attendance)-len(employees_more_than_4days)
print("Number of employees with less than 4 days attendance:", count_less_than_4)

max_days = max([i[2] for i in attendance])
employee_max_days = [i[1] for i in attendance if i[2] == max_days]
print("Employee with highest attendance:", employee_max_days[0])

#Sample Output
# Employees with more than 4 days attendance: ['John', 'Amit']
# Number of employees with less than 4 days attendance: 2
# Employee with highest attendance: John
