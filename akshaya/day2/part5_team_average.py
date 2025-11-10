# Function with variable arguments (*args)
def scores(*efficiencies):
    avg = sum(efficiencies) / len(efficiencies)
    print(f"Average Team Efficiency: {avg:.1f}")
    if avg > 25:
        print("Team performed above expectations")
    else:
        print("Team needs improvement")