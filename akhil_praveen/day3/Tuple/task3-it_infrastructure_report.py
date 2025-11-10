# IT_Infrastructure_Report

servers = (
 ("AppServer1", ("192.168.1.10", 65, "Running")),
 ("DBServer1", ("192.168.1.11", 85, "Running")),
 ("CacheServer", ("192.168.1.12", 90, "Down")),
 ("BackupServer", ("192.168.1.13", 40, "Running"))
)
max_usage=0
max_name=""
print("All server names with status = \"Running\"")
for name, (ip, cpu, status) in servers:
    if status=="Running":
        print(name)
    if max_usage<cpu:
        max_usage=cpu
        max_name=name
print()
print("Server with the highest CPU usage: ",max_name)
print()
for name, (ip, cpu, status) in servers:
    if cpu>80:
        print(f"High CPU Alert:{name} ({cpu}%)")
    if status=="Down":
        print(f"Alert:{name} is down at {ip}")
print()

# All server names with status = "Running"
# AppServer1
# DBServer1
# BackupServer

# Server with the highest CPU usage:  CacheServer

# High CPU Alert:DBServer1 (85%)
# High CPU Alert:CacheServer (90%)
# Alert:CacheServer is down at 192.168.1.12