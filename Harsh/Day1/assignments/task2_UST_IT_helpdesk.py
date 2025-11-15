# Task 2: IT Helpdesk Ticket Menu
# Objective: 
# Create a command-line helpdesk ticket system for employees to 
# raise and track IT issues such as hardware, software, or network problems.

print("============ UST IT Helpdesk ==============")
print("1. Raise Hardware Issue")
print("2. Raise Software Issue")
print("3. Raise Network Issue")
print("4. View Total Tickets Raised")
print("5. Exit")

hard=0
soft=0
network=0
total=0

while(True):
    choice=int(input("enter the choice: "))
    
    if(choice<1 or choice >5):
        print("Enter the number between 1 to 5")
        
    if (choice==1):
        hard+=1
        print("Hardware issue reported. IT team will respond soon")
        
    if(choice==2):
        soft+=1
        print("Software issue reported. IT team will respond soon")
        
    if(choice==3):
        network+=1
        print("Network issue reported. IT team will respond soon")
        
    if(choice==4):
        total=hard+soft+network
        print(f"Hardware Tickets: {hard}")
        print(f"Software Tickets: {soft}")
        print(f"Network Tickets: {network}")
        print(f"Total Tickets Raised: {total}")
        
    if(choice==5):
        print("Exiting Helpdesk. Thank you!")
        print("***********************************************************")
        break


# ============ UST IT Helpdesk ==============
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# enter the choice: 1
# Hardware issue reported. IT team will respond soon
# enter the choice: 2
# Software issue reported. IT team will respond soon
# enter the choice: 3
# Network issue reported. IT team will respond soon
# enter the choice: 4
# Hardware Tickets: 1
# Software Tickets: 1
# Network Tickets: 1
# Total Tickets Raised: 3
# enter the choice: 5
# Exiting Helpdesk. Thank you!
# ***********************************************************