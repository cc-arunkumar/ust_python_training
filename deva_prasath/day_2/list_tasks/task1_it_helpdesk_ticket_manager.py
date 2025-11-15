# IT Helpdesk Ticket Manager
# You are developing a small internal IT Helpdesk system for your company.
# You need to manage the list of open support tickets throughout the day.

# List of open tickets
tickets = ["Email not working", "VPN issue", "System slow", "Password reset"]

# Add a new ticket to the list
tickets.append("Printer not responding")

# Remove an existing ticket from the list
tickets.remove("System slow")

# Another list of issues to extend the original list
b = ["Wi-Fi disconnected", "Laptop battery issue"]

# Extend the original ticket list with new tickets
tickets.extend(b)

# Print the total number of open tickets
print("Total Open tickets: ", len(tickets))

# Print the organised ticket list after sorting
print("Organised Ticket List: ")
tickets.sort()  # Sort the tickets in alphabetical order

# Print each ticket in the sorted list
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