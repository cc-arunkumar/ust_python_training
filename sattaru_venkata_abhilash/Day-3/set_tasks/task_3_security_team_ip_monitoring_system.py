# Task 3: Security Team — IP Monitoring System
# Scenario:
# Your company’s security team monitors IP addresses connecting to the system.
# Some IPs are suspicious and listed in a blacklist.

# Given sets
connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}

# 1. Print all IPs that are blacklisted and currently connected
ips = connected_ips & blacklisted_ips
print("Blacklisted & Connected:", ips)

# 2. Print all safe IPs — connected but not blacklisted
safe_ips = connected_ips - blacklisted_ips
print("Safe IPs:", safe_ips)

# 3. Add new suspicious IP "10.0.0.9" to blacklisted_ips
blacklisted_ips.add("10.0.0.9")

# 4. Print alert for each IP that’s both connected and blacklisted
ips = connected_ips & blacklisted_ips
for ip in ips:
    print(f"ALERT: Blocked IP detected - {ip}")

# 5. Display total unique blacklisted IPs in the system
print("Total Blacklisted IPs:", len(blacklisted_ips))


# Sample Output:
# Blacklisted & Connected: {'10.0.0.2', '10.0.0.8'}
# Safe IPs: {'10.0.0.1', '10.0.0.9', '10.0.0.5'}
# ALERT: Blocked IP detected - 10.0.0.9
# ALERT: Blocked IP detected - 10.0.0.8
# ALERT: Blocked IP detected - 10.0.0.2
# Total Blacklisted IPs: 4