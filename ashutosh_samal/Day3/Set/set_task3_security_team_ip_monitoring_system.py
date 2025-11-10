#Task 3: Security Team — IP Monitoring

connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}

print("Blacklisted & Connected:",connected_ips.intersection(blacklisted_ips))
print("Safe IPs:",connected_ips.difference(blacklisted_ips))

blacklisted_ips.add("10.0.0.9")

for ip in connected_ips:
    if ip in blacklisted_ips:
        print("ALERT: Blocked IP detected -",ip)

print("Total Blacklisted IPs:",len(blacklisted_ips))

#Sample Execution
# Blacklisted & Connected: {'10.0.0.2', '10.0.0.8'}
# Safe IPs: {'10.0.0.9', '10.0.0.5', '10.0.0.1'}
# ALERT: Blocked IP detected - 10.0.0.9
# ALERT: Blocked IP detected - 10.0.0.2
# ALERT: Blocked IP detected - 10.0.0.8
# Total Blacklisted IPs: 4
