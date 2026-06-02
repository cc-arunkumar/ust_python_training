#Part 3: Function with arguments and without return
def overview_performance(name,department,efficiency_score):
    print(f"Employee: {name} | Department: {department} | Efficiency: {efficiency_score}")
    if efficiency_score>=25:
        print("Excellent performance")
    elif efficiency_score>=15 and efficiency_score<25:
        print("Good performance")
    else:
        print("Needs improvement")

#Sample Output
#overview_performance("John Doe","IT",18.75)
#Employee: John Doe | Department: IT | Efficiency: 18.75
#Good performance