# Task 2: Employee Training Progress Tracker
# Scenario:
# You are tracking the employees who have completed their mandatory “Cyber
# Security Awareness” training.




#  Step 1: Create the initial list of completed employees
completed = ["John", "Priya", "Amit"]

#  Step 2: Add new completed employees
completed.append("Neha")   
completed.append("Rahul") 

#  Step 3: Remove an employee from the completed list
completed.remove("Amit")   

#  Step 4: Create a list of pending employees
pending = ["Meena", "Vivek", "Sita"]

#  Step 5: Merge pending employees into the completed list
completed.extend(pending)  

#  Step 6: Assign the merged list to allEmployess
allEmployess = completed

#  Step 7: Print the list before sorting
print(allEmployess) 
# Step 8: Sort the list alphabetically and Print
allEmployess.sort()  
print(allEmployess)  

#  Step 9: Print each employee name one by one
for x in range(len(allEmployess)):
    print(allEmployess[x])

#  Step 10: Print the total number of employees
print("Total Employees", len(allEmployess))


# ===========sample output=================
# ['John', 'Priya', 'Neha', 'Rahul', 'Meena', 'Vivek', 'Sita']
# ['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']
# John
# Meena
# Neha
# Priya
# Rahul
# Sita
# Vivek
# Total Employees 7
