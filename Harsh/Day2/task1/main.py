
from part1 import welcome
from part2 import emp_score
from part3 import report
from part4 import project_name
from part5 import avg_eff_score

def main():
    welcome()  
    print("Current Project:", project_name())  

   
    e1 = emp_score(10, 3)
    e2 = emp_score(11, 4)
    e3 = emp_score(12, 4)

    report("Harsh", "IT", e1)
    report("Rohit", "IT", e2)
    report("Prithvi", "IT", e3)

   
    avg_eff_score(e1, e2, e3)

if __name__ == "__main__":
    main()