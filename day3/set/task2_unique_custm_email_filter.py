campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}
print(campaign_A.union(campaign_B))
print(campaign_A.intersection(campaign_B))
print(campaign_A.difference(campaign_B))

unique_count = len(campaign_A.union(campaign_B))
print("Count of unique elements:", unique_count)

