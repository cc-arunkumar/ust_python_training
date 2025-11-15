# Task 3: Security Team — IP Monitoring
# System
# Scenario:
# Your company’s security team monitors IP addresses connecting to the system.
# Some IPs are suspicious and listed in a blacklist.
# You must analyze connections using sets.
# Instructions:
# connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
# blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}
# Tasks:
# 1. Print all IPs that are blacklisted and currently connected.
# (Hint: intersection)
# 2. Print all safe IPs — connected but not blacklisted.
# (Hint: difference)
# 3. A new suspicious IP "10.0.0.9" is detected — add it to blacklisted_ips .
# Set Tasks 3
# 4. Print an alert message for each IP that’s currently connected and blacklisted:
# ALERT: Blocked IP detected - 10.0.0.2
# ALERT: Blocked IP detected - 10.0.0.8
# ...
# 5. Finally, display total unique blacklisted IPs in your system.


connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}

# Print all IPs that are blacklisted and currently connected
blocked_connected = connected_ips.intersection(blacklisted_ips)
print("Blacklisted & Connected:", blocked_connected)

# Print all safe IPs — connected but not blacklisted
safe_ips = connected_ips.difference(blacklisted_ips)
print("Safe IPs:", safe_ips)

# Add new suspicious IP to blacklisted_ips
blacklisted_ips.add("10.0.0.9")

# Print alert messages for each blacklisted and connected IP
inter=connected_ips.intersection(blacklisted_ips)
for ip in inter :
    print(f"ALERT: Blocked IP detected → {ip}")

print("Total Blacklisted IPs:", len(blacklisted_ips))

# Blacklisted & Connected: {'10.0.0.2', '10.0.0.8'}
# Safe IPs: {'10.0.0.9', '10.0.0.1', '10.0.0.5'}
# ALERT: Blocked IP detected → 10.0.0.9
# ALERT: Blocked IP detected → 10.0.0.2
# ALERT: Blocked IP detected → 10.0.0.8
# Total Blacklisted IPs: 4