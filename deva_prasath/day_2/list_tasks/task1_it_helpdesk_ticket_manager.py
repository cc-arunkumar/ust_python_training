# IT Helpdesk Ticket Manager
# You are developing a small internal IT Helpdesk system for your company.
# You need to manage the list of open support tickets throughout the day.

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


#Sample output

# Total Open tickets:  6
# Organised Ticket List: 
# Email not working
# Laptop battery issue
# Password reset
# Printer not responding
# VPN issue
# Wi-Fi disconnected