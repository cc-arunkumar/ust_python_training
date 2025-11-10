#Task 3:IT Infrastructure Report
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