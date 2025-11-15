# task3:Security Team — IP Monitoring System\
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
# Set Tasks 3
# 4. Print an alert message for each IP that’s currently connected and blacklisted:
# ALERT: Blocked IP detected - 10.0.0.2
# ALERT: Blocked IP detected - 10.0.0.8
# ...
# 5. Finally, display total unique blacklisted IPs in your system.

#Code

# Set of currently connected IP addresses
connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}

# Set of blacklisted IP addresses
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}

# Find IPs that are both connected and blacklisted (intersection of sets)
print("Blacklisted & Connected:", connected_ips.intersection(blacklisted_ips))

# Find safe IPs (connected but not blacklisted → difference of sets)
print("Safe IPs:", connected_ips - blacklisted_ips)

# Add a new IP ("10.0.0.9") to the blacklist
blacklisted_ips.add("10.0.0.9")

# Check again for any connected IPs that are now blacklisted
for ip in connected_ips.intersection(blacklisted_ips):
    print(f"ALERT: Blocked IP detected - {ip}")

# Print the total number of blacklisted IPs
print("Total Blacklisted IPs:", len(blacklisted_ips))


#output
# PS C:\Users\303379\day3_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe "c:/Users/303379/day3_training/task3_Security Team_IP Monitoring System.py"
# Blacklisted & Connected: {'10.0.0.2', '10.0.0.8'}
# Safe IPs: {'10.0.0.5', '10.0.0.9', '10.0.0.1'}
# ALERT: Blocked IP detected - 10.0.0.2
# ALERT: Blocked IP detected - 10.0.0.8
# ALERT: Blocked IP detected - 10.0.0.9
# Total Blacklisted IPs: 4
# PS C:\Users\303379\day3_training> 
