connected_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.8", "10.0.0.9"}
blacklisted_ips = {"10.0.0.2", "10.0.0.8", "10.0.0.10"}

print(connected_ips.intersection(blacklisted_ips))
print(connected_ips.difference(blacklisted_ips))
blacklisted_ips.add("10.0.0.9")
for i in connected_ips.union(blacklisted_ips):
    print(i)

print(len(connected_ips.union(blacklisted_ips)))


# ========sample output =====================
# {'10.0.0.8', '10.0.0.2'}
# {'10.0.0.5', '10.0.0.9', '10.0.0.1'}
# 10.0.0.9
# 10.0.0.1
# 10.0.0.10
# 10.0.0.8
# 10.0.0.5
# 10.0.0.2
# 6
