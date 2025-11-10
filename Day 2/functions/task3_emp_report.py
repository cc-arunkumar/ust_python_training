# Part 3: Function with arguments and without return
# Objective:
# After calculating the efficiency, HR wants to print a formatted report for each
# employee.


def calculating_effiency(name,dep,ef_Score):
    print(f"Employee efficiency Score:{ef_Score}")
    if(ef_Score>25):
        print("\"Excellent\"")
    elif(ef_Score<25 and ef_Score>=15):
        print("good")
    else:
        print("need Improvemnet")
name = input("Enter Employee Name:")
dep = input("Enter Employee dep:")
tot_hours = int(input("Enter the hours Worked :"))
tot_task = int(input("Enter the Task Completed :"))
ef_Score = (tot_task/tot_hours)*10

calculating_effiency(name,dep,ef_Score)

# sample output

# Enter Employee Name:madhan
# Enter Employee dep:AI
# Enter the hours Worked :9
# Enter the Task Completed :25
# Employee efficiency Score:27.77777777777778
# "Excellent"