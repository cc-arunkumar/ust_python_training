# average_effiiciency
def average_effi(*efficiency_score):
    total=0
    for score in efficiency_score:
        total+=score    
    avg=total/len(efficiency_score)
    print("Average Team Efficiency: ",avg)
    if(avg>25):
        print("Team performed above expectations.")
    else:
        print("Team needs improvement.")


average_effi(35,45,57,88,45,11)

# Average Team Efficiency:  46.833333333333336
# Team performed above expectations.