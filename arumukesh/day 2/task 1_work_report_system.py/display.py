def display(e_name,dep_name,score):
    print(f"Employee Name: {e_name}|Department: {dep_name}|Efficiency Score: {score:.2f}")
    if score >25:
        print("Excellent Performance")
    elif score >15:
        print("Good Performance")
    else:
        print("Needs Improvement")