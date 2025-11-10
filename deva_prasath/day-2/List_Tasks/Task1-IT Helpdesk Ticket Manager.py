# Task 1: IT Helpdesk Ticket Manager


tickets=["Email not working", "VPN issue", "System slow", "Password reset"]
tickets.append("Printer not responding")
tickets.remove("System slow")
b=["Wi-Fi disconnected","Laptop battery issue"]
tickets.extend(b)
print("Total Open tickets: ",len(tickets))
print("Organised Ticket List: ")
tickets.sort()
for i in tickets:
    print(i)


# Total Open tickets:  6
# Organised Ticket List: 
# Email not working
# Laptop battery issue
# Password reset
# Printer not responding
# VPN issue
# Wi-Fi disconnected