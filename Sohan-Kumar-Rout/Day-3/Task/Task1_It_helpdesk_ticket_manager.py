#Task 1: IT Helpdesk Ticket Manager

#Code
ticket=["Email not working","VPN Issue","System slow","Password reset"]
ticket.append("Printer not responding")
ticket.remove("System slow")
ticket.extend(["Wi-Fi disconnected","Laptop battery issue"])
print("Total open Tickets : ",len(ticket))
ticket.sort()
print("Organized Ticket List : ")
for tickets in ticket:
    print(tickets)

#Sample Output
# Total open Tickets :  6
# Organized Ticket List : 
# Email not working
# Laptop battery issue
# Password reset
# Printer not responding
# VPN Issue
# Wi-Fi disconnected


