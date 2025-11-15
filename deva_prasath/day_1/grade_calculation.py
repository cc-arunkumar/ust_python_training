# Function to calculate grade based on marks
def grade_calculation(a,b,c,d,e):
    Total = a + b + c + d + e  # Calculate total marks
    Percentage = (Total / 500) * 100  # Calculate percentage

    # Determine grade based on percentage
    if Percentage > 90:
        grade = 'A'
    elif Percentage >= 80 and Percentage < 90:
        grade = 'B'
    elif Percentage >= 70 and Percentage < 80:
        grade = 'C'
    elif Percentage > 60 and Percentage < 70:
        grade = 'D'
    else:
        grade = 'F'
    return grade

# Input marks for each subject
Tamil = int(input("Enter Tamil Marks: "))
English = int(input("Enter English Marks: "))
Math = int(input("Enter Math Marks: "))
Science = int(input("Enter Science Marks: "))
Social = int(input("Enter Social Marks: "))

# Calculate and print the grade
res = grade_calculation(Tamil, English, Math, Science, Social)
print(f"Your grade is {res}")


#Sample output
# Enter Tamil Marks: 95
# Enter English Marks: 96 
# Enter Math Marks: 95
# Enter Science Marks: 92
# Enter Social Marks: 98
# Your grade is A