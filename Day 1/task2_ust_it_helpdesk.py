# Task 2: IT Helpdesk Ticket Menu
# Objective: 
# Create a command-line helpdesk ticket system for employees to raise and track IT issues such as hardware, software, or network problems.

print("======UST IT Helpdesk======")
print("1.Raise Hardware Issue")
print("2.Raise Software Issue")
print("3.Raise Network Issue")
print("4.View Total Tickets Raised")
print("5.Exit")

count = 0

while True:
    n = int(input("Enter Your Choice:"))
    if(n==1):
        print("Hardware Issue recorded . IT team will respond soon\n")
        count += 1

    elif(n==2):
        print("Software Issue recorded . IT team will respond soon\n")
        count += 1

    elif(n==3):
        print("Network Issue recorded . IT team will respond soon\n")
        count += 1

    elif(n==4):
        print(f"View Total Tickets Raised:{count}\n")
    elif(n==5):
        print("!Thank You")
        break
    else:
        print("!Enter Valid Response")

# sample output
# ======UST IT Helpdesk======
# 1.Raise Hardware Issue
# 2.Raise Software Issue
# 3.Raise Network Issue
# 4.View Total Tickets Raised
# 5.Exit
# Enter Your Choice:1
# Hardware Issue recorded . IT team will respond soon

# Enter Your Choice:2
# Software Issue recorded . IT team will respond soon

# Enter Your Choice:3
# Network Issue recorded . IT team will respond soon

# Enter Your Choice:4
# View Total Tickets Raised:3

# Enter Your Choice:5
# !Thank You
    

