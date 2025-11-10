def avg_eff_score(*scores):
    total=0
    count=0
    for i in scores:
        total+=i
        count+=1
    avg=total/count
    print("Average Team Efficiency:" , avg)
    if avg>25:
        print("Tem performed well")
    else:
        print("Need improvement")