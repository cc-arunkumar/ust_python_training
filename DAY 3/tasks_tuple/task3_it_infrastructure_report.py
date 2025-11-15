"""
Task 3: IT Infrastructure Report
Scenario:
Nested tuples represent company servers and their configuration details.
Each tuple:
(server_name, (ip_address, cpu_usage%, status))
"""

servers=(("AppServer1",("192.168.1.10",65,"Running")),
         ("DBServer1",("192.168.1.11",85,"Running")),
         ("CacheServer",("192.168.1.12",90,"Down")),
         ("BackupServer",("192.168.1.13",40,"Running")))

high_cpu_usage=0  # Track highest CPU usage
high_cpu_server=""  # Server with highest CPU
high_cpu_list=[]  # List of servers with CPU > 80%

for server_name,(ip,cpu,status) in servers:
    if cpu>high_cpu_usage:  # Update highest CPU server
        high_cpu_usage=cpu
        high_cpu_server=server_name
    if status=="Running":  # Print running servers
        print(server_name)
    if cpu>80:  # Track high CPU servers
        high_cpu_list.append(f"{server_name} ({cpu}%)")
    if status=="Down":  # Alert for down server
        print(f"ALERT: {server_name} is down at {ip}")

if high_cpu_list:  # Print all high CPU servers
    print("High CPU Alert: "+" | ".join(high_cpu_list))
print(f"Server with the highest CPU usage {high_cpu_server}")  # Highest CPU server
