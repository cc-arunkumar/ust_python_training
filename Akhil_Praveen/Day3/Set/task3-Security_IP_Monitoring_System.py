connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}
print("IPs that are blacklisted and currently connected: ", connected_ips.intersection(blacklisted_ips))
print("All safe IPs: ",connected_ips.difference(blacklisted_ips))
blacklisted_ips.add("10.0.0.9")
for i in connected_ips.intersection(blacklisted_ips):
    print("ALERT: Blocked IP detected - ", i)
print("Total Blacklisted IPs: ",len(blacklisted_ips))


# IPs that are blacklisted and currently connected:  {'10.0.0.8', '10.0.0.2'}
# All safe IPs:  {'10.0.0.1', '10.0.0.9', '10.0.0.5'}
# ALERT: Blocked IP detected -  10.0.0.9
# ALERT: Blocked IP detected -  10.0.0.8
# ALERT: Blocked IP detected -  10.0.0.2
# Total Blacklisted IPs:  4