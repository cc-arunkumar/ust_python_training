#Task 1: IT Helpdesk Ticket Manager

#code
tickets=["Email not working","VPN issue","System slow","Password reset"]
new_ticket="Printer not responding"
tickets.append(new_ticket)
tickets.remove("System slow")
tickets.extend(["Wi-fi disconnected","Laptop battery issue"])
total_number_of_tickets=len(tickets)
print("Total open tickets: ",total_number_of_tickets)
tickets.sort()
print("Organized Ticket List:")
for each_ticket in tickets:
    print(each_ticket)
print()



#output
'''
Total open tickets:  6
Organized Ticket List:
Email not working
Laptop battery issue
Password reset
Printer not responding
VPN issue
Wi-fi disconnected

'''