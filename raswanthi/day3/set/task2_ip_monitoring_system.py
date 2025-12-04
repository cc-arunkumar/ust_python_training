#task 3: IP Monitoring system
connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}

blacklisted_connected = connected_ips.intersection(blacklisted_ips)
print(f"Blacklisted & Connected: {blacklisted_connected}")

safe_ips = connected_ips.difference(blacklisted_ips)
print(f"Safe IPs: {safe_ips}")

blacklisted_ips.add("10.0.0.9")

for ip in connected_ips.intersection(blacklisted_ips):
    print(f"ALERT: Blocked IP detected - {ip}")

print(f"Total Blacklisted IPs: {len(blacklisted_ips)}")

'''output:
Blacklisted & Connected: {'10.0.0.2', '10.0.0.8'}
Safe IPs: {'10.0.0.1', '10.0.0.5', '10.0.0.9'}
ALERT: Blocked IP detected - 10.0.0.2
ALERT: Blocked IP detected - 10.0.0.8
ALERT: Blocked IP detected - 10.0.0.9
Total Blacklisted IPs: 4
'''