def update():
    emp_id = input("Enter Employee ID to update salary: ").strip()
    sal = input("Enter New Salary: ").strip()
    with open("employees.txt", "r") as file:
        
        for line in file:
            fields = line.strip().split(",")
            if fields[0].strip() == emp_id:
                fields[3]=sal
                print(f"ID: {fields[0]}")
                print(f"Name: {fields[1]}")
                print(f"Department: {fields[2]}")
                print(f"Salary: {fields[3]}")
                print(f"Date of Joining: {fields[4]}")
           
            
                
  