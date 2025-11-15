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

# Initialize counters for each type of issue
hardware = 0
software = 0
network = 0

# Run the program until user chooses to exit
while True:
    # Display menu options
    print("1. Raise hardware issue")
    print("2. Raise software issue")
    print("3. Raise network issue")
    print("4. View total tickets raised")
    print("5. Exit")

    # Take user input for choice
    choice = input("Enter your choice: ")

    # Check which option user selected
    if choice == '1':  # Hardware issue
        hardware += 1
        print("Hardware issue recorded. IT team will respond soon.")
    elif choice == '2':  # Software issue
        software += 1
        print("Software issue recorded. IT team will respond soon.")
    elif choice == '3':  # Network issue
        network += 1
        print("Network issue recorded. IT team will respond soon.")
    elif choice == '4':  # Show ticket summary
        total = hardware + software + network
        print("Hardware tickets:", hardware)
        print("Software tickets:", software)
        print("Network tickets:", network)
        print("Total tickets raised:", total)
    elif choice == '5':  # Exit program
        print("Exiting helpdesk.\nThank you.")
        break
    else:  # Invalid input
        print("Invalid choice. Please try again.")



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