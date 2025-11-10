#Task 2: Unique Customer 
campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

unique_emails = campaign_A.union(campaign_B)
print(f"All Unique Emails: {unique_emails}")

both_campaigns = campaign_A.intersection(campaign_B)
print(f"Common Customers: {both_campaigns}")

only_campaign_A = campaign_A.difference(campaign_B)
print(f"Only Campaign A: {only_campaign_A}")

only_one_campaign = campaign_A.symmetric_difference(campaign_B)
print(f"Only One Campaign: {only_one_campaign}")

print(f"Total Unique: {len(unique_emails)}")

'''output:
Only Campaign A: {'john@ust.com', 'rahul@ust.com'}
Only One Campaign: {'neha@ust.com', 'john@ust.com', 'meena@ust.com', 'rahul@ust.com'}
Total Unique: 6
'''