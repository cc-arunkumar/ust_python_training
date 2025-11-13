servers = (
 ("AppServer1", ("192.168.1.10", 65, "Running")),
 ("DBServer1", ("192.168.1.11", 85, "Running")),
 ("CacheServer", ("192.168.1.12", 90, "Down")),
 ("BackupServer", ("192.168.1.13", 40, "Running"))
)

high_cpu = servers[0][1]
server_name = ""

for name,details in servers:
    status = details[2]
    if(status == "Running"):
        print(f"{name} is {status}")
    cpu_per = details[1]
    if cpu_per > high_cpu:
        high_cpu = cpu_per
        server_name=name
print(f"CPU with highest usage is:{server_name}")