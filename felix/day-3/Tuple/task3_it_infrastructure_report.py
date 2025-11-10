# IT_Infrastructure_Report

servers = (
 ("AppServer1", ("192.168.1.10", 65, "Running")),
 ("DBServer1", ("192.168.1.11", 85, "Running")),
 ("CacheServer", ("192.168.1.12", 90, "Down")),
 ("BackupServer", ("192.168.1.13", 40, "Running"))
)

print("Server in running:")
max=servers[0][1][1]
high_cpu = servers[0][0]

for (name,(ip,cpu,status)) in servers:
    if status == "Running":
        print(name)    
    if cpu>max:
        max=cpu
        high_cpu = name

print("High CPU Alert: ",end="")
for (name,(ip,cpu,status)) in servers:
    if cpu>80:
        print(f"{name}({cpu}%)|",end="")
        
print("\nAlert: ",end="")
for (name,(ip,cpu,status)) in servers:
    if status=="Down":
        print(f"{name} is down at ({ip})|",end="")


# output

# Server in running:
# AppServer1
# DBServer1
# BackupServer
# High CPU Alert: DBServer1(85%)|CacheServer(90%)|
# Alert: CacheServer is down at (192.168.1.12)|