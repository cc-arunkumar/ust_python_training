# Task 4: Categorize Age Groups
age=int(input("age= "))
classify=lambda age:"Junior" if age<30 else "Mid-level" if age<45  else "Senior" 
print(classify(age))
# sample output
# age= 22
# Junior