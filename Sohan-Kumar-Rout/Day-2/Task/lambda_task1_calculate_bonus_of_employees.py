#Task : Calculate the bonus of employees

#Code
salary = float(input("Enter your salary : "))
bonus = lambda sal : sal + (sal*0.10)
print("The total salary after bonus is : ",bonus(salary))

#Output
# Enter your salary : 50000
# The total salary after bonus is :  55000.0
