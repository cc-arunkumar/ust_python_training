#Task 3:IT Infrastructure Report
servers = (
 ("AppServer1", ("192.168.1.10", 65, "Running")),
 ("DBServer1", ("192.168.1.11", 85, "Running")),
 ("CacheServer", ("192.168.1.12", 90, "Down")),
 ("BackupServer", ("192.168.1.13", 40, "Running"))
)
maxi=servers[0][1][1]
maxi_name=servers[0][0]
for name,ip in servers:
    if(ip[2]=="Running"):
        print("Running",name)
    if(ip[1]>maxi):
        maxi=ip[1]
        maxi_name=name
    if(ip[1]>80):
        print(f"High CPU Alert: {name}({ip[1]}%)")
    if(ip[2]=="Down"):
        print(f"ALERT: {name} is down at {ip[0]}")
print("Maximum",maxi_name)
#Output
# Running AppServer1
# Running DBServer1
# High CPU Alert: DBServer1(85%)
# High CPU Alert: CacheServer(90%)
# ALERT: CacheServer is down at 192.168.1.12
# Running BackupServer
# Maximum CacheServer