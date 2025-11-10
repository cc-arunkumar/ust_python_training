servers = (
 ("AppServer1", ("192.168.1.10", 65, "Running")),
 ("DBServer1", ("192.168.1.11", 85, "Running")),
 ("CacheServer", ("192.168.1.12", 90, "Down")),
 ("BackupServer", ("192.168.1.13", 40, "Running"))
)

for (server_name, (ip_address, cpu_usage , status)) in servers:
    if(status=="Running"):
        print(server_name)


max_usage=0
server=""
for (server_name, (ip_address, cpu_usage, status)) in servers:
    if cpu_usage > max_usage:
        max_usage = cpu_usage
        server = server_name
print(server)

for (server_name, (ip_address, cpu_usage, status)) in servers:
    if cpu_usage>80:
        print(server_name)


for (server_name, (ip_address, cpu_usage, status)) in servers:
    if status == "Down":
        print(f"\nALERT: {server_name} is down at {ip_address}")


# AppServer1
# DBServer1
# BackupServer

# CacheServer

# DBServer1
# CacheServer

# ALERT: CacheServer is down at 192.168.1.12