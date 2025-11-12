# Task 3: Security Team — IP Monitoring
# System
# Scenario:
# Your company’s security team monitors IP addresses connecting to the system.
# Some IPs are suspicious and listed in a blacklist.


# Step 1: Initialize sets of connected and blacklisted IPs
connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}

# Step 2: Find IPs that are both connected and blacklisted
print(" IPs that are both connected and blacklisted")
print(connected_ips.intersection(blacklisted_ips))  # Common IPs

# Step 3: Find IPs that are connected but not blacklisted
print("IPs that are connected but not blacklisted")
print(connected_ips.difference(blacklisted_ips))  # Safe IPs

# Step 4: Add a new IP to the blacklist
blacklisted_ips.add("10.0.0.9")  # Now 10.0.0.9 is blacklisted too

# Step 5: Print all unique IPs from both sets
print("all unique IPs from both sets")
for i in connected_ips.union(blacklisted_ips):
    print(i)

# Step 6: Print the total number of unique IPs
print("the total number of unique IPs")
print(len(connected_ips.union(blacklisted_ips)))




# ========sample output =====================
# IPs that are both connected and blacklisted
# {'10.0.0.2', '10.0.0.8'}
# IPs that are connected but not blacklisted
# {'10.0.0.9', '10.0.0.1', '10.0.0.5'}
# all unique IPs from both sets
# 10.0.0.2
# 10.0.0.5
# 10.0.0.9
# 10.0.0.1
# 10.0.0.8
# 10.0.0.10
# the total number of unique IPs
# 6

