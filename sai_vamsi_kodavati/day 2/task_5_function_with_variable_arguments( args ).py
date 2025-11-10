# TASK: UST Employee Daily Work Report Automation

# TASK 5 Function with variable arguments ( args )


def average_efficience_score(*efficiency_score):
    total = 0
    count = 0
    for efficiency in efficiency_score:
        total += efficiency
        count += 1
    print("Average Team Efficiency: ",total/count)
    if((total//count)>25):
        print("Team performed above expectations.")
    else:
        print("Team needs improvement")
    
average_efficience_score(20.32,10,13,7)

# output

# Average Team Efficiency:  12.58
# Team needs improvement