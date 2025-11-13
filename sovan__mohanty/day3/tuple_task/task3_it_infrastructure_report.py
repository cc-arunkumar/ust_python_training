#Task 3 IT Infrastructure Report

servers = (
 ("AppServer1", ("192.168.1.10", 65, "Running")),
 ("DBServer1", ("192.168.1.11", 85, "Running")),
 ("CacheServer", ("192.168.1.12", 90, "Down")),
 ("BackupServer", ("192.168.1.13", 40, "Running"))
)
high_cpu=0
for server_name, (ip_address, cpu_usage, status) in servers:
    if(status=="Running"):
        print("Server Names with All Server Running: ",server_name)
    if(cpu_usage>high_cpu):
        high_cpu=cpu_usage
for server_name, (ip_address, cpu_usage, status) in servers:
    if(high_cpu==cpu_usage):
        print("Server with high cpu: ",server_name)

for server_name, (ip_address, cpu_usage, status) in servers:
    if(cpu_usage>80):
        print(f"High CPU Alert: {server_name} ({cpu_usage}%) |",end="")
    if(status=="Down"):
        print(f"ALERT: {server_name} is down at {ip_address}")

# Sample Execution
# Server Names with All Server Running:  AppServer1
# Server Names with All Server Running:  DBServer1
# Server Names with All Server Running:  BackupServer
# Server with high cpu:  CacheServer
# High CPU Alert: DBServer1 (85%) |High CPU Alert: CacheServer (90%) |ALERT: CacheServer is down at 192.168.1.12
