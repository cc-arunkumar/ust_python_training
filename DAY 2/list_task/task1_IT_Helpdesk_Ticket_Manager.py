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



"""
SAMPLE OUTPUT

['Email not working', 'VPN issue', 'System slow', 'Password reset', 'Printer not responding']
['Email not working', 'VPN issue', 'Password reset', 'Printer not responding']
['Email not working', 'VPN issue', 'Password reset', 'Printer not responding', 'Wi-Fi disconnected', 'Laptop battery issue']
6
['Email not working', 'Laptop battery issue', 'Password reset', 'Printer not responding', 'VPN issue', 'Wi-Fi disconnected']
Email not working
Laptop battery issue
Password reset
Printer not responding
VPN issue
Wi-Fi disconnected

"""