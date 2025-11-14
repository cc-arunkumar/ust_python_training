# Task 3 : IT Infrastructure Report

# Code
servers = (
 ("AppServer1", ("192.168.1.10", 65, "Running")),
 ("DBServer1", ("192.168.1.11", 85, "Running")),
 ("CacheServer", ("192.168.1.12", 90, "Down")),
 ("BackupServer", ("192.168.1.13", 40, "Running"))
)

print("Running Servers : ")
for name, (ip, cpu, status) in servers:
    if status == "Running":
        print("-", name)

highest_cpu = 0
highest_server = ""
for name, (ip, cpu, status) in servers:
    if cpu > highest_cpu:
        highest_cpu = cpu
        highest_server = name
print("\nServer with Highest CPU Usage:", highest_server, f"({highest_cpu}%)")

high_alerts = []
for name, (ip, cpu, status) in servers:
    if cpu > 80:
        high_alerts.append(f"{name} ({cpu}%)")
print("\nHigh CPU Alert:", " | ".join(high_alerts))

print("\nDown Servers Alert:")
for name, (ip, cpu, status) in servers:
    if status == "Down":
        print(f"ALERT: {name} is down at {ip}")

        
# Sample Output
# Running Servers : 
# - AppServer1
# - DBServer1
# - BackupServer

# Server with Highest CPU Usage: CacheServer (90%)

# High CPU Alert: DBServer1 (85%) | CacheServer (90%)

# Down Servers Alert:
# ALERT: CacheServer is down at 192.168.1.12












