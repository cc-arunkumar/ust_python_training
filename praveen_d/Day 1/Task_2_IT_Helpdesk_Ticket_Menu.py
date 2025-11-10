# Task_2_IT_Helpdesk_Ticket_Menu


toRiseCompliant=True
hardware_ticket_count=0
software_ticket_count=0
network_ticket_count=0

while toRiseCompliant:
    print("1. Raise Hardware Issue")
    print("2. Raise Software Issue")
    print("3. Raise Network Issue")
    print("4. View Total Tickets Raised")
    print("5. Exit")

    issue=int(input("Enter your choice:"))
  

    match issue:
        case 1:
            print("Hardware issue recorded. IT team will respond soon.")
            hardware_ticket_count+=1
        case 2:
            print("Software issue recorded. IT team will respond soon.")
            software_ticket_count+=1
        case 3:
            print("Network issue recorded. IT team will respond soon.")
            network_ticket_count+=1
        case 4:
            print( f"Hardware Ticket Raised:{hardware_ticket_count}\nNetwork Ticket raised:{network_ticket_count}\nSoftware Ticket Raised:{software_ticket_count}")
            total_tickets=hardware_ticket_count+software_ticket_count+network_ticket_count
            print(f"Total Tickets Raised:{total_tickets}")
        case 5:
            print("Exiting......")
            toRiseCompliant=False




# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice:1
# Hardware issue recorded. IT team will respond soon.
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice:2
# Software issue recorded. IT team will respond soon.
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice:3
# Network issue recorded. IT team will respond soon.
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice:4
# Hardware Ticket Raised:1
# Network Ticket raised:1
# Software Ticket Raised:1
# Total Tickets Raised:3
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice:5
# Exiting......