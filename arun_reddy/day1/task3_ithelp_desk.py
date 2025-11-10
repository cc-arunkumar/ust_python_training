print("======UST IT HELPDESK=====")
print("1.Raise Hardware Issue")
print("2. Raise Software Issue")
print("3. Raise Network Issue")
print("4. View Total Tickets Raised")
print("5. Exit ")
hardware_count=0
software_count=0
network_count=0
while True:
    ch=int(input("Enter ur choice"))
    match ch:
        case 1:
            print("Hardware issue recorded,IT team will respond soon")
            hardware_count=hardware_count+1
        case 2: 
            print(" Software issue recorded.IT team will respond soon")
            software_count=software_count+1
        case 3:
            print("Network issue recorded.IT team will respond soon")
            network_count=network_count+1
        case 4:
            print(f" Software_ticket_count:{software_count},Hardware_ticket_count:{hardware_count},Network_ticket_count:{network_count}")
            print("Total_Ticket_Count",software_count+hardware_count+network_count)
        case 5:
            print("Exit program GraceFully")
            break

# sample execution
# ======UST IT HELPDESK=====
# 1.Raise Hardware Issue      
# 2. Raise Software Issue     
# 3. Raise Network Issue      
# 4. View Total Tickets Raised
# 5. Exit
# Enter ur choice1
# Hardware issue recorded,IT team will respond soon
# Enter ur choice2
#  Software issue recorded.IT team will respond soon
# Enter ur choice3
# Network issue recorded.IT team will respond soon
# Enter ur choice4
#  Software_ticket_count:1,Hardware_ticket_count:1,Network_ticket_count:1
# Total_Ticket_Count 3
# Enter ur choice5
# Exit program GraceFully
