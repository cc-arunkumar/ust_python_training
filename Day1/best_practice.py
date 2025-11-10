name = input("Enter neme: ")
mathematics_mark = int(input("Enter mathematiccs mark: "))
chemistry_mark = int(input("Enter chemistry mark: "))
physics_mark = int(input("Enter physics mark: "))
english_mark = int(input("Enter english mark: "))
biology_mark = int(input("Enter biology mark: "))

total_marks = mathematics_mark + chemistry_mark + physics_mark + english_mark + biology_mark
percentage = total_marks*100/500

if percentage >= 90:
    print("A grade")
elif percentage >= 80:
    print("B grade")
elif percentage >= 70:
    print("C grade")
elif percentage >= 60:
    print("D grade")
