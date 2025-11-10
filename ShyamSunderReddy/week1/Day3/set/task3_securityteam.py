#Task 3: Security Team — IP Monitoring System
connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}
print("Blacklisted & Connected: ",blacklisted_ips&connected_ips)
print("Safe IPs: ",connected_ips-blacklisted_ips)
blacklisted_ips.add( "10.0.0.9" )
connblack=list(connected_ips&blacklisted_ips)
for str in connblack:
    print("ALERT: Blocked IP detected -",str)
print("Total Blacklisted IPs: ",len(blacklisted_ips))

#sample output
# Blacklisted & Connected:  {'10.0.0.8', '10.0.0.2'}
# Safe IPs:  {'10.0.0.5', '10.0.0.1', '10.0.0.9'}
# ALERT: Blocked IP detected - 10.0.0.8
# ALERT: Blocked IP detected - 10.0.0.2
# ALERT: Blocked IP detected - 10.0.0.9
# Total Blacklisted IPs:  4