#Calculate Bonus for Employees

salary=int(input("enter the salary: "))
bonus_salary=lambda salary:salary+(salary*0.10)
print("bonus=",bonus_salary(salary))

#sample execution
# enter the salary: 30000
# bonus= 33000.0