def grade_calculation(a,b,c,d,e):
    Total= a+b+c+d+e
    Percentage=(Total/500)*100

    if Percentage>90:
        grade='A'
    elif Percentage>=80 and Percentage<90:
        grade='B'
    elif Percentage>=70 and Percentage<80:
        grade='C'
    elif Percentage>60 and Percentage<70:
        grade='D'
    else:
        grade='F'
    return grade

Tamil=int(input("Enter Tamil Marks: "))
English=int(input("Enter English Marks: "))
Math=int(input("Enter Math Marks: "))
Science=int(input("Enter Science Marks: "))
Social=int(input("Enter Social Marks: "))

res=grade_calculation(Tamil,English,Math,Science,Social)
print(f"Your grade is {res}")