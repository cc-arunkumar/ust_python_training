"""
IT Helpdesk Ticket Menu

Objective: 
	Create a command-line helpdesk ticket system for employees to raise and track IT issues such as hardware, software, or network problems.

"""


print("UST IT HELPDESK")

hardware=0;software=0;network=0;total=0

while True:
    print("1. Raise Hardware Issue")
    print("2. Raise Software Issue")
    print("3. Raise Network Issue")
    print("4. View Total Tickets Raised")
    print("5. Exit")
    choice=int(input("Enter Your choice: "))
    match choice:
        
        case 1:
            print("Hardware issue recorded. IT team will respond soon.")
            hardware+=1
        case 2:
            print("Software issue recorded. IT team will respond soon")
            software+=1
        case 3:
            print("Newtwok issue recorded. IT team will respond soon.")
            network+=1
        case 4:
        
            print(f"Hardware Tickets: {hardware}")
            print(f"Software Tickets: {software}")
            print(f"Network Tickets: {network} ")
            total=software+hardware+network
            print(f"Total Tickets Raised: {total}")
        case 5:
            print("Exiting Helpdesk. Thank you!")
            break
        case _:
            print("Please Choose from 1-5")


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