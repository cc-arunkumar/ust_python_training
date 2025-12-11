def transform_data(employee_data):
    for employee in employee_data:
        employee["category"] = "Fresher" if employee["age"] < 25 else "Experienced"
    return employee_data
