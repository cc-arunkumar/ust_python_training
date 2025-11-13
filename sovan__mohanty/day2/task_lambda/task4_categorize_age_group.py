#Categorize Age groups
age=int(input("Enter the age of the employee: "))
categorize=lambda age:"Junior" if age<30 else("Mid-Level" if age>=30 and age<45 else "Senior")
print(categorize(age))

#Sample Executions
# Enter the age of the employee: 45
# Senior