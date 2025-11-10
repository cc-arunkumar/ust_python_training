# Task 3:IT Infrastructure Report
# Scenario:
# You have nested tuples representing company servers and their configuration
# details.

servers = (
 ("AppServer1", ("192.168.1.10", 65, "Running")),
 ("DBServer1", ("192.168.1.11", 85, "Running")),
 ("CacheServer", ("192.168.1.12", 90, "Down")),
 ("BackupServer", ("192.168.1.13", 40, "Running"))
 )

print(f"Server Name with Status Running:")
high = 0
high_name=""

for (server,(add,per,status)) in servers:
    
    if(status=="Running"):
        print(server)
    if(per>high):
        high=per
        high_name=server
    if(per>80):
        print(server)
print(f"server with the highest CPU usage:{high_name}")

# sample output:

# IT_infrastructure_report.py
# Server Name with Status Running:
# AppServer1
# DBServer1
# DBServer1
# CacheServer
# BackupServer
# server with the highest CPU usage:CacheServer