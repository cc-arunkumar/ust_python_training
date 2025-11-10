#Task 2: Unique Customer Email Filter
campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}
uniq_emails = campaign_A.union(campaign_B)
print("All Unique Emails:",uniq_emails)
print("Common Customers:",campaign_A.intersection(campaign_B))
print("Only Campaign A",campaign_A.difference(campaign_B))
print("Only One Campaign",campaign_A.symmetric_difference(campaign_B))
print("Total Unique:",len(uniq_emails))

#Sample Output
# All Unique Emails: {'john@ust.com', 'neha@ust.com', 'priya@ust.com', 'amit@ust.com', 'meena@ust.com', 'rahul@ust.com'}
# Common Customers: {'amit@ust.com', 'priya@ust.com'}
# Only Campaign A {'john@ust.com', 'rahul@ust.com'}
# Only One Campaign {'john@ust.com', 'neha@ust.com', 'meena@ust.com', 'rahul@ust.com'}
# Total Unique: 6
