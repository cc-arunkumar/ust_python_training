# IT Infrastructure Report

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

# Tuple of server records (server_name, (IP, CPU_usage, status))
servers = (
    ("AppServer1", ("192.168.1.10", 65, "Running")),
    ("DBServer1", ("192.168.1.11", 85, "Running")),
    ("CacheServer", ("192.168.1.12", 90, "Down")),
    ("BackupServer", ("192.168.1.13", 40, "Running"))
)

# Print servers that are currently running
print("Servers currently running:")
for name, (ip, cpu, status) in servers:
    if status == "Running":
        print(name)

# Find server with highest CPU usage
max_cpu = 0
max_server = ""
for name, (ip, cpu, status) in servers:
    if cpu > max_cpu:
        max_cpu = cpu
        max_server = name
print(f"\nServer with highest CPU usage: {max_server} ({max_cpu}%)")

# Identify servers with CPU usage greater than 80%
high_cpu_servers = []
for name, (ip, cpu, status) in servers:
    if cpu > 80:
        high_cpu_servers.append(f"{name} ({cpu}%)")

# Print high CPU alerts if any
if high_cpu_servers:
    print("\nHigh CPU Alert:", " | ".join(high_cpu_servers))
else:
    print("\nNo servers with high CPU usage.")

# Print alerts for servers that are down
for name, (ip, cpu, status) in servers:
    if status == "Down":
        print(f"\nALERT: {name} is down at {ip}")

# Output:
# AppServer1
# DBServer1
# BackupServer
#
# Server with highest CPU usage: CacheServer (90%)
#
# High CPU Alert: DBServer1 (85%) | CacheServer (90%)
#
# ALERT: CacheServer is down at 192.168.1.12
