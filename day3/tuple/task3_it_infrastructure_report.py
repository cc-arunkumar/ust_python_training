servers = (
    ("AppServer1", ("192.168.1.10", 65, "Running")),
    ("DBServer1", ("192.168.1.11", 85, "Running")),
    ("CacheServer", ("192.168.1.12", 90, "Down")),
    ("BackupServer", ("192.168.1.13", 40, "Running"))
)

print("Servers with status 'Running':")
for name, (ip, cpu, status) in servers:
    if status == "Running":
        print(name)
max_usage = 0
server=""
for(server_name,(ip,cpu,status)) in servers:
    if cpu >max_usage:
        max_usage = cpu
        server = server_name
print(server)

for(server_name,(ip,cpu,status)) in servers:
    if cpu >80:
        print(server_name)
for(server_name,(ip,cpu,status)) in servers:
    if status == 'Down':
        print("servers that are down:",ip)


# output
# Servers with status 'Running':
# AppServer1
# DBServer1
# BackupServer
# CacheServer
# DBServer1
# CacheServer
# servers that are down: 192.168.1.12
