# Task 1:IT Helpdesk Ticket Manager
# Scenario:
# You are developing a small internal IT Helpdesk system for your company.
# You need to manage the list of open support tickets throughout the day.




#  Step 1: Create the initial list of tickets
tickets = ["Email not working", "VPN issue", "System slow", "Password reset"]
new_ticket = "System slow"  # New ticket to be added

#  Step 2: Modify the ticket list
tickets.append(new_ticket)  
tickets.remove("System slow") 
tickets.extend(["Wi-Fi disconnected", "Laptop battery issue"])  # Add two more tickets

#  Step 3: Display the updated list and its length
print(tickets) 
print(len(tickets))  
#  Step 4: Sort the tickets alphabetically
tickets.sort()  
print(tickets)




# ===============sample output=================
# ['Email not working', 'VPN issue', 'Password reset', 'System slow', 'Wi-Fi disconnected', 'Laptop battery 
# issue']
# 6
# ['Email not working', 'Laptop battery issue', 'Password reset', 'System slow', 'VPN issue', 'Wi-Fi disconnected']