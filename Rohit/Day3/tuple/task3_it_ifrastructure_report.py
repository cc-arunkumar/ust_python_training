servers = (
    ("AppServer1", ("192.168.1.10", 65, "Running")),
    ("DBServer1", ("192.168.1.11", 95, "Running")),
    ("CacheServer", ("192.168.1.12", 90, "Down")),
    ("BackupServer", ("192.168.1.13", 40, "Running"))
)

minimum = 80
highest_server = ''

for name, (ip, cpu, status) in servers:
    # print(cpu)
    if cpu >= 80:
        # print(cpu)
        highest_server = name
        print(f"Server with the highest CPU usage: {highest_server} ({cpu}%)")

    if status == 'Running':
        print(f"{name} is running.")

    if cpu > minimum:
        print(f"{name} has CPU usage above {minimum}%.")

# =============sample output =====================
# AppServer1 is running.
# Server with the highest CPU usage: DBServer1 (95%)
# DBServer1 is running.
# DBServer1 has CPU usage above 80%.
# Server with the highest CPU usage: CacheServer (90%)
# CacheServer has CPU usage above 80%.
# BackupServer is running.