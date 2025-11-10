def avg_eff_score(*eff_score):
    avg_eff = sum(eff_score)/len(eff_score)
    print(f"Average Team Efficiency : {round(avg_eff,2)}")
    if(avg_eff>25):
        print("Team performed above expectations.")
    else:
        print("Team needs improvement.")