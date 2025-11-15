#Task 1: IT Helpdesk Ticket Manager


# List of open tickets
tickets = ["Email not working", "VPN issue", "System slow", "Password reset"]

# Adding a new ticket to the list using append()
tickets.append("Printer not responding")

# Removing a specific ticket from the list using remove()
tickets.remove("System slow")

# Adding multiple tickets at once using extend()
tickets.extend(["Wi-Fi disconnected", "Laptop battery issue"])

# Sorting the list of tickets in alphabetical order
tickets.sort()

# Printing the total number of open tickets
print("Total open tickets: ", len(tickets))

# Printing the sorted list of tickets
print(tickets)

# Displaying the organized list of tickets one by one
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