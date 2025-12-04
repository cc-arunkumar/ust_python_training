#Task 3: IT Infrastructure Report

servers=(("AppServer1",("192.168.1.10",65,"Running")),
         ("DBServer1",("192.168.1.11",85,"Running")),
         ("CacheServer",("192.168.1.12",90,"Down")),
         ("BackupServer",("192.168.1.13",40,"Running"))
         )

for server_name,(ip_address,cpu_usage,status) in servers:
    if status=="Running":
        print(server_name)


highest_cpu_server = max(servers, key=lambda s: s[1][1])
print(f"\nHighest CPU Usage: {highest_cpu_server[0]} ({highest_cpu_server[1][1]}%)")

for server_name, (ip_address, cpu_usage, status) in servers:
    if cpu_usage > 80:
        print(f"High CPU Alert:{server_name}(85%)|{server_name}")

for server_name, (ip_address, cpu_usage, status) in servers:
    if status == "Down":
        print(f"ALERT: {server_name} is down at {ip_address}")

high_cpu_alerts = []
for server_name, (ip_address, cpu_usage, status) in servers:
    if cpu_usage > 80:
        high_cpu_alerts.append(f"{server_name} ({cpu_usage}%)")

if high_cpu_alerts:
    print("High CPU Alert:", " | ".join(high_cpu_alerts))

'''
Output:
AppServer1
DBServer1
BackupServer

Highest CPU Usage: CacheServer (90%)
High CPU Alert:DBServer1(85%)|DBServer1
High CPU Alert:CacheServer(85%)|CacheServer
ALERT: CacheServer is down at 192.168.1.12
High CPU Alert: DBServer1 (85%) | CacheServer (90%)
'''