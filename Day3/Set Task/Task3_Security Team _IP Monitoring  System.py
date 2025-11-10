connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}

blocked_connected = connected_ips.intersection(blacklisted_ips)
print("Blacklisted & Connected:", blocked_connected)

safe_ips = connected_ips.difference(blacklisted_ips)
print("Safe IPs:", safe_ips)

blacklisted_ips.add("10.0.0.9")

inter=connected_ips.intersection(blacklisted_ips)
for ip in inter :
    print(f"ALERT: Blocked IP detected → {ip}")

print("Total Blacklisted IPs:", len(blacklisted_ips))

# Blacklisted & Connected: {'10.0.0.2', '10.0.0.8'}
# Safe IPs: {'10.0.0.9', '10.0.0.1', '10.0.0.5'}
# ALERT: Blocked IP detected → 10.0.0.9
# ALERT: Blocked IP detected → 10.0.0.2
# ALERT: Blocked IP detected → 10.0.0.8
# Total Blacklisted IPs: 4