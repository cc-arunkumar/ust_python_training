servers = (
    ("AppServer1", ("192.168.1.10", 65, "Running")),
    ("DBServer1", ("192.168.1.11", 85, "Running")),
    ("CacheServer", ("192.168.1.12", 90, "Down")),
    ("BackupServer", ("192.168.1.13", 40, "Running"))
)

print("Servers with status 'Running':")
for name, (_, cpu, status) in servers:
    if status == "Running":
        print(name)
    if cpu > 80:
        print("High CPU Alert:",name)

highest_cpu_server = max(servers, key=lambda s: s[1][1])
print(f"\nServer with highest CPU usage: {highest_cpu_server[0]}")


for name, (ip, cpu, status) in servers:
    if status == "Down":
        print(f"ALERT: {name} is down at {ip}")
        
#Sample Execution
# Servers with status 'Running':
# AppServer1
# DBServer1
# High CPU Alert: DBServer1
# High CPU Alert: CacheServer
# BackupServer
# Server with highest CPU usage: CacheServer
# ALERT: CacheServer is down at 192.168.1.12