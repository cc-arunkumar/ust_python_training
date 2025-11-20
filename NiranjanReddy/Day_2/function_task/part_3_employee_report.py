# Part 3: Function with arguments and without return
def formatted_report(Employee_Name,Department_Name,efficiency_score ):
    print("Employee: ",Employee_Name,"| Department: ",Department_Name,"| Efficiency: ", efficiency_score)
    if efficiency_score >25:
        print("Excellent performance.")
    elif 15<=efficiency_score <=25:
        print("Good performance.")
    else:
        print("Needs improvement")
