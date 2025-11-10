#Task 2: Unique Customer Email Filter

campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

print("All Unique Emails:",campaign_A.union(campaign_B))
print("Common Customers:",campaign_A.intersection(campaign_B))
print("Only Campaign A:",campaign_A.difference(campaign_B))
print("Only One Campaign:",campaign_A.symmetric_difference(campaign_B))
print("Total Unique:",len(campaign_A.union(campaign_B)))

#Sample Execution
# All Unique Emails: {'amit@ust.com', 'priya@ust.com', 'rahul@ust.com', 'meena@ust.com', 'john@ust.com', 'neha@ust.com'}
# Common Customers: {'amit@ust.com', 'priya@ust.com'}
# Only Campaign A: {'john@ust.com', 'rahul@ust.com'}
# Only One Campaign: {'rahul@ust.com', 'meena@ust.com', 'john@ust.com', 'neha@ust.com'}
# Total Unique: 6