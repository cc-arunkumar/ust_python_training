# Task 1:IT Helpdesk Ticket Manager
# Scenario:
# You are developing a small internal IT Helpdesk system for your company.
# You need to manage the list of open support tickets throughout the day.
# Instructions:
# 1. Create a list named tickets with the following ticket titles:
# ["Email not working", "VPN issue", "System slow", "Password reset"]
# 2. A new ticket "Printer not responding" arrives. Add it to the list.
# (Hint: use append() )
# 3. "System slow" issue has been resolved — remove it from the list.
# (Hint: use remove() )
# 4. Add two more tickets at once:
# ["Wi-Fi disconnected", "Laptop battery issue"]
# (Hint: use extend() )
# 5. Display total number of open tickets.
# (Hint: len() )
# 6. Sort the tickets alphabetically to organize them better.
# (Hint: sort() )
# 7. Display all ticket names line by line using a loop.
# Day 3 1
# Expected Output(sample):
# Total open tickets: 5
# Organized Ticket List:
# Email not working
# Laptop battery issue
# Password reset
# Printer not responding
# Wi-Fi disconnected

# Code

# Create a list of support tickets
tickets = ["Email not working", "VPN issue", "System slow", "Password reset"]

# Add a new ticket to the list using append()
tickets.append("Printer not responding")

# Remove a specific ticket from the list using remove()
tickets.remove("System slow")

# Add multiple new tickets at once using extend()
tickets.extend(["Wi-Fi disconnected", "Laptop battery issue"])

# Count the total number of open tickets using len()
open_ticket = len(tickets)

# Print the total number of open tickets
print("Total open tickets:", open_ticket)

# Print a header before showing the organised list of tickets
print("Organised Tickets:")

# Sort the tickets alphabetically using sort()
tickets.sort()

# Loop through the sorted list and print each ticket one by one
for i in tickets:
    print(i)

#OutPut
# 3_training/task1_Helpdesk_List.py
# Total open tickets: 6
# Organised Tickets:
# Email not working
# Laptop battery issue
# Password reset
# Printer not responding
# VPN issue
# Wi-Fi disconnected
# PS C:\Users\303379\day3_training> 
