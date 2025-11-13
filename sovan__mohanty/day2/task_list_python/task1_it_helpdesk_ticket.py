#Task1 IT Helpdesk Ticket
Tickets=["Email not working", "VPN issue", "System slow", "Password reset"]
Tickets.append("Printer not responding")
Tickets.remove("System slow")
Tickets.extend(["Wi-Fi disconnected", "Laptop battery issue"])
print("Total Open tickets: ",len(Tickets))
print("Organized Ticket List:")
for ticket in Tickets:
    print(ticket)
#Sample Execution:
# Total Open tickets:  6
# Organized Ticket List:
# Email not working
# VPN issue
# Password reset
# Printer not responding
# Wi-Fi disconnected
# Laptop battery issue
