# Task 2: Unique Customer Email Filter


campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}


all_unique = campaign_A.union(campaign_B)
print("All Unique Emails:", all_unique)


common_customers = campaign_A.intersection(campaign_B)
print("Common Customers:", common_customers)


only_campaign_A = campaign_A.difference(campaign_B)
print("Only Campaign A:", only_campaign_A)


only_one_campaign = campaign_A.symmetric_difference(campaign_B)
print("Only One Campaign:", only_one_campaign)

print("Total Unique:", len(all_unique))

#sample output
# All Unique Emails: {'rahul@ust.com', 'meena@ust.com', 'neha@ust.com', 'john@ust.com', 'amit@ust.com', 'priya@ust.com'}
# Common Customers: {'amit@ust.com', 'priya@ust.com'}
# Only Campaign A: {'john@ust.com', 'rahul@ust.com'}
# Only One Campaign: {'rahul@ust.com', 'meena@ust.com', 'neha@ust.com', 'john@ust.com'}
# Total Unique: 6

