# Task 3: Security Team — IP Monitoring System

# Your company’s security team monitors IP addresses connecting to the system.
# Some IPs are suspicious and listed in a blacklist.
# You must analyze connections using sets.

# Sets representing connected and blacklisted IP addresses
connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}

# Find the common IPs between connected and blacklisted (intersection)
common = connected_ips & blacklisted_ips

# Find all unique IPs in both sets (union)
total = connected_ips | blacklisted_ips

# Print common blacklisted and connected IPs
print("Blacklisted & Connected: ", connected_ips & blacklisted_ips)

# Print all safe (non-blacklisted) connected IPs
print("All safe IPs: ", connected_ips - blacklisted_ips)

# Add a new blacklisted IP
blacklisted_ips.add("10.0.0.9")

# Print alert for each blocked IP detected
for i in common:
    print("ALERT: BLOCKED IP DETECTED- ", i)

# Print the total number of blacklisted IPs
print(len(blacklisted_ips))



#Sample output

# Blacklisted & Connected:  {'10.0.0.2', '10.0.0.8'}
# All safe IPs:  {'10.0.0.9', '10.0.0.5', '10.0.0.1'}
# ALERT:BLOCKED IP DETECTED-  10.0.0.9
# ALERT:BLOCKED IP DETECTED-  10.0.0.5
# ALERT:BLOCKED IP DETECTED-  10.0.0.1
# 4