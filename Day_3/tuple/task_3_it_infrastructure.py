# Task 3:IT Infrastructure Report
servers = (
 ("AppServer1", ("192.168.1.10", 65, "Running")),
 ("DBServer1", ("192.168.1.11", 85, "Running")),
 ("CacheServer", ("192.168.1.12", 90, "Down")),
 ("BackupServer", ("192.168.1.13", 40, "Running"))
)
max=0
# 1. Print all server names with status = "Running".
for server_name,(ip_address, cpu_usage, status) in servers:
    if status=="Running":
        print(f"Running status: {server_name}, {ip_address}, {cpu_usage}, {status}")

# 2. Find the server with the highest CPU usage.
    if cpu_usage>max:
        max=cpu_usage
        name=server_name
print(f"Max server: {name}")
# 3. Display all servers that have CPU usage above 80% as:
for server_name,(ip_address, cpu_usage, status) in servers:
    if cpu_usage>80:
        print(f"CPU usage above 80: {server_name},{ip_address},{cpu_usage},{status}")
# 4. For servers that are “Down”, print
for server_name,(ip_address, cpu_usage, status) in servers:
    if status=="Down":
        print(f"{server_name}- ALERT: CacheServer is down at 192.168.1.12")
# Sample output
# Running status: AppServer1, 192.168.1.10, 65, Running
# Running status: DBServer1, 192.168.1.11, 85, Running
# Running status: BackupServer, 192.168.1.13, 40, Running
# Max server: CacheServer
# CPU usage above 80: DBServer1,192.168.1.11,85,Running
# CPU usage above 80: CacheServer,192.168.1.12,90,Down
# CacheServer- ALERT: CacheServer is down at 192.168.1.12
