#employee attendence tracker
tuple1=(("E101","john",5),("E102","priya",3),("E103","amit",4),("E104","neha",2))
count_less_than4=0
for employee_id,employee_name,days_present in tuple1:
    if days_present>=4:
        print("employee attended 4 or more days = ",employee_name)
    else:
        count_less_than4 += 1
print("employees attended less than 4 ", count_less_than4)
max_attendence=0
top_employee=None
for employee_id,employee_name,days_present in tuple1:
    if days_present>max_attendence:
        max_attendence=days_present
        top_employee=(employee_id,employee_name,days_present)
print("employee with maximum attandence",top_employee)


#output
# employee attended 4 or more days =  john
# employee attended 4 or more days =  amit
# employees attended less than 4  2
# employee with maximum attandence ('E101', 'john', 5)