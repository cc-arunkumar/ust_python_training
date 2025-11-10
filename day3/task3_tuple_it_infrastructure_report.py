#tuple IT Infrastructure report


servers = (("AppServer1", ("192.168.1.10", 65, "Running")),("DBServer1", ("192.168.1.11", 85, "Running")),("CacheServer", ("192.168.1.12", 90, "Down")),("BackupServer", ("192.168.1.13", 40, "Running")))
print("Running Servers:")
for name, (ip, cpu, status) in servers:
    if status == "Running":
        print(name)
print()
max_cpu = 0
max_server = ""
for name, (ip, cpu, status) in servers:
    if cpu > max_cpu:
        max_cpu = cpu
        max_server = name
print(f"Highest CPU Usage: {max_server} ({max_cpu}%)\n")
high_cpu = [f"{name} ({cpu}%)" for name, (ip, cpu, status) in servers if cpu > 80]
print("High CPU Alert:", " | ".join(high_cpu))
print()
for name, (ip, cpu, status) in servers:
    if status == "Down":
        print(f"ALERT: {name} is down at {ip}")
 
#sample output
#  Running Servers:
# AppServer1
# DBServer1
# BackupServer

# Highest CPU Usage: CacheServer (90%)

# High CPU Alert: DBServer1 (85%) | CacheServer (90%)

# ALERT: CacheServer is down at 192.168.1.12