def team_average_efficiency(*efficiencies):
    if len(efficiencies) == 0:
        print("No efficiency scores provided.")
        return

    avg = sum(efficiencies) / len(efficiencies)
    print(f"Average Team Efficiency: {avg}")

    if avg > 25:
        print("Team performed above expectations.")
    else:
        print("Team needs improvement.")
