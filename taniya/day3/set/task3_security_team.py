connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}
print(blacklisted_ips.intersection(connected_ips))
blacklisted_ips.add("10.0.0.9")
print(blacklisted_ips)

inter_conn=connected_ips.intersection(blacklisted_ips)
for ip in inter_conn:
    print("ALERT:Blocked IP detected: {ip}")
    print("ALERT:Blocked IP dtected:",len(blacklisted_ips))

# output
# {'10.0.0.2', '10.0.0.8'}
# {'10.0.0.2', '10.0.0.9', '10.0.0.10', '10.0.0.8'}
# ALERT:Blocked IP detected: {ip}
# ALERT:Blocked IP dtected: 4
# ALERT:Blocked IP detected: {ip}
# ALERT:Blocked IP dtected: 4
# ALERT:Blocked IP detected: {ip}
# ALERT:Blocked IP dtected: 4