#Task 2: IT Helpdesk Ticket Menu
print("===== UST IT Helpdesk =====")
print("1.Raise Hardware Issue")
print("2.Raise Software Issue")
print("3.Raise Network Issue")
print("4.View Total Tickets Raised")
print("5. Exit")
hardware_ticket_count = 0
software_ticket_count = 0
network_ticket_count = 0

while(True):

    value = int(input("Enter your choice: "))
    
    if value==1:
        hardware_ticket_count += 1 
        print(f"Hardware issue recorded. IT Team will respond soon.")
    elif value==2:
        software_ticket_count += 1
        print(f"Software issue recorded. IT Team will respond soon.")
    elif value==3:
        network_ticket_count += 1 
        print(f"Network issue recorded. IT Team will respond soon.")
    elif value==4:
        total_tickets_count = hardware_ticket_count+software_ticket_count+network_ticket_count
        print(f"Hardware Tickets: {hardware_ticket_count} \n Software Tickets: {software_ticket_count} \n Network Tickets: {network_ticket_count} \n Total Tickets: {total_tickets_count}")
    elif value==5:
        print("Exiting Helpdesk. Thank you!")
        break 
    else:
        print("Invalid Response!  Please Enter Correct Option")

#Sample Output
# ===== UST IT Helpdesk =====
# 1.Raise Hardware Issue
# 2.Raise Software Issue
# 3.Raise Network Issue
# 4.View Total Tickets Raised
# 5. Exit

# Enter your choice: 1
# Hardware issue recorded. IT Team will respond soon.
# Enter your choice: 2
# Software issue recorded. IT Team will respond soon.
# Enter your choice: 3
# Network issue recorded. IT Team will respond soon.
# Enter your choice: 1
# Hardware issue recorded. IT Team will respond soon.
# Enter your choice: 4
# Hardware Tickets: 2 
#  Software Tickets: 1
#  Network Tickets: 1
#  Total Tickets: 4
# Enter your choice: 5
# Exiting Helpdesk. Thank you!