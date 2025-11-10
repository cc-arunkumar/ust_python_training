# Task 3: IT Infrastructure Report
# Scenario:
# Each tuple represents a server with details (server_name, (ip_address, cpu_usage%, status))

servers = (
    ("AppServer1", ("192.168.1.10", 65, "Running")),
    ("DBServer1", ("192.168.1.11", 85, "Running")),
    ("CacheServer", ("192.168.1.12", 90, "Down")),
    ("BackupServer", ("192.168.1.13", 40, "Running"))
)

# 1. Print all server names with status = "Running"
print("Running servers:")
for name, (ip, cpu, status) in servers:
    if status == "Running":
        print(f"- {name}")

# 2. Find the server with the highest CPU usage
max_cpu = -1
server_max_cpu = ""
for name, (ip, cpu, status) in servers:
    if cpu > max_cpu:
        max_cpu = cpu
        server_max_cpu = name
print(f"\nServer with highest CPU usage: {server_max_cpu} ({max_cpu}%)")

# 3. Display all servers that have CPU usage above 80%
print("High CPU Alert:")
for name, (ip, cpu, status) in servers:
    if cpu > 80:
        print(f"{name} ({cpu}%)")

# 4. For servers that are “Down”, print alert messages
for name, (ip, cpu, status) in servers:
    if status == "Down":
        print(f"ALERT: {name} is down at {ip}")


# Sample Output:
# Running servers:
# - AppServer1
# - DBServer1
# - BackupServer
#
# Server with highest CPU usage: CacheServer (90%)
# High CPU Alert:
# DBServer1 (85%)
# CacheServer (90%)
# ALERT: CacheServer is down at 192.168.1.12