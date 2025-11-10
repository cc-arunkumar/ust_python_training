# Task 3: Security Team — IP Monitoring
# System
# Scenario:
# Your company’s security team monitors IP addresses connecting to the system.
# Some IPs are suspicious and listed in a blacklist.
# You must analyze connections using sets.
# Instructions:
# connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
# blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}
# Tasks:
# 1. Print all IPs that are blacklisted and currently connected.
# (Hint: intersection)
# 2. Print all safe IPs — connected but not blacklisted.
# (Hint: difference)
# 3. A new suspicious IP "10.0.0.9" is detected — add it to blacklisted_ips .
# 4. Print an alert message for each IP that’s currently connected and blacklisted:
# ALERT: Blocked IP detected - 10.0.0.2
# ALERT: Blocked IP detected - 10.0.0.8
# ...
# 5. Finally, display total unique blacklisted IPs in your system.

connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}
#  Print all IPs that are blacklisted and currently connected.

print("all ips:",connected_ips.intersection(blacklisted_ips))

#  Print all safe IPs — connected but not blacklisted.
print("connected but not blacklisted:",connected_ips.difference(blacklisted_ips))

#  new suspicious IP "10.0.0.9" is detected — add it to blacklisted_ips .
blacklisted_ips.add("10.0.0.9")
# Print an alert message for each IP that’s currently connected and blacklisted
list1=list(connected_ips.intersection(blacklisted_ips))
for alert in list1:
    print(f"ALERT: blocked IP detected-{alert}")

#  Finally, display total unique blacklisted IPs in your system.
length=blacklisted_ips.difference(connected_ips)
print(f"unique in blacklist:{len(length)}")

# output
# all ips: {'10.0.0.8', '10.0.0.2'}
# connected but not blacklisted: {'10.0.0.5', '10.0.0.9', '10.0.0.1'}
# ALERT: blocked IP detected-10.0.0.9
# ALERT: blocked IP detected-10.0.0.8
# ALERT: blocked IP detected-10.0.0.2
# unique in blacklist:1