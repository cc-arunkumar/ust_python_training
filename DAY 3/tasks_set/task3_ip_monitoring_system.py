"""
Task 3: Security Team — IP Monitoring System
Scenario:
Your company’s security team monitors IP addresses connecting to the system.
Some IPs are suspicious and listed in a blacklist.
You must analyze connections using sets

"""


connected_ips={"10.0.0.1","10.0.0.2","10.0.0.5","10.0.0.8","10.0.0.9"}
blacklisted_ips={"10.0.0.2","10.0.0.8","10.0.0.10"}
blacklisted_connected=connected_ips.intersection(blacklisted_ips)

print("Blacklisted & Connected:",blacklisted_connected)

safe_ips=connected_ips.difference(blacklisted_ips)
print("Safe IPs:",safe_ips)

blacklisted_ips.add("10.0.0.9")

for ip in connected_ips:
    if ip in blacklisted_ips:
        print(f"ALERT: Blocked IP detected - {ip}")
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