# Task 1:IT Helpdesk Ticket Manager
# Scenario:
# You are developing a small internal IT Helpdesk system for your company.
# You need to manage the list of open support tickets throughout the day.


# Initialize a list with some IT support tickets
tickets = ["Email not working", "VPN issue", "System slow", "Password reset"]

# Add a new ticket to the list
tickets.append("Printer not responding")

# Remove a specific ticket from the list
tickets.remove("System slow")

# Add multiple new tickets at once
tickets.extend(["Wi-Fi disconnected", "Laptop battery issue"])

# Print the total number of open tickets
print("Total open tickets:", len(tickets))

# Sort the tickets alphabetically for better organization
tickets.sort()

# Print the organized ticket list one by one
print("Organized Ticket List:")
for ticket in tickets:
    print(ticket)



# Total open tickets: 6
# Organized Ticket List:
# Email not working
# Laptop battery issue
# Password reset
# Printer not responding
# VPN issue
# Wi-Fi disconnected