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
# High CPU Alert: DBServer1 (85%) | CacheServer (90%)
# 4. For servers that are “Down”, print:
# ALERT: CacheServer is down at 192.168.1.1

servers = (
 ("AppServer1", ("192.168.1.10", 65, "Running")),
 ("DBServer1", ("192.168.1.11", 85, "Running")),
 ("CacheServer", ("192.168.1.12", 90, "Down")),
 ("BackupServer", ("192.168.1.13", 40, "Running"))
)

max_cpu_usage=0
for server_name,(ip,cpu,status) in servers:
    if status=="Running":
        print(server_name)

    if cpu>max_cpu_usage:
        max_cpu_usage=cpu

    if cpu>80:
        print(f"High CPU Alert: {server_name}{(cpu)} | " )
    print()

    if status=="Down":
        print(f"ALERT: CacheServer is down at {ip}")

# EXPECTED OUTPUT:
# PS C:\UST python> & C:/Users/303489/AppData/Local/Programs/Python/Python312/python.exe "c:/UST python/Praveen D/Day 3/Tasks/tuple/task_3_it_infrastructure_report.py"
# AppServer1

# DBServer1
# High CPU Alert: DBServer185 | 

# High CPU Alert: CacheServer90 | 

# ALERT: CacheServer is down at 192.168.1.12
# BackupServer



