# Unique_Customer_Email_Filter

campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}
print("unique emails collected: ",campaign_A.union(campaign_B))
print("customers who signed up for both campaigns: ",campaign_A.intersection(campaign_B))
print("customers who signed up only for Campaign A: ",campaign_A.difference(campaign_B))
print("customers who signed up for exactly one campaign: ",campaign_A.symmetric_difference(campaign_B))
print("total unique customers: ",len(campaign_B.union(campaign_A)))

# unique emails collected:  {'neha@ust.com', 'amit@ust.com', 'rahul@ust.com', 'john@ust.com', 'meena@ust.com', 'priya@ust.com'}
# customers who signed up for both campaigns:  {'amit@ust.com', 'priya@ust.com'}
# customers who signed up only for Campaign A:  {'rahul@ust.com', 'john@ust.com'}
# customers who signed up for exactly one campaign:  {'rahul@ust.com', 'meena@ust.com', 'john@ust.com', 'neha@ust.com'}
# total unique customers:  6