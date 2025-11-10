#IT help desk manager
tickets=["Email not working","VPN issue","system slow","password reset"]
tickets.append("printer not responding")
tickets.remove("system slow")
tickets.extend(["wifi disconnected","laptop battery issue"])
print("total open tickets:",len(tickets))
tickets.sort()
print("organized ticket list:")
for ticket in tickets:
    print(ticket)

# total open tickets: 6
# organized ticket list:
# Email not working
# VPN issue
# laptop battery issue
# password reset
# printer not responding
# wifi disconnected