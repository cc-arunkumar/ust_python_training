# Search Employee by ID
# Ask the user for an Employee ID.
# Search the file line by line.
# If found, display the employee details.
# If not found, print a message “Employee not found.”
# Example:
# Enter Employee ID to search: E103
# Employee Found:
# E103 | Arjun Mehta | Finance | 55000 | 2021-03-15


def search():
    # Ask the user to enter an Employee ID
    emp_id = input("Enter the id:").strip()
    
    # Flag to track if the employee is found
    found = False

    # Open the employees.txt file in read mode
    with open("employees.txt", "r") as file:
        for line in file:
            # Split each line into fields: [ID, Name, Department, Salary, Date of Joining]
            fields = line.strip().split(",")

            # Compare the entered ID with the first field (Employee ID)
            if fields[0].strip() == emp_id:
                # If match found, display employee details
                print("\n Employee Found:")
                print(f"ID: {fields[0]}")
                print(f"Name: {fields[1]}")
                print(f"Department: {fields[2]}")
                print(f"Salary: {fields[3]}")
                print(f"Date of Joining: {fields[4]}")
                
                # Mark as found and stop searching further
                found = True
                break

    # If no matching employee was found
    if not found:
        print(" Employee not found.")
