# Task 3:IT Infrastructure Report
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

# Print all server names with status = "Running"
for (server_name, (ip_address, cpu_usage , status)) in servers:
    if(status=="Running"):
        print(server_name)

# Find the server with the highest CPU usage
max_usage=0
server=""
for (server_name, (ip_address, cpu_usage, status)) in servers:
    if cpu_usage > max_usage:
        max_usage = cpu_usage
        server = server_name
print(server)

# Display all servers that have CPU usage above 80%
for (server_name, (ip_address, cpu_usage, status)) in servers:
    if cpu_usage>80:
        print(server_name)

# For servers that are “Down”, print alert message
for (server_name, (ip_address, cpu_usage, status)) in servers:
    if status == "Down":
        print(f"\nALERT: {server_name} is down at {ip_address}")


# AppServer1
# DBServer1
# BackupServer

# CacheServer

# DBServer1
# CacheServer

# ALERT: CacheServer is down at 192.168.1.12