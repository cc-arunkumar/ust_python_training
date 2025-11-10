# Task 1: IT Helpdesk Ticket Manager


tickets = ["Email not working", "VPN issue", "System slow", "Password reset"]


tickets.append("Printer not responding")


tickets.remove("System slow")


tickets.extend(["Wi-Fi disconnected", "Laptop battery issue"])


print("Total open tickets:", len(tickets))


tickets.sort()


print("Organized Ticket List:")
for ticket in tickets:
    print(ticket)

#sample output
# Total open tickets: 6
# Organized Ticket List:
# Email not working
# Laptop battery issue
# Password reset
# Printer not responding
# VPN issue
# Wi-Fi disconnected
# PS C:\Users\303375\Downloads\Tasks> 
