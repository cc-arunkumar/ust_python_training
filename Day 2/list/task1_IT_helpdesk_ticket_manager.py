# Task 1:IT Helpdesk Ticket Manager
# Scenario:
# You are developing a small internal IT Helpdesk system for your company.
# You need to manage the list of open support tickets throughout the day.


tickets=["Email not working", "VPN issue", "System slow", "Password reset"]
print("Intial List:",tickets)

# Adding new
tickets.append("Printer not responding") 
print(f"\nAdded one from list:",tickets)

# Deleting 
tickets.remove("System slow")
print("\ndeleted one from list:",tickets)

# extending 
tickets.extend(["Wi-Fi disconnected", "Laptop battery issue"]) 
print("\nextended one from list:",tickets)

# length of tickets
print("\ntotal length of the list:",len(tickets))

# sorted order
tickets.sort() 
print(tickets)

for i in range(len(tickets)):
    print(tickets[i])

# sample output:
# Intial List: ['Email not working', 'VPN issue', 'System slow', 'Password reset']
# Added one from list: ['Email not working', 'VPN issue', 'System slow', 'Password reset', 'Printer not responding']
# deleted one from list: ['Email not working', 'VPN issue', 'Password reset', 'Printer not responding']
# extended one from list: ['Email not working', 'VPN issue', 'Password reset', 'Printer not responding', 'Wi-Fi disconnected', 'Laptop battery issue']

# total length of the list: 6
# ['Email not working', 'Laptop battery issue', 'Password reset', 'Printer not responding', 'VPN issue', 'Wi-Fi disconnected']
# Email not working
# Laptop battery issue
# Password reset
# Printer not responding
# VPN issue
# Wi-Fi disconnected

