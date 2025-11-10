# Task 2: IT Helpdesk Ticket Menu
# Objective: 
# 	Create a command-line helpdesk ticket system for employees to raise and track IT issues such as hardware, software, or network problems.


# ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice:


# Functional Rules
# ================

# Raise Hardware Issue
# 	Display: "Hardware issue recorded. IT team will respond soon."
# 	Increment hardware_ticket count.

# Raise Software Issue
# 	Display: "Software issue recorded. IT team will respond soon."
# 	Increment software_ticket count.

# Raise Network Issue
# 	Display: "Network issue recorded. IT team will respond soon."
# 	Increment network_ticket count.

# View Total Tickets Raised
# 	Display each issue type count and total number of tickets raised.

# Exit
# 	Exit program gracefully.
	
	
# Sample Execution:
# -------------------
# ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 2
# Software issue recorded. IT team will respond soon.

# Enter your choice: 1
# Hardware issue recorded. IT team will respond soon.

# Enter your choice: 4
# Hardware Tickets: 1
# Software Tickets: 1
# Network Tickets: 0
# Total Tickets Raised: 2

# Enter your choice: 5
# Exiting Helpdesk. Thank you!
hardware=0
software=0
network=0

while True:
    print("=======UST IT Helpdesk========")
    print("1.Raise Hardware Issue")
    print("2.Raise Software Issue")
    print("3.Raise Network Issue")
    print("4.view total tickets raised")
    print("5.exit")
    choice=int(input("enter the choice:"))

    if choice==1:
        print("Hardware issue is ticket raised")
        hardware+=1
    elif choice==2:
        print("software issue is ticket raised")
        software+=1
    elif choice==3:
        print("network issue is ticket raised")
        network+=1
    elif choice==4:
        print("Number of Hardware issue ticket: ",hardware)
        print("Number of software issue ticket:",software)
        print("Number of network issues ticket:",network)
        total=hardware+software+network
        print("Total raised issues :",total)
    elif choice==5:
        print("Exit")
        break

# sample output


#     =======UST IT Helpdesk========
# 1.Raise Hardware Issue
# 2.Raise Software Issue
# 3.Raise Network Issue
# 4.view total tickets raised
# 5.exit
# enter the choice:1
# Hardware issue is ticket raised
# =======UST IT Helpdesk========
# 1.Raise Hardware Issue
# 2.Raise Software Issue
# 3.Raise Network Issue
# 4.view total tickets raised
# 5.exit
# enter the choice:2
# software issue is ticket raised
# =======UST IT Helpdesk========
# 1.Raise Hardware Issue
# 2.Raise Software Issue
# 3.Raise Network Issue
# 4.view total tickets raised
# 5.exit
# enter the choice:3
# network issue is ticket raised
# =======UST IT Helpdesk========
# 1.Raise Hardware Issue
# 2.Raise Software Issue
# 3.Raise Network Issue
# 4.view total tickets raised
# 5.exit
# enter the choice:4
# Number of Hardware issue ticket:  1
# Number of software issue ticket: 1
# Number of network issues ticket: 1
# Total raised issues : 3
# =======UST IT Helpdesk========
# 1.Raise Hardware Issue
# 2.Raise Software Issue
# 3.Raise Network Issue
# 4.view total tickets raised
# 5.exit
# enter the choice:5
# Exit
    