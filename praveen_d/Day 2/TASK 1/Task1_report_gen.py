
# Part 3: Function with arguments and without return


def report_generator(employee_name,department_name,employee_effiency_score):
    print(f"Employee name:{employee_name}")
    print(f"Employee department:{department_name}")
    print(f"Employee Efficiency score:{employee_effiency_score}")
    if employee_effiency_score>25:
        print("Excelent performance")
    elif employee_effiency_score<25 and employee_effiency_score>15:
        print("Good perfomance")
    else:
        print("Needs Improvement")

# function


