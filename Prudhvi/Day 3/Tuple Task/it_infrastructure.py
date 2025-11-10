servers = (
 ("AppServer1", ("192.168.1.10", 65, "Running")),
 ("DBServer1", ("192.168.1.11", 85, "Running")),
 ("CacheServer", ("192.168.1.12", 90, "Down")),
 ("BackupServer", ("192.168.1.13", 40, "Running"))
)

for name, (ip, cpu, status) in servers:
    if status == "Running":
        print(name)

high = 0
server = ""
for name, (ip, cpu, status) in servers:
    if cpu > high:
        high = cpu
        server = ip
print(server)

name_high = []
high_cpu = 80
for name, (ip, cpu, status) in servers:
    if cpu > 80:
        name_high.append(f"{name} ({cpu}%)")
print(f" " .join(name_high))


for name, (ip, cpu, status) in servers:
    if status == "Down":
        print(f"ALERT: {name} is down at {ip}")

#sample output
# AppServer1
# DBServer1
# BackupServer
# 192.168.1.12
# DBServer1 (85%) CacheServer (90%)
# ALERT: CacheServer is down at 192.168.1.12
# PS C:\Users\303464\Desktop\Training> 