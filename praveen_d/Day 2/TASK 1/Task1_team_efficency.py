

# Part 5_ Function with variable arguments (args)


def calculate_team_efficiency(*effiencies):
    sum=0
    for eff in effiencies:
        sum+=eff
    
    average=sum/len(effiencies)

    if average> 25:
        print("Team performed above expectations.")
    else:
        print("Team needs to improve")





