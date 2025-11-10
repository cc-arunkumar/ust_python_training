# #Task 2: IT Helpdesk Ticket Menu
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

hardwaret=0
softwaret=0
networkt=0
total=0
print("====== UST IT Helpdesk ======")
print("1. Raie Hardware Issue")
print("2. Raie Software Issue")
print("3. Raie Network Issue")
print("4. View Total Tickets Raised")
print("5. Exit")
while(True):
    
    n=int(input("Enter your choice: "))
    
    if(n==1):
        hardwaret=hardwaret+1
        total=total+1
        print("Hardware issue recorded. IT team will respond soon.")
    elif(n==2):
        softwaret=softwaret+1
        total=total+1
        print("Software issue recorded. IT team will respond soon.")
    elif(n==3):
        networkt=networkt+1
        total=total+1
        print("Network issue recorded. IT team will respond soon.")
    elif(n==4):
        print(f"HardwarecTickets: {hardwaret}")
        print(f"Software Tickets: {softwaret}")
        print(f"Network Ticket: {networkt}")
        print(f"Total Tickets Raised: {total}")
    elif(n==5):
        print("Exiting Helpdesk.Thank you!")
        break
    else:
        print("Enter proper choice")
        
#Sample Output
# ====== UST IT Helpdesk ======
# 1. Raie Hardware Issue      
# 2. Raie Software Issue      
# 3. Raie Network Issue       
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 1
# Hardware issue recorded. IT team will respond soon.
# Enter your choice: 2
# Software issue recorded. IT team will respond soon.
# Enter your choice: 3
# Network issue recorded. IT team will respond soon.
# Enter your choice: 4
# HardwarecTickets: 1
# Software Tickets: 1
# Network Ticket: 1
# Total Tickets Raised: 3
# Enter your choice: 5
# Exiting Helpdesk.Thank you!