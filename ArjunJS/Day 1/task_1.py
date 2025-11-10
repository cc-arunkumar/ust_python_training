#Task 1:
# Take input from end user for marks of 5 subject 
# Calculate total and percentage
# A-90 and above , B- 80-89 , C-70-79 .... D- 60-69 F - below 60
mark_list=[]
total=0
ch='Y'
while(ch=='Y' or ch=='y'):
    print("Choose the below options:")
    print("1. Enter the marks of 5 subject")
    print("2. If mark provided find Total")
    print("3. Find Grade")
    print("4. Exit")
    n=int(input("Choose choice:"))
    if(n==1):
        mark_list=[]
        for i in range(1,6):
            mark=int(input(f"Enter the mark for Subject {i}: "))
            mark_list.append(mark)
    elif(n==2):
        if len(mark_list)>0:
            total = sum(mark_list)
            print("Total is :",total)
        else:
            print("Mark not provided")
    elif(n==3):
        if len(mark_list)>0:
            total = sum(mark_list)
            percent = total/5
            if(percent>=90):
                print("Grade A")
            elif(80<=percent<90):
                print("Grade B")
            elif(70<=percent<80):
                print("Grade C")
            elif(60<=percent<70):
                print("Grade D")
            else:
                print("Grade F(Failed)")
        else:
            print("Mark not given!!!")
    elif(n==4):
        break
    else:
        print("Provide a number within range!!")
    ch=input("\nDo you wish to continue(Y/N)")