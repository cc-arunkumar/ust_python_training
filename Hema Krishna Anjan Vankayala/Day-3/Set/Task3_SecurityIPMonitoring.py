#Task 3: Security Team — IP Monitoring System
connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}
connected_blacklisted = connected_ips.intersection(blacklisted_ips)
print("Blacklisted & Connected:",connected_blacklisted)
print("Safe IPs:",connected_ips.difference(blacklisted_ips))
blacklisted_ips.add("10.0.0.9")
for i in list(connected_ips.intersection(blacklisted_ips)):
    print(f"ALERT: Blocked IP detected - ",i)
print("Total Blacklisted IPs: ",len(blacklisted_ips))

#Sample Output
# Blacklisted & Connected: {'10.0.0.2', '10.0.0.8'}
# Safe IPs: {'10.0.0.9', '10.0.0.5', '10.0.0.1'}
# ALERT: Blocked IP detected -  10.0.0.2
# ALERT: Blocked IP detected -  10.0.0.8
# ALERT: Blocked IP detected -  10.0.0.9
# Total Blacklisted IPs:  4