# Task 3: Security Team — IP Monitoring System
connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}

# 1. Print all IPs that are blacklisted and currently connected.
print("Blacklisted & Connected:", connected_ips & blacklisted_ips)

# 2. Print all safe IPs — connected but not blacklisted.
print("Safe IPs:",connected_ips-blacklisted_ips)

# 3. A new suspicious IP "10.0.0.9" is detected — add it to blacklisted_ips .
blacklisted_ips.add("10.0.0.9")

# 4. Print an alert message for each IP that’s currently connected and blacklisted:
intersect_set=connected_ips&blacklisted_ips
for i in intersect_set:
    print(f"ALERT: Blocked IP detected -{i}")

# 5. Finally, display total unique blacklisted IPs in your system.
print("Total Blacklisted IPs:",blacklisted_ips)

# Sample output
# Blacklisted & Connected: {'10.0.0.8', '10.0.0.2'}
# Safe IPs: {'10.0.0.9', '10.0.0.1', '10.0.0.5'}
# ALERT: Blocked IP detected -10.0.0.9
# ALERT: Blocked IP detected -10.0.0.8
# ALERT: Blocked IP detected -10.0.0.2
# Total Blacklisted IPs: {'10.0.0.9', '10.0.0.10', '10.0.0.8', '10.0.0.2'}