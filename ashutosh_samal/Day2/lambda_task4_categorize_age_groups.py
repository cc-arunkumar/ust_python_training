#Task 4: Categorize Age Groups

age = int(input("Enter age: "))
employee_level = lambda age:"Junior" if age<30  else "Mid-level" if 30<=age<45 else "Senior"
print(employee_level(age))

#Sample Execution
# Enter age: 30
# Mid-level

# Enter age: 25
# Junior

# Enter age: 45
# Senior