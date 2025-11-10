# Task 1:IT Helpdesk Ticket Manager

tickets = ["Email not working","VPN issue","System slow","Password reset"]

tickets.append("Printer not responding")

tickets.remove("System slow")

tickets.extend(["Wi-Fi disconnected","Laptop battery issue"])

total_tickets=len(tickets)
print(f"Total number of open tickets raised:{total_tickets}")

tickets.sort()

for i in range(0,total_tickets):
    print(tickets[i])



