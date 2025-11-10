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
# 4. For servers that are “Down”,
servers = (
    ("AppServer1", ("192.168.1.10", 65, "Running")),
    ("DBServer1", ("192.168.1.11", 85, "Running")),
    ("CacheServer", ("192.168.1.12", 90, "Down")),
    ("BackupServer", ("192.168.1.13", 40, "Running"))
)

print("Running Servers:")
for name, (ip, cpu, status) in servers:
    if status == "Running":
        print(name)

max_cpu = 0
max_server = ""
for name, (ip, cpu, status) in servers:
    if cpu > max_cpu:
        max_cpu = cpu
        max_server = name
print("\nHighest CPU Usage:", max_server, f"({max_cpu}%)")

print("\nHigh CPU Alert:", end=" ")
alerts = []
for name, (ip, cpu, status) in servers:
    if cpu > 80:
        alerts.append(f"{name} ({cpu}%)")
print(" | ".join(alerts))

for name, (ip, cpu, status) in servers:
    if status == "Down":
        print(f"ALERT: {name} is down at {ip}")
# sample output
# Running Servers:
# AppServer1
# DBServer1
# BackupServer

# Highest CPU Usage: CacheServer (90%)

# High CPU Alert: DBServer1 (85%) | CacheServer (90%)

