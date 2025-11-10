#Task 3:IT Infrastructure Report

# Scenario:
# You have nested tuples representing company servers and their configuration
# details.
# Each tuple in the list looks like:
# (server_name, (ip_address, cpu_usage%, status))
# Example:
# servers = (
#  ("AppServer1", ("192.168.1.10", 65, "Running")),
#  ("DBServer1", ("192.168.1.11", 85, "Running")),
#  ("CacheServer", ("192.168.1.12", 90, "Down")),
#  ("BackupServer", ("192.168.1.13", 40, "Running"))
# )
# Your Tasks:
# 1. Print all server names with status = "Running".
# 2. Find the server with the highest CPU usage.
# 3. Display all servers that have CPU usage above 80% as:
# Tuple Tasks 3
# High CPU Alert: DBServer1 (85%) | CacheServer (90%)
# 4. For servers that are “Down”, print:
# ALERT: CacheServer is down at 192.168.1.12

servers = (
 ("AppServer1", ("192.168.1.10", 65, "Running")),
 ("DBServer1", ("192.168.1.11", 85, "Running")),
 ("CacheServer", ("192.168.1.12", 90, "Down")),
 ("BackupServer", ("192.168.1.13", 40, "Running"))
)

status_running = [i[0] for i in servers if i[1][2]=="Running"]
print("Running servers:", status_running)

highest_gpu_usage = max([i[1][1] for i in servers])
highest_gpu_usage_server = [i[0] for i in servers if i[1][1]==highest_gpu_usage]
print("Server with highest GPU usage:", highest_gpu_usage_server[0])

high_cpu_usage_servers = [i[0] for i in servers if i[1][1]>80]

print("High CPU Alert:", end=" ")

print(" | ".join([f"{i} ({[j[1] for j in servers if j[0]==i][0][1]}%)" for i in high_cpu_usage_servers]))

for i in servers:
    if i[1][2]=="Down":
        print(f"ALERT: {i[0]} is down at {i[1][0]}")

#Sample Output
# Running servers: ['AppServer1', 'DBServer1', 'BackupServer']
# Server with highest GPU usage: CacheServer
# High CPU Alert: DBServer1 (85%) | CacheServer (90%)
# ALERT: CacheServer is down at 192.168.1.12