#Task 3: Security Team — IP Monitoring System
connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}
print(f"Currenty connected : {connected_ips & blacklisted_ips}")
print(f"Safe IPs : { connected_ips - blacklisted_ips}")
blacklisted_ips.add("10.0.0.9")
for i in connected_ips & blacklisted_ips :
    print(f"ALERT: Blocked IP detected : {i}")
print(f"Unique blacklisted ips : {len(blacklisted_ips)}")
#Output
# Currenty connected : {'10.0.0.2', '10.0.0.8'}
# Safe IPs : {'10.0.0.1', '10.0.0.5', '10.0.0.9'}
# ALERT: Blocked IP detected : 10.0.0.2
# ALERT: Blocked IP detected : 10.0.0.9
# ALERT: Blocked IP detected : 10.0.0.8
# Unique blacklisted ips : 4