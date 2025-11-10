connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}


print("Blacklisted & Connected: ",connected_ips & blacklisted_ips)
print("Safe IPs:",connected_ips-blacklisted_ips)
blacklisted_ips.add("10.0.0.9")
list1=list(connected_ips & blacklisted_ips)
for address in list1:
    print(f"connected_ips & blacklisted_ips-{address}")
mylist=connected_ips | blacklisted_ips
print("Total Blacklisted IPs: ",len(mylist))


# ============Sample Execution=============
# Blacklisted & Connected:  {'10.0.0.8', '10.0.0.2'}
# Safe IPs: {'10.0.0.9', '10.0.0.5', '10.0.0.1'}
# connected_ips & blacklisted_ips-10.0.0.9
# connected_ips & blacklisted_ips-10.0.0.8
# connected_ips & blacklisted_ips-10.0.0.2
# Total Blacklisted IPs:  6