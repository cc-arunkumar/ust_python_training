# #Task 3:IT Infrastructure Report
# Scenario:
# You have nested tuples representing company servers and their configuration
# details.
# Each tuple in the list looks like:
# (server_name, (ip_address, cpu_usage%, status))
# Example:
# servers = (
#  ("AppServer1", ("192.168.1.10", 65, "Running")),
#  ("DBServer1", ("192.168.1.11", 85, "Running")),
#  ("CacheServer", ("192.168.1.12", 90, "Down")),
#  ("BackupServer", ("192.168.1.13", 40, "Running"))
# )
# Your Tasks:
# 1. Print all server names with status = "Running".
# 2. Find the server with the highest CPU usage.
# 3. Display all servers that have CPU usage above 80% as:
# High CPU Alert: DBServer1 (85%) | CacheServer (90%)
# 4. For servers that are “Down”, print:
# ALERT: CacheServer is down at 192.168.1.12

servers = (
 ("AppServer1", ("192.168.1.10", 65, "Running")),
 ("DBServer1", ("192.168.1.11", 85, "Running")),
 ("CacheServer", ("192.168.1.12", 90, "Down")),
 ("BackupServer", ("192.168.1.13", 40, "Running"))
)

highest=0
name=""
highusage=[]
down=[]
for (server_name, (ip_address, cpu_usage, status)) in servers:
    if(status=="Running"):
        print(server_name)
    if(cpu_usage>highest):
        highest=cpu_usage
        name=server_name
    if(cpu_usage>80):
        one=[server_name,cpu_usage]
        highusage.append(one)
    if(status=="Down"):
        two=[server_name,ip_address]
        down.append(two)

print("Highest cpu usage: ",name,highest,"%")

print("High CPU Alert: ",end="")
for str,usage in highusage:
    print(str,"(",usage,"%)",end=" | ")
print()
for str,ip in down:
    print("ALERT: ",str,"is down at ",ip)


#Sample output
# AppServer1
# DBServer1
# BackupServer
# Highest cpu usage:  CacheServer 90 %
# High CPU Alert: DBServer1 ( 85 %) | CacheServer ( 90 %) | 
# ALERT:  CacheServer is down at  192.168.1.12