#Task 3: Security Team — IP Monitoring

# Sets representing connected IPs and blacklisted IPs
connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}

# Printing blacklisted IPs that are currently connected (intersection of both sets)
print("Blacklisted & Connected:", connected_ips.intersection(blacklisted_ips))

# Printing connected IPs that are not blacklisted (difference between connected_ips and blacklisted_ips)
print("Safe IPs:", connected_ips.difference(blacklisted_ips))

# Adding a new IP to the blacklisted IPs set
blacklisted_ips.add("10.0.0.9")

# Checking if any connected IP is now blacklisted, and printing an alert for each blocked IP
for ip in connected_ips:
    if ip in blacklisted_ips:
        print("ALERT: Blocked IP detected -", ip)

# Printing the total number of blacklisted IPs
print("Total Blacklisted IPs:", len(blacklisted_ips))

#Sample Execution
# Blacklisted & Connected: {'10.0.0.2', '10.0.0.8'}
# Safe IPs: {'10.0.0.9', '10.0.0.5', '10.0.0.1'}
# ALERT: Blocked IP detected - 10.0.0.9
# ALERT: Blocked IP detected - 10.0.0.2
# ALERT: Blocked IP detected - 10.0.0.8
# Total Blacklisted IPs: 4
