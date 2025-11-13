# Part 5: Function with variable arguments ( args )

def marks(*args):
    total1=sum(args)
    percentage=(total1/len(args)*100)*100
    print("percentage",percentage)
    if (percentage>25):
        print(" Team performed above expectations")
    else:
        print("Team needs improvement")

marks(100,90,70,88)

# sample output
#  percentage 870000.0
#  Team performed above expectations