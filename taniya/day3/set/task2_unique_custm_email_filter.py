# Define two sets of email campaigns
campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

# Union → all unique emails from both campaigns
print(campaign_A.union(campaign_B))

# Intersection → common emails in both campaigns
print(campaign_A.intersection(campaign_B))

# Difference → emails in campaign_A but not in campaign_B
print(campaign_A.difference(campaign_B))

# Count of unique emails across both campaigns
unique_count = len(campaign_A.union(campaign_B))
print("Count of unique elements:", unique_count)

# -------------------------
# Expected Output:
# {'john@ust.com', 'rahul@ust.com', 'amit@ust.com', 'neha@ust.com', 'meena@ust.com', 'priya@ust.com'}
# {'amit@ust.com', 'priya@ust.com'}
# {'john@ust.com', 'rahul@ust.com'}
# Count of unique elements: 6