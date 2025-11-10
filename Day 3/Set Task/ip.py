connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}

print(blacklisted_ips.intersection(connected_ips))
print(connected_ips.difference(blacklisted_ips))
blacklisted_ips.add("10.0.0.9")
print(blacklisted_ips)
print(len(connected_ips.union(blacklisted_ips)))

for ip in blacklisted_ips & connected_ips:
    print(f"ALERT: Blocked IP detected - {ip}")