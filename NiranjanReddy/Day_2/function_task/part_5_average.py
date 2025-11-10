
# Part 5: Function with variable arguments ( args )

def average_efficiency_score(*efficiency_score):
    average=sum(efficiency_score)/len(efficiency_score)
    print("Average Team Efficiency: ", average)
    if average>25:
        print("Team performed above expectations")
    else:
        print("Team needs improvement")