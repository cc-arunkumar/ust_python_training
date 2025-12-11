def transform_data_func(employees_data):
    transformed = []
    for emp in employees_data:
        emp_copy = emp.copy()
        emp_copy["category"] = "Fresher" if emp_copy["age"] <= 25 else "Experienced"
        transformed.append(emp_copy)
    return transformed


