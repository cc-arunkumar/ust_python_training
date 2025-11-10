#Categorize Age Groups

# HR wants to classify employees as:

# “Junior” → if age < 30

# “Mid-level” → if 30 ≤ age < 45

# “Senior” → if age ≥ 45

# Use a lambda with conditional expressions.


age=35
category=(lambda x:"Junior" if x<30 else "Mid level" if x<45 else "senior")(age)
print(category)


#o/p:
#Mid level