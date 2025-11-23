
mark_list=[]
total_marks=0

for i in range(1,6):
    mark=int(input(f"Enter mark of {i}: "))
    mark_list.append(mark)
    total_marks+=mark

#mark_list=[20,40,10,90,100]
marks_percentage= (total_marks/500)*100
print(marks_percentage)

if(marks_percentage>=90):
    print("A")
elif(marks_percentage<90 and marks_percentage>80):
    print("B")
elif(marks_percentage<80 and marks_percentage>70):
    print("C")
elif(marks_percentage<70 and marks_percentage>60):
    print("D")
elif(marks_percentage<60 and marks_percentage>50):
    print("E")
else:
    print("No grade")



