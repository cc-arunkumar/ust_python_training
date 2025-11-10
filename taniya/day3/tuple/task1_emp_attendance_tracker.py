# print all emp names who attend 4 or more days
tuple=(("E101","John",5),
            ("E102","Priya",3),
            ("E103","Amit",4),
            ("E104","Neha",2)
           )
# attendance
count = 0

for employee_id,employee_name,days_present in tuple:
    if days_present >= 4:
        print("employees who attended 4 or more days:",employee_name)
    elif days_present < 4:
        count += 1
        
print("employees present less than 4 days: ",count)

maximum_days = 0
employee=""
for employee_id,employee_name,days_present in tuple:
    if days_present > maximum_days:
        maximum_days = days_present
        employee = employee_name

        print(employee_name,"prsent for max days: ",days_present)


# output
# employees who attended 4 or more days: John
# employees who attended 4 or more days: Amit
# employees present less than 4 days:  2
# John prsent for max days:  5

        