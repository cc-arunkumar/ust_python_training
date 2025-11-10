
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
hardware = 0
software = 0
network = 0

while True:
    print("\n====== UST IT Helpdesk ======")
    print("1. Raise Hardware Issue")
    print("2. Raise Software Issue")
    print("3. Raise Network Issue")
    print("4. View Total Tickets Raised")
    print("5. Exit")

    choice =int( input("Enter your choice: "))

    if choice == 1:
        hardware += 1
        print("Hardware issue recorded. IT team will respond soon.")
    elif choice == 2:
        software += 1
        print("Software issue recorded. IT team will respond soon.")
    elif choice == 3:
        network += 1
        print("Network issue recorded. IT team will respond soon.")
    elif choice == 4:
        total = hardware + software + network
        print("Hardware Tickets:", hardware)
        print("Software Tickets:", software)
        print("Network Tickets:", network)
        print("Total Tickets Raised:", total)
        
    elif choice == 5:
        print("Exiting Helpdesk. Thank you!")
        break
    else:
        print("invalid choice")



# sample output
# ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 1
# Hardware issue recorded. IT team will respond soon.

# ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 2
# Software issue recorded. IT team will respond soon.

# ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 3
# Network issue recorded. IT team will respond soon.

# ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 4
# Hardware Tickets: 1
# Software Tickets: 1
# Network Tickets: 1
# Total Tickets Raised: 3

# ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 5
# Exiting Helpdesk. Thank you!