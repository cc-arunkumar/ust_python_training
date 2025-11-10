a = int(input("Enter marks of subject 1 : "))
b = int(input("Enter marks of subject 2 : "))
c = int(input("Enter marks of subject 3 : "))
d = int(input("Enter marks of subject 4 : "))
e = int(input("Enter marks of subject 5 : "))
total_marks = a + b + c + d + e
percentage = (total_marks / 500) * 100
if(percentage > 90):
    print("A")
elif(percentage > 80 and percentage < 89):
    print("B")
elif(percentage > 70 and percentage < 79):
    print("C")
elif(percentage > 60 and percentage < 69):
    print("D")
else:
    print("E")
