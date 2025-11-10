
servers = (
 ("AppServer1", ("192.168.1.10", 65, "Running")),
 ("DBServer1", ("192.168.1.11", 85, "Running")),
 ("CacheServer", ("192.168.1.12", 90, "Down")),
 ("BackupServer", ("192.168.1.13", 40, "Running"))
)


#  Print all server names with status = "Running".

for server_name, (ip_address,cpu_usage,status) in servers:
    if status == "Running":
        print("status = Running:",server_name)


# ind the server with the highest CPU usage
max=0
names=""
for server_name, (ip_address,cpu_usage,status) in servers:
    if cpu_usage>max:
        max=cpu_usage
        names=server_name
        print(f"server with the highest CPU usage:{names}")

#  Display all servers that have CPU usage above 80% as:
name=[]
for server_name, (ip_address,cpu_usage,status) in servers:
    if cpu_usage>80:
        name.append(f"{server_name},{cpu_usage}")
print(f"cpu usage:{name}")


# For servers that are “Down”, print


for server_name, (ip_address,cpu_usage,status) in servers:
    if status=="Down":
        print(f"ALERT:{server_name} is down at {ip_address}")



# output
# status = Running: AppServer1
# status = Running: DBServer1
# status = Running: BackupServer
# server with the highest CPU usage:AppServer1
# server with the highest CPU usage:DBServer1
# server with the highest CPU usage:CacheServer
# cpu usage:['DBServer1,85', 'CacheServer,90']
# ALERT:CacheServer is down at 192.168.1.12


        


