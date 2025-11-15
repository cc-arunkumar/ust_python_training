# Function to calculate and evaluate average team efficiency
def team_average_efficiency(*efficiencies):
    # Check if no efficiency scores are provided
    if len(efficiencies) == 0:
        print("No efficiency scores provided.")
        return

    # Calculate average efficiency
    avg = sum(efficiencies) / len(efficiencies)
    print(f"Average Team Efficiency: {avg}")

    # Evaluate team performance based on average efficiency
    if avg > 25:
        print("Team performed above expectations.")
    else:
        print("Team needs improvement.")
