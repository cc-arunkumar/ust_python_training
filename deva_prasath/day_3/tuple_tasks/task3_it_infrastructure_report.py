#IT infrastructure report

# Your company stores server status.

servers = (
 ("AppServer1", ("192.168.1.10", 65, "Running")),
 ("DBServer1", ("192.168.1.11", 85, "Running")),
 ("CacheServer", ("192.168.1.12", 90, "Down")),
 ("BackupServer", ("192.168.1.13", 40, "Running"))
)

for i,j in servers:
    if j[2]=="Running":
        print("Running Servers: ",i)

max_cpu = -1
max_server = ""
for name, (ip, cpu, status) in servers:
    if cpu > max_cpu:
        max_cpu = cpu
        max_server = name
print("Server with highest CPU usage:",max_server)

high_cpu_servers = []  

for name, (ip, cpu, status) in servers:
    if cpu > 80:
        alert = f"{name} ({cpu}%)"
        high_cpu_servers.append(alert)

if high_cpu_servers:
    print("High CPU Alert:", " | ".join(high_cpu_servers))

for name, (ip, cpu, status) in servers:
    if status == "Down":
        print(f"ALERT: {name} is down at {ip}")


#Sample output

# Running Servers:  AppServer1
# Running Servers:  DBServer1
# Running Servers:  BackupServer
# Server with highest CPU usage: CacheServer
# High CPU Alert: DBServer1 (85%) | CacheServer (90%)
# ALERT: CacheServer is down at 192.168.1.12