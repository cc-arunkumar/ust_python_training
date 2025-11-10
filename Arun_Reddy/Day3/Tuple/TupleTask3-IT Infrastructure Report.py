# (server_name, (ip_address, cpu_usage%, status))

servers = (
 ("AppServer1", ("192.168.1.10", 65, "Running")),
 ("DBServer1", ("192.168.1.11", 85, "Running")),
 ("CacheServer", ("192.168.1.12", 90, "Down")),
 ("BackupServer", ("192.168.1.13", 40, "Running"))
)

# Print all server names with status = "Running".
mx=0
nme=""
listans=[]
for name,(ipaddress,usage,status) in servers:
    if status=="Running":
        print(name)
    if usage>mx:
        mx=usage
        nme=name
# 2. Find the server with the highest CPU usage.
print("Highest server usage",nme)
# 3. Display all servers that have CPU usage above 80% as:
listans=[]
for name,(ipaddress,usage,status) in servers:
    if usage>80:
        listans.append((name,usage))
print("High CPU Alert:",listans)
# For servers that are “Down”, print:
# ALERT: CacheServer is down at 192.168.1.12
for name,(ipaddress,usage,status) in servers:
    if status=="Down":
        print(f"ALERT: {name} is down at {ipaddress}")


# //////sample execution 
# AppServer1
# DBServer1
# BackupServer
# Highest server usage CacheServer
# High CPU Alert: [('DBServer1', 85), ('CacheServer', 90)]
# ALERT: CacheServer is down at 192.168.1.12


