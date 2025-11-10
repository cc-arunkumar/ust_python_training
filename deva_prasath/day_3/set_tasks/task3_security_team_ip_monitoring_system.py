# Task 3: Security Team — IP Monitoring System

# Your company’s security team monitors IP addresses connecting to the system.
# Some IPs are suspicious and listed in a blacklist.
# You must analyze connections using sets.

connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}
common=connected_ips-blacklisted_ips
total=connected_ips|blacklisted_ips
print("Blacklisted & Connected: ",connected_ips & blacklisted_ips)
print("All safe IPs: ",connected_ips-blacklisted_ips)
blacklisted_ips.add("10.0.0.9")
for i in common:
    print("ALERT:BLOCKED IP DETECTED- ",i)
print(len(blacklisted_ips))


#Sample output

# Blacklisted & Connected:  {'10.0.0.2', '10.0.0.8'}
# All safe IPs:  {'10.0.0.9', '10.0.0.5', '10.0.0.1'}
# ALERT:BLOCKED IP DETECTED-  10.0.0.9
# ALERT:BLOCKED IP DETECTED-  10.0.0.5
# ALERT:BLOCKED IP DETECTED-  10.0.0.1
# 4