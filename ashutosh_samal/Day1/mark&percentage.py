#Calculate total marks and percentage

math_marks = int(input("Enter marks sequered in maths: "))
science_marks = int(input("Enter marks sequered in science: "))
english_marks = int(input("Enter marks sequered in English: "))
sst_marks = int(input("Enter marks sequered in social studies: "))
pedu_marks = int(input("Enter marks sequered in physical education: "))

total_marks_secured = (math_marks+science_marks+english_marks+sst_marks+pedu_marks)
percentage = (total_marks_secured/500)*100

if(percentage>=90):
    print("Total marks secured: ",total_marks_secured)
    print("Grade is A")
elif(percentage>=80 and percentage<90):
    print("Total marks secured: ",total_marks_secured)
    print("Grade is B")
elif(percentage>=70 and percentage<80):
    print("Total marks secured: ",total_marks_secured)
    print("Grade is C")
elif(percentage>=60 and percentage<=70):
    print("Total marks secured: ",total_marks_secured)
    print("Grade is D")
else:
    print("Total marks secured: ",total_marks_secured)
    print("Grade is F")
    

#Output
# Enter marks sequered in maths: 95
# Enter marks sequered in science: 90
# Enter marks sequered in English: 87
# Enter marks sequered in social studies: 90
# Enter marks sequered in physical education: 85
# Total marks secured:  447
# Grade is B