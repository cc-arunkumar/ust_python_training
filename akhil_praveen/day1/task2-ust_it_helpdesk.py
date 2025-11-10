# Ust_it_helpdesk

def ust_it_help():
    print("===== UST IT Helpdesk =====")
    print("1. Raise Hardware Issue")
    print("2. Raise Software Issue")
    print("3. Raise Network Issue")
    print("4. View total tickets raised")
    print("5. Exit")
    hard=0
    soft=0
    net=0
    total=0
    while True:
        choice = int(input("Enter your choice: "))
        if(choice==1):
            hard+=1
            print("Hardware Issue recorded. IT team will respond soon")
        elif(choice==2):
            soft+=1
            print("Software Issue recorded. IT team will respond soon")
        elif(choice==3):
            net+=1
            print("Network Issue recorded. IT team will respond soon")
        elif(choice==4):
            print("Hardware tickets raised :",hard)
            print("Software tickets raised :",soft)
            print("Network tickets raised :",net)
            total=hard+soft+net
            print("Total tickets raised :",total)
        elif(choice==5):
            print("Exiting Helpdesk. Thank you!")
            break
        else:
            print("Invalid choice please enter valid choice.")
        print("")

ust_it_help()

# output
# ===== UST IT Helpdesk =====
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View total tickets raised
# 5. Exit
# Enter your choice: 1
# Hardware Issue recorded. IT team will respond soon

# Enter your choice: 2
# Software Issue recorded. IT team will respond soon

# Enter your choice: 3
# Network Issue recorded. IT team will respond soon

# Enter your choice: 4
# Hardware tickets raised : 1
# Software tickets raised : 1
# Network tickets raised : 1
# Total tickets raised : 3

# Enter your choice: 5
# Exiting Helpdesk. Thank you!