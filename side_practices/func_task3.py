import func_task2

name = input("enter your name:")
dep = input("enter your dep:")
tot_hours = int(input("Enter te total hours:"))
tot_task = int(input("Enter te total task completed:"))


e_score = func_task2.efficiency_score(tot_hours,tot_task)
def status(name,dep,e_score):
    if(e_score>=25):
        print("Excellent performance.")
    elif(e_score<25 and e_score>=15):
        print("Good performance.")
    else:
        print("Needs improvement")
status(name,dep,e_score)