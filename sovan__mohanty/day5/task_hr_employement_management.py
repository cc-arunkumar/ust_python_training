print("HR Employement Management System")
print("1.Adding more Employees detail")
print("2.Reading the file")
print("3.Search Employee by ID")
print("4.Update Employee Salary")
print("5. Geenerate Summary Report")
print("6. Delete the Employee record")
choice=int(input("Enter your choice: "))
while(True):
    if(choice==1):
        #Task HR Employment Management System
        with open("HR_Employement_Management.txt",'w') as file:
            file.write("E101,Neha Sharma, HR, 600000,2020-05-10\n")
            file.write("E102,Ravi Kumar, IT, 750000,2019-08-16\n")
            file.write("E103,Arjun Mehta, Finance, 550000,2021-07-10\n")
            file.write("E104,Fatima Khan, HR, 650000,2020-02-11\n")
    elif(choice==2):
        #Adding more employee inputs
        with open("HR_Employement_Management.txt",'a') as file:
            id=input("Enter Employee ID: ")
            name=input("Enter Employee name: ")
            dept=input("Enter department name: ")
            sal=float(input("Enter Employee salary: "))
            doj=input("Enter Employee date of joining")
            file.write(f"{id},{name},{dept},{sal},{doj}\n")
    elif(choice==3):
    #Reading the file
        import os
        if os.path.exists("HR_Employement_Management.txt"):
            with open("HR_Employement_Management.txt",'r') as file:
                for line in file:
                    content=line.strip()
                    print(content)
        else:
            print("The file does not exists")
    elif(choice==4): 
        #Search Employee by ID

        with open("HR_Employement_Management.txt",'r') as file:
            target=input("Enter EMployee id: ")
            cout=0
            for line in file:
                content=line.strip().split(",")
                if content[0]==target:
                    print("Employee found:")
                    print("|".join(content))
                    cout+=1
                    break
                
            if(cout==0):
                print("Employee not found")
    elif(choice==5):
        #Update Employee salary

        with open("HR_Employement_Management.txt",'r') as file:
            update=[]
            id=input("Enter the Employee ID")
            new_salary=input("Enter the new salary")
            for line in file:
                content=line.strip().split(",")
                if content[0]==id:
                    content[3]=new_salary
                    update=",".join(content)
                    update.append(update + "\n")
                else:
                    update.append(line)
        with open("HR_Employement_Management.txt",'w') as file:
            file.write(update)
    elif(choice==6):
        #Generate Summary Report
        from collections import defaultdict
        dept_data=defaultdict(lambda:{"count":0,"total_salary":0})
        with open("HR_Employement_Management.txt",'r') as file:
            for line in file:
                content=line.strip().split(",")
                if len(content)>=4:
                    dept=content[2]
                    sal=float(content[3])
                    dept_data[dept]['count']+=1
                    dept_data[dept]['total_salary']+=sal
                    
        with open("Report.txt",'w') as file:
            for dept,data in dept_data.items():
                count=data['count']
                total_salary=data["total_salary"]
                avg_sal=total_salary/count if count else 0
                file.write(f"{dept} Department-->Employees: {count} | Total Salary: {float(total_salary)} | Average Salary: {avg_sal}\n")
    elif(choice==7):
        #Delete the Employee record
        update=[]
        deleted=False
        with open("HR_Employement_Management.txt",'r') as file:
            id=input("Enter the Employee id: ")
            for line in file:
                content=line.strip().split(",")
                if id==content[0]:
                    deleted=True
                    continue
                update.append(line)
        with open("HR_Employement_Management.txt",'w') as file:
            file.write(update)
        if deleted:
            print("Employee deleted successfully!")
    else:
        file.close()
        break
    choice=int(input("Enter your choice: "))

            


            
    
    
    
        
            
    

           
            


    