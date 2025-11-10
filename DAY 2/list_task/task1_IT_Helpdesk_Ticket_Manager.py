"""
Scenario:

You are developing a small internal IT Helpdesk system for your company.
You need to manage the list of open support tickets throughout the day.

"""


tickets=["Email not working", "VPN issue", "System slow", "Password reset"]

tickets.append("Printer not responding") # Adding new
print(tickets)
tickets.remove("System slow") # Deleting 
print(tickets)
tickets.extend(["Wi-Fi disconnected", "Laptop battery issue"]) # extending 
print(tickets)
print(len(tickets)) # length of tickets
tickets.sort() # sorted order
print(tickets)

for i in range(len(tickets)):
    print(tickets[i])

