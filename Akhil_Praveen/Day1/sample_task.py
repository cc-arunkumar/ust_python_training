def read_marks():
    st=[]
    for i in range(5):
        mark=int(input(f"Enter the mark of subject {i+1}: "))
        st.append(mark)
    return st
def total_percentage(st):
    total=0
    for i in range(len(st)):
        total+=st[i]
    percentage=(total/500)*100
    print(f"Total marks: {total}")
    print(f"Percentage: {percentage}")
    return percentage
def grade_based_on_percentage(percentage):
    grade=""
    if(percentage>=90):
        grade="A"
    elif(percentage>=80):
        grade="B"
    elif(percentage>=70):
        grade="C"
    elif(percentage>=60):
        grade="D"
    else:
        grade="E"
    print(f"Grade:{grade}")

marks=read_marks()
percentage=total_percentage(marks)
grade_based_on_percentage(percentage)