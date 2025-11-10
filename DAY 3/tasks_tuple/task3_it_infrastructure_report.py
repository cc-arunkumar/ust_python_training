"""
Task 3:IT Infrastructure Report
Scenario:
You have nested tuples representing company servers and their configuration
details.

Each tuple in the list looks like:
(server_name, (ip_address, cpu_usage%, status))
Example:
servers = (
 ("AppServer1", ("192.168.1.10", 65, "Running")),
 ("DBServer1", ("192.168.1.11", 85, "Running")),
 ("CacheServer", ("192.168.1.12", 90, "Down")),
 ("BackupServer", ("192.168.1.13", 40, "Running"))
)

"""


servers = (
 ("AppServer1", ("192.168.1.10", 65, "Running")),
 ("DBServer1", ("192.168.1.11", 85, "Running")),
 ("CacheServer", ("192.168.1.12", 90, "Down")),
 ("BackupServer", ("192.168.1.13", 40, "Running"))
)


high_cpu_usage=0
high_cpu_server=""
high_cpu_list=[]

for server_name, (ip,cpu,status) in servers:
    if cpu>high_cpu_usage:
        high_cpu_usage=cpu 
        high_cpu_server=server_name

    # Servers running
    if status=="Running":
        print(server_name)

    # CPU ABOVE 80%
    if cpu>80:
        high_cpu_list.append(f"{server_name} ({cpu}%)")

    # SERVER DOWN 
    if status=="Down":
        print(f"ALERT: CacheServer is down at {ip}")

if high_cpu_list:
    print("High CPU Alert: " + " | ".join(high_cpu_list))
# HIGH CUP USAGE
print(f"Server with the highest CPU usage {high_cpu_server}")        


# sample output

"""
AppServer1
DBServer1
ALERT: CacheServer is down at 192.168.1.12
BackupServer
High CPU Alert: DBServer1 (85%) | CacheServer (90%)
Server with the highest CPU usage CacheServer

"""