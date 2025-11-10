#Task4- Calculating age diff

#Code.
age = int(input("Enter the age : "))
age_status = lambda age : "Junior" if age<30  else("Mid-Level" if age>=30 and age <45 else "Senior")
print(age_status(age))

#Output
# Enter the age : 34
# Mid-Level

