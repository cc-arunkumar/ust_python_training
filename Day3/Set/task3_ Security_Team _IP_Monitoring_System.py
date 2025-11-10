connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}

print("Blacklisted & Connected: ",connected_ips & blacklisted_ips)
print("Safe IPs: ",connected_ips - blacklisted_ips)
blacklisted_ips.add("10.0.0.9")

l=list(connected_ips & blacklisted_ips)
for i in l:
    print("ALERT: Blocked IP detected - ",i)


print("Total Blacklisted IPs: ",len(blacklisted_ips))

# output

# Blacklisted & Connected:  {'10.0.0.8', '10.0.0.2'}
# Safe IPs:  {'10.0.0.9', '10.0.0.5', '10.0.0.1'}
# ALERT: Blocked IP detected -  10.0.0.9
# ALERT: Blocked IP detected -  10.0.0.8
# ALERT: Blocked IP detected -  10.0.0.2
# Total Blacklisted IPs:  4