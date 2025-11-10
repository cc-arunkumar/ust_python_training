#Task 3: Security Team — IP Monitoring System


#Code 
connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}

diff_set = connected_ips-blacklisted_ips
union_set = connected_ips | blacklisted_ips
blacklisted_ips.add("10.0.0.9")
iteration_set= connected_ips & blacklisted_ips
print("Blacklisted & Connected : ",iteration_set)
print("Safe IPs:  ",diff_set)
for i in iteration_set:
    print("ALERT: Blocked IP detected : ",i)
print("Total Blacklisted IPs: ",len(blacklisted_ips))

#Output
# Blacklisted & Connected :  {'10.0.0.2', '10.0.0.8', '10.0.0.9'}
# Safe IPs:   {'10.0.0.5', '10.0.0.1', '10.0.0.9'}
# ALERT: Blocked IP detected :  10.0.0.2
# ALERT: Blocked IP detected :  10.0.0.8
# ALERT: Blocked IP detected :  10.0.0.9
# Total Blacklisted IPs:  4
