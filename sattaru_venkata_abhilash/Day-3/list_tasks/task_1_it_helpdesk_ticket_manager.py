# Task 1: IT Helpdesk Ticket Manager
# Scenario:
# You are developing a small internal IT Helpdesk system to manage open support tickets.

# Step 1: Create the list of tickets
tickets = ["Email not working", "VPN issue", "System slow", "Password reset"]

# Step 2: Add a new ticket
tickets.append("Printer is not working")

# Step 3: Remove resolved ticket
tickets.remove("System slow")

# Step 4: Add two more tickets at once
tickets.extend(["Wi-Fi disconnected", "Laptop battery issue"])

# Step 5: Display total number of open tickets
print("Total open tickets:", len(tickets))

# Step 6: Sort tickets alphabetically
tickets.sort()

# Step 7: Display organized ticket list
print("Organized Ticket List:")
for ticket in tickets:
    print(ticket)


# Sample Output:
# Total open tickets: 6
# Organized Ticket List:
# Email not working
# Laptop battery issue
# Password reset
# Printer is not working
# VPN issue
# Wi-Fi disconnected
