# Tuple representing server information: (Server Name, (IP Address, CPU Usage, Status))
servers = (
    ("AppServer1", ("192.168.1.10", 65, "Running")),
    ("DBServer1", ("192.168.1.11", 85, "Running")),
    ("CacheServer", ("192.168.1.12", 90, "Down")),
    ("BackupServer", ("192.168.1.13", 40, "Running"))
)

# Print servers that are currently running
print("Servers with status 'Running':")
for name, (_, cpu, status) in servers:
    if status == "Running":  # Check if the server is running
        print(name)  # Print the server name

    if cpu > 80:  # Check if CPU usage is greater than 80
        print("High CPU Alert:", name)  # Print alert for high CPU usage

# Find the server with the highest CPU usage using max() and a lambda function to compare CPU values
highest_cpu_server = max(servers, key=lambda s: s[1][1])
print(f"\nServer with highest CPU usage: {highest_cpu_server[0]}")  # Print the server with the highest CPU usage

# Check for servers that are down and print alerts
for name, (ip, cpu, status) in servers:
    if status == "Down":  # Check if the server is down
        print(f"ALERT: {name} is down at {ip}")  # Print alert with server name and IP address

#Sample Execution
# Servers with status 'Running':
# AppServer1
# DBServer1
# High CPU Alert: DBServer1
# High CPU Alert: CacheServer
# BackupServer
# Server with highest CPU usage: CacheServer
# ALERT: CacheServer is down at 192.168.1.12