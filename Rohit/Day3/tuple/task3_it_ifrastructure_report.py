# Task 3:IT Infrastructure Report
# Scenario:
# You have nested tuples representing company servers and their configuration
# details.

# Step 1: Define server data as a tuple of server records
servers = (
    ("AppServer1", ("192.168.1.10", 65, "Running")),
    ("DBServer1", ("192.168.1.11", 95, "Running")),
    ("CacheServer", ("192.168.1.12", 90, "Down")),
    ("BackupServer", ("192.168.1.13", 40, "Running"))
)

# Step 2: Set CPU threshold and initialize variable to track highest usage
minimum = 80
highest_server = ''

# Step 3: Iterate through each server record
for name, (ip, cpu, status) in servers:

    # Step 4: Check if CPU usage is above or equal to threshold
    if cpu >= 80:
        highest_server = name
        print(f"Server with the highest CPU usage: {highest_server} ({cpu}%)")

    # Step 5: Print servers that are currently running
    if status == 'Running':
        print(f"{name} is running.")

    # Step 6: Print servers with CPU usage above the minimum threshold
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