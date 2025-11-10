# Task 3 - IT Infrastructure Report

# Scenario:
# Your company stores weekly sales data as tuples.
# Each tuple has:
# (branch_name, total_sales_amount)
# Example data:
# sales_data = (
#  ("Chennai", 85000),
#  ("Bangalore", 92000),
#  ("Hyderabad", 78000),
#  ("Pune", 102000),
#  ("Delhi", 98000)
# )

# Your Tasks:
# 1. Print all branches with sales above ₹90,000.
# 2. Find the average sales across all branches.
# 3. Identify and print the branch with the lowest sales.
# 4. Convert this tuple data into a list of tuples and update Pune’s sales to 105000 ,
# then convert it back to a tuple and print the updated data.


servers = (("AppServer1", ("192.168.1.10", 65, "Running")),("DBServer1", ("192.168.1.11", 85, "Running")),("CacheServer", ("192.168.1.12", 90, "Down")),("BackupServer", ("192.168.1.13", 40, "Running")))
for (server_name, (ip_address, cpu_usage, status)) in servers:
    if(status=="Running"):
        print(server_name)
max_usage=max(servers,key=lambda x:x[1][1])
print("Server with highest Used:",max_usage)
high_servers = list(filter(lambda x: x[1][1] > 80, servers))
print("High CPU Alrets: ",high_servers)

for server_name, (ip, cpu, status) in servers:
    if status == "Down":
        print(f"ALERT: {server_name} is down at {ip}")

#Sample output
# AppServer1
# DBServer1
# BackupServer
# Server with highest Used: ('CacheServer', ('192.168.1.12', 90, 'Down'))
# High CPU Alrets:  [('DBServer1', ('192.168.1.11', 85, 'Running')), ('CacheServer', ('192.168.1.12', 90, 'Down'))]
# ALERT: CacheServer is down at 192.168.1.12

