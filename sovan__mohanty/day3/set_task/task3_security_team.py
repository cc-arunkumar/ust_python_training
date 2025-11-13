#Task3 Security Team — IP Monitoring System
connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}
print("Blacklisted & Connected: ",connected_ips & blacklisted_ips)
print("Safe IPs: ",connected_ips-blacklisted_ips)
blacklisted_ips.add("10.0.0.9")
new_list=connected_ips & blacklisted_ips
for i in new_list:
    print("ALERT: Blocked IP detected: ",i)
print("Total unique blacklisted ip: ",len(blacklisted_ips))
#Sample Execution
# Blacklisted & Connected:  {'10.0.0.2', '10.0.0.8'}
# Safe IPs:  {'10.0.0.1', '10.0.0.9', '10.0.0.5'}
# ALERT: Blocked IP detected:  10.0.0.2
# ALERT: Blocked IP detected:  10.0.0.9
# ALERT: Blocked IP detected:  10.0.0.8
# Total unique blacklisted ip:  4