# TASK 3 - Security Team — IP Monitoring System

connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}

print("Blacklisted & Connected:",connected_ips & blacklisted_ips)

print("Safe IPs:",connected_ips - blacklisted_ips)

blacklisted_ips.add("10.0.0.9")

for ip in connected_ips & blacklisted_ips:
    print(f"ALERT: Blocked IP detected - {ip}")


print("Total Unique Blacklisted IPs:", len(blacklisted_ips))


# ------------------------------------------------------------------------------------

# Sample Output
# Blacklisted & Connected: {'10.0.0.8', '10.0.0.2'}
# Safe IPs: {'10.0.0.9', '10.0.0.1', '10.0.0.5'}
# ALERT: Blocked IP detected - 10.0.0.8
# ALERT: Blocked IP detected - 10.0.0.9
# ALERT: Blocked IP detected - 10.0.0.2
# Total Unique Blacklisted IPs: 4



