# Task 1:IT Helpdesk Ticket Manager
tickets=["Email not working", "VPN issue", "System slow", "Password reset"]
tickets.append("Printer not responding")
tickets.remove( "System slow" )

tickets2=["Wi-Fi disconnected", "Laptop battery issue"]
tickets3=tickets+tickets2
print(tickets3)
print("Total open tickets=",len(tickets3))
sorted(tickets3)

print("Organized Ticket List:")
for ticket in tickets3:
    print(ticket)




# sample output
# Total open tickets= 6
# Organized Ticket List:
# Email not working
# VPN issue
# Password reset
# Printer not responding
# Wi-Fi disconnected
# Laptop battery issue