# Function to modify employee data by adding a category
def modify_data(employees):
    for emp in employees:
        emp['category'] = 'Fresher' if emp['age'] < 25 else 'Experienced'
    return employees
