eid_check = ["E101","E102","E103","E104","E105"]

def add_new_employee():
    eid = input("Enter Employee ID: ")
    if eid in eid_check:
        print("Employee id exist: ")
        return
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = input("Enter salary: ")
    date = input("Enter joining date (YYYY-MM-DD): ")
    eid_check.append(eid)
    with open("employees.txt","a") as file:
        file.write(f"{eid},{name},{department},{salary},{date}\n")
        
def display():
    with open("employees.txt","r") as file:
        for line in file:
            for i in line.split(','):
                print(i,"|",end="")
        
def search():
    eid = input("Enter the Employee ID: ")
    with open("employees.txt","r") as file:
        flag = 0
        for line in file:
            if line[:4] == eid:
                flag = 1
                for i in line.split(','):
                    print(i,"|",end="")
        if flag == 0:
            print("Employee not found")
            
def update():
    eid = input("Enter the Employee ID: ")
    salary = input("Enter the salary: ")
    with open("employees.txt","r+") as file:
        line1 = file.readlines()
        i=0
        for line in line1:
            if line.split(",")[0] == eid:
                data = line.split(",")
                data[3] = salary
                file.seek(0)
                j = 0
                line = ",".join(data)
                for l in line1:
                    if j==i:
                       file.write(line) 
                    else:
                        file.write(l)
                    j+=1
            i+=1
                

# update()
# file = open("employees.txt","r")
# print(file.read())


def summary():
    d = {}
    with open("employees.txt","r") as file:
        for line in file:
            if line.split(",")[2] not in d:
                sal = int(line.split(",")[3])
                d[line.split(",")[2]] = [sal,1]
            else:
                d[line.split(",")[2]][0] += int(line.split(",")[3])
                d[line.split(",")[2]][1] += 1
    with open("report.txt","w") as file:
        for i in d:
            file.write(f"{i} Department -> Employees: {d[i][1]} | Total Salary: {d[i][0]} | Average Salary: {d[i][0]/d[i][1]}\n")
            
    
# summary()

def delete():
    eid = input("Enter Employee ID to delete: ")
    with open("employees.txt","r+") as file:
        i = 0
        line1 = file.readlines()
        for line in line1:
            if line.split(",")[0] == eid:
                file.seek(0)
                file.truncate()
                j=0
                for l in line1:
                    if j!=i:
                        print(l)
                        file.write(l)
                    j+=1
                break
            i+=1
            
# delete()
                

while(True):
    print("1. Add New Employee\n2. Display All Employees\n3. Search Employee by ID\n4. Update Employee Salary\n5. Generate Department Report\n6. Delete Employee\n7. Exit")
            
                    