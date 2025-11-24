import json   # Import the JSON module to work with JSON data

# Open the existing employee data file in read mode
with open("C:/Users/303391/Desktop/ust_python_training/arjun_j_s/day_12/employee_data.json", "r") as employee_data_file:
    
    # Load the JSON data from the file into a Python dictionary
    emp_data = json.load(employee_data_file)

    # Create a new employee record as a dictionary
    my_employee = {"id": 103, "name": "Arun", "age": 16}
        
    # Append the new employee record to the list of employees
    emp_data["employees"].append(my_employee)

    # Print the updated employee data to the console
    print(emp_data)

# Open a new file in write mode to save the updated employee data
with open("C:/Users/303391/Desktop/ust_python_training/arjun_j_s/day_12/updated_employee_data.json", "w") as updated_file:
    
    # Write the updated employee data back to a new JSON file with indentation for readability
    json.dump(emp_data, updated_file, indent=2)