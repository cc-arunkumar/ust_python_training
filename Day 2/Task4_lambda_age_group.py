#Task 4: Categorize Age Groups
age=int(input("Enter the age : "))
age_group = lambda age : "Senior" if age>=45 else "Mid Level" if 45> age >=30 else "Junior"
print(age_group(age))
#Output
#Enter the age : 45
# Senior
# Enter the age : 32
# Mid Level
# Enter the age : 21
# Junior