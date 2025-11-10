#Part 5: Function with variable arguments ( args )
def avg_efficiency_score(*eff_scores):
    sum_of_scores = 0
    msg=""
    for score in eff_scores:
        sum_of_scores += score
    avg_scores = sum_of_scores/len(eff_scores) 

    if avg_scores>25:
        msg="Team performed above expectations."
    else:
        msg="Team needs improvement."

    return f"Average Team Efficiency: {avg_scores} \n {msg}"

#Sample Output
#avg_efficiency_score(18.75,27.5,30.0)
#'Average Team Efficiency: 25.416666666666668
# Team performed above expectations.'
