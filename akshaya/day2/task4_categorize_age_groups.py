#Task 4: Categorize Age Groups
categorize=lambda age:"Junior" if age<30 else("Mid-level" if age<45 else "Senior")
age=35
print(categorize(age))

#sample output
# Mid-level