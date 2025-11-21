"""
Task 3: Security Team — IP Monitoring System
Scenario:
Your company’s security team monitors IP addresses connecting to the system.
Some IPs are suspicious and listed in a blacklist.
You must analyze connections using sets

"""

# Set of currently connected IP addresses
connected_ips={"10.0.0.1","10.0.0.2","10.0.0.5","10.0.0.8","10.0.0.9"}

# Set of blacklisted IP addresses
blacklisted_ips={"10.0.0.2","10.0.0.8","10.0.0.10"}

# IPs that are both connected and blacklisted
blacklisted_connected=connected_ips.intersection(blacklisted_ips)
print("Blacklisted & Connected:",blacklisted_connected)

# Connected IPs that are not blacklisted
safe_ips=connected_ips.difference(blacklisted_ips)
print("Safe IPs:",safe_ips)

# Adding a new IP to the blacklist
blacklisted_ips.add("10.0.0.9")

# Alert for each connected IP that is in blacklist
for ip in connected_ips:
    if ip in blacklisted_ips:
        print(f"ALERT: Blocked IP detected - {ip}")

# Total number of blacklisted IPs
print("Total Blacklisted IPs:",len(blacklisted_ips))


# sample output

"""
Blacklisted & Connected: {'10.0.0.2', '10.0.0.8'}
Safe IPs: {'10.0.0.5', '10.0.0.1', '10.0.0.9'}
ALERT: Blocked IP detected - 10.0.0.8
ALERT: Blocked IP detected - 10.0.0.2
ALERT: Blocked IP detected - 10.0.0.9
Total Blacklisted IPs: 4

"""
