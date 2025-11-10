
campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

all_unique = campaign_A.union(campaign_B)
print("All Unique Emails:", all_unique)

common_customers = campaign_A.intersection(campaign_B)
print("Common Customers:", common_customers)

only_A = campaign_A.difference(campaign_B)
print("Only Campaign A:", only_A)

only_one_campaign = campaign_A.symmetric_difference(campaign_B)
print("Only One Campaign:", only_one_campaign)

print("Total Unique:", len(all_unique))

# All Unique Emails: {'amit@ust.com', 'meena@ust.com', 'priya@ust.com', 'john@ust.com', 'neha@ust.com', 'rahul@ust.com'}
# Common Customers: {'amit@ust.com', 'priya@ust.com'}
# Only Campaign A: {'rahul@ust.com', 'john@ust.com'}
# Only One Campaign: {'meena@ust.com', 'john@ust.com', 'neha@ust.com', 'rahul@ust.com'}
# Total Unique: 6