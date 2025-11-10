#Task 1: IT Helpdesk Ticket Manager


tickets = ["Email not working", "VPN issue", "System slow", "Password reset"]
tickets.append("Printer not responding")
tickets.remove("System slow")
tickets.extend(["Wi-Fi disconnected", "Laptop battery issue"])
tickets.sort()
print("Total open tickets: ",len(tickets))
print(tickets)

print("Organized ticket list: ")
for i in tickets:
    print(i)


# Total open tickets:  6
# ['Email not working', 'Laptop battery issue', 'Password reset', 'Printer not responding', 'VPN issue', 'Wi-Fi disconnected']
# Organized ticket list: 
# Email not working
# Laptop battery issue
# Password reset
# Printer not responding
# VPN issue
# Wi-Fi disconnected