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

#Code

# Tuple of servers: (Server Name, (IP Address, CPU Usage %, Status))
servers = (
    ("AppServer1", ("192.168.1.10", 65, "Running")),
    ("DBServer1", ("192.168.1.11", 85, "Running")),
    ("CacheServer", ("192.168.1.12", 90, "Down")),
    ("BackupServer", ("192.168.1.13", 40, "Running"))
)

# Print servers that are currently running
print("Servers with status 'Running':")
for name, (ip, cpu, status) in servers:
    if status == "Running":
        print(name)

# Find the server with the highest CPU usage
max_cpu = 0
max_server = ""
for name, (ip, cpu, status) in servers:
    if cpu > max_cpu:
        max_cpu = cpu
        max_server = name
print(f"\nServer with highest CPU usage: {max_server} ({max_cpu}%)")

# Identify servers with CPU usage above 80% and prepare alert list
high_cpu = []
for name, (ip, cpu, status) in servers:
    if cpu > 80:
        high_cpu.append(f"{name} ({cpu}%)")
print("\nHigh CPU Alert:", " | ".join(high_cpu))

# Alert if any server is down
for name, (ip, cpu, status) in servers:
    if status == "Down":
        print(f"\nALERT: {name} is down at {ip}")


#output
# PS C:\Users\303379\day3_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day3_training/task_3_IT_Infrastructure_Report
# Servers with status 'Running':
# AppServer1
# DBServer1
# BackupServer
# Server with highest CPU usage: CacheServer (90%)
# High CPU Alert: DBServer1 (85%) | CacheServer (90%)
# ALERT: CacheServer is down at 192.168.1.12
# PS C:\Users\303379\day3_training> 


