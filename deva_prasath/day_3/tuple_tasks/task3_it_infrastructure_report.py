#IT infrastructure report

# Your company stores server status.

# Tuple containing server data with server name, IP, CPU usage, and status
servers = (
    ("AppServer1", ("192.168.1.10", 65, "Running")),
    ("DBServer1", ("192.168.1.11", 85, "Running")),
    ("CacheServer", ("192.168.1.12", 90, "Down")),
    ("BackupServer", ("192.168.1.13", 40, "Running"))
)

# Loop through the servers and print the names of running servers
for i, j in servers:
    if j[2] == "Running":
        print("Running Servers: ", i)

# Find the server with the highest CPU usage
max_cpu = -1  # Initialize with a value lower than any possible CPU usage
max_server = ""
for name, (ip, cpu, status) in servers:
    if cpu > max_cpu:  # If this server has higher CPU usage than the previous max
        max_cpu = cpu
        max_server = name  # Update the server with the highest CPU usage
print("Server with highest CPU usage:", max_server)

# Find servers with CPU usage above 80% and create alert messages
high_cpu_servers = []  
for name, (ip, cpu, status) in servers:
    if cpu > 80:
        alert = f"{name} ({cpu}%)"  # Format the alert message
        high_cpu_servers.append(alert)

# Print the high CPU alerts if there are any
if high_cpu_servers:
    print("High CPU Alert:", " | ".join(high_cpu_servers))

# Loop through the servers and print an alert for any servers that are down
for name, (ip, cpu, status) in servers:
    if status == "Down":
        print(f"ALERT: {name} is down at {ip}")  # Print the alert for down servers



#Sample output

# Running Servers:  AppServer1
# Running Servers:  DBServer1
# Running Servers:  BackupServer
# Server with highest CPU usage: CacheServer
# High CPU Alert: DBServer1 (85%) | CacheServer (90%)
# ALERT: CacheServer is down at 192.168.1.12