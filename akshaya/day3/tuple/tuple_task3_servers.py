# Task 3: IT Infrastructure Report

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
print(f"\nServer with highest CPU usage: {max_server} ({max_cpu}%)")


print("\nHigh CPU Alert:")
alerts = []
for name, (ip, cpu, status) in servers:
    if cpu > 80:
        alerts.append(f"{name} ({cpu}%)")
print(" | ".join(alerts))


print("\nDown Servers:")
for name, (ip, cpu, status) in servers:
    if status == "Down":
        print(f"ALERT: {name} is down at {ip}")



#sample output
# Running Servers:
# AppServer1
# DBServer1
# BackupServer

# Server with highest CPU usage: CacheServer (90%)

# High CPU Alert:
# DBServer1 (85%) | CacheServer (90%)

# Down Servers:
# ALERT: CacheServer is down at 192.168.1.12
