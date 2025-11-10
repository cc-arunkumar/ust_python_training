# UST IT Helpdesk

print("===== UST IT Helpdesk =====")
hardware_ticket,software_ticket,network_ticket = 0,0,0
while(True):
    print("1. Raise Hardware Issue\n2. Raise Software Issue\n3. Raise Network Issue\n4. View Total Tickets Raised\n5. Exit")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        hardware_ticket +=1
        print("Hardware issue recorded. IT team will respond soon")
    elif(choice == 2):
        software_ticket += 1
        print("software issue recorded. IT team will respond soon")
    elif(choice == 3):
        network_ticket += 1
        print("Network issue recorded. IT team will respond soon")
    elif(choice == 4):
        print("Hardware Tickets: ",hardware_ticket)
        print("Software Tickets: ",software_ticket)
        print("Network Tickets: ",network_ticket)
        print("Totla Tickets: ",hardware_ticket + software_ticket + network_ticket)
    elif(choice == 5):
        break
    else:
        print("Invalid choice")
    print("\n")
print("Exiting Helpdesk. Thank You!")


# output

# ===== UST IT Helpdesk =====
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 1
# Hardware issue recorded. IT team will respond soon


# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 3
# Network issue recorded. IT team will respond soon


# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 4
# Hardware Tickets:  1
# Software Tickets:  0
# Network Tickets:  1
# Totla Tickets:  2


# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 5
# Exiting Helpdesk. Thank You!