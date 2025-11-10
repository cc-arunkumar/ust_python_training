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

# Code

hardware=0
software=0
network=0
while True:
    print("1.raise hardware issue")
    print("2.raise software issue")
    print("3.raise network issue")
    print("4.view total tickets raised")
    print("5.exit")
    choice=input("enter your choice:")
    if choice=='1':
        hardware+=1
        print("hardware issue recorded IT team will respond soon")
    elif choice=='2':
        software+=1
        print("software issue recorded IT team will respond soon")
    elif choice=='3':
        network+=1
        print("network issue recorded IT team will respond soon")
    elif choice=='4':
        total=hardware+software+network
        print("hardware tickets:",hardware)
        print("software tickets:",software)
        print("network tickets:",network)
        print("total tickets raised:",total)
    elif choice=='5':
        print("existing helpdesk.\nthank you")
        break
    else:
        print("invalid")


#Output

# PS C:\Users\303379\day1_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day1_training/task2.py
# 1.raise hardware issue
# 2.raise software issue
# 3.raise network issue
# 4.view total tickets raised
# 5.exit
# enter your choice:1
# hardware issue recorded IT team will respond soon
# 1.raise hardware issue
# 2.raise software issue
# 3.raise network issue
# 4.view total tickets raised
# 5.exit
# enter your choice:2
# software issue recorded IT team will respond soon
# 1.raise hardware issue
# 2.raise software issue
# 3.raise network issue
# 4.view total tickets raised
# 5.exit
# enter your choice:3
# network issue recorded IT team will respond soon
# 1.raise hardware issue
# 2.raise software issue
# 3.raise network issue
# 4.view total tickets raised
# 5.exit
# enter your choice:4
# hardware tickets: 1
# software tickets: 1
# network tickets: 1
# total tickets raised: 3
# 1.raise hardware issue
# 2.raise software issue
# 3.raise network issue
# 4.view total tickets raised
# 5.exit
# enter your choice:5
# existing helpdesk.
# thank you
# PS C:\Users\303379\day1_training> 