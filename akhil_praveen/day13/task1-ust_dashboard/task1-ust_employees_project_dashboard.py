import json

# 1.Load the JSON file
with open("C:/Users/303394/Desktop/ust_python_training/akhil_praveen/day13/employees_data.json","r") as employee_data_file:
    data = json.load(employee_data_file)
    employees = data["employees"]
    fields = list(employees[0].keys())
    # print(fields)
    # ['id', 'name', 'role', 'skills', 'projects']

    # 2.Display all employee names with their roles
    print("All employee names with their roles\n")
    for row in employees:
        print(f"{row[fields[1]]} - {row[fields[2]]}")
    print("")

    # 3. Print each employee’s total hours spent across all projects
    print("Employee’s total hours spent across all projects\n")
    for row in employees:
        hr = 0
        for j in row[fields[4]]:
            if j["hours_logged"]:
                hr += j["hours_logged"]
        print(f"{row[fields[1]]} - {hr} hours")
    print("")

    # 4.Create a list of all unique skills across the organization
    skills = []
    for row in employees:
        skills += row[fields[3]]
    
    skills = set(skills)
    skills = list(skills)
    skills.sort()
    print("All skills: ",skills)

    # 5.Identify employees who know Python
    print("")
    print("Employees who knows python: ")
    for row in employees:
        if "Python" in row[fields[3]]:
            print("     ",row[fields[1]])
    print("")
    # 6.Create a dictionary mapping each project name to total hours contributed by all employees
    print("Each project name to total hours:")
    proj_dict = {}
    for row in employees:
        for j in row[fields[4]]:
            if j["name"] :
                if j["name"] in proj_dict:
                    proj_dict[j["name"]] +=j["hours_logged"]
                else:
                    proj_dict[j["name"]] = j["hours_logged"]
    
    print(proj_dict)

    #  7.Save the above dictionary as a new JSON file
    with open("C:/Users/303394/Desktop/ust_python_training/akhil_praveen/day13/project_hours.json","w") as project_hours:
        json.dump(proj_dict,project_hours,indent=2)