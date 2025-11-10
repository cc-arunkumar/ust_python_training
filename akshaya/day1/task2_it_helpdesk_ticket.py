# Task 2: IT Helpdesk Ticket Menu

hardware_ticket = 0
software_ticket = 0
network_ticket = 0


print("====== UST IT Helpdesk ======")
print("1. Raise Hardware Issue")
print("2. Raise Software Issue")
print("3. Raise Network Issue")
print("4. View Total Tickets Raised")
print("5. Exit")
while True:
    
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            hardware_ticket += 1
            print("Hardware issue recorded. IT team will respond soon.")
            
        case 2:
            software_ticket += 1
            print("Software issue recorded. IT team will respond soon.")
            
        case 3:
            network_ticket += 1
            print("Network issue recorded. IT team will respond soon.")
            
        case 4:
            total = hardware_ticket + software_ticket + network_ticket
            print(f"Hardware Tickets: {hardware_ticket}")
            print(f"Software Tickets: {software_ticket}")
            print(f"Network Tickets: {network_ticket}")
            print(f"Total Tickets Raised: {total}")
            
        case 5:
            print("Exiting Helpdesk. Thank you!")
            break
            
# sample output       
# ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 1
# Hardware issue recorded. IT team will respond soon.
# Enter your choice: 2
# Software issue recorded. IT team will respond soon.
# Enter your choice: 4
# Hardware Tickets: 1
# Software Tickets: 1
# Network Tickets: 0
# Total Tickets Raised: 2
# Enter your choice: 5
# Exiting Helpdesk. Thank you!