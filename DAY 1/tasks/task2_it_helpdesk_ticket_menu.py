"""
IT Helpdesk Ticket Menu

Objective: 
	Create a command-line helpdesk ticket system for employees to raise and track IT issues such as hardware, software, or network problems.

"""


print("UST IT HELPDESK")   # Display system title

hardware=0;software=0;network=0;total=0   # Initialize ticket counters

while True:   # Infinite loop to repeatedly show menu
    print("1. Raise Hardware Issue")
    print("2. Raise Software Issue")
    print("3. Raise Network Issue")
    print("4. View Total Tickets Raised")
    print("5. Exit")
    choice=int(input("Enter Your choice: "))   # Get user choice
    match choice:   # Match-case structure for menu actions
        
        case 1:
            print("Hardware issue recorded. IT team will respond soon.")   # Acknowledge hardware issue
            hardware+=1   # Increment hardware ticket count
        case 2:
            print("Software issue recorded. IT team will respond soon")   # Acknowledge software issue
            software+=1   # Increment software ticket count
        case 3:
            print("Newtwok issue recorded. IT team will respond soon.")   # Acknowledge network issue
            network+=1   # Increment network ticket count
        case 4:
        
            print(f"Hardware Tickets: {hardware}")   # Display hardware ticket count
            print(f"Software Tickets: {software}")   # Display software ticket count
            print(f"Network Tickets: {network} ")   # Display network ticket count
            total=software+hardware+network   # Calculate total tickets
            print(f"Total Tickets Raised: {total}")   # Show total
        case 5:
            print("Exiting Helpdesk. Thank you!")   # Exit message
            break   # Break loop to exit program
        case _:
            print("Please Choose from 1-5")   # Handle invalid menu choice


# SAMPLE OUTPUT

"""UST IT HELPDESK
1. Raise Hardware Issue
2. Raise Software Issue
3. Raise Network Issue
4. View Total Tickets Raised
5. Exit
Enter Your choice: 1
Hardware issue recorded. IT team will respond soon.
1. Raise Hardware Issue
2. Raise Software Issue
3. Raise Network Issue
4. View Total Tickets Raised
5. Exit
Enter Your choice: 2
Software issue recorded. IT team will respond soon
1. Raise Hardware Issue
2. Raise Software Issue
3. Raise Network Issue
4. View Total Tickets Raised
5. Exit
Enter Your choice: 4
Hardware Tickets: 1
Software Tickets: 1
Network Tickets: 0
Total Tickets Raised: 2
1. Raise Hardware Issue
2. Raise Software Issue
3. Raise Network Issue
4. View Total Tickets Raised
5. Exit
Enter Your choice: 5
Exiting Helpdesk. Thank you!"""
