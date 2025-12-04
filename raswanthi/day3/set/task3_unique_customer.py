#Task 2: Unique Customer 
campaign_A = {"john@example.com", "priya@example.com", "amit@example.com", "rahul@example.com"}
campaign_B = {"neha@example.com", "amit@example.com", "priya@example.com", "meena@example.com"}

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
Only Campaign A: {'john@example.com', 'rahul@example.com'}
Only One Campaign: {'neha@example.com', 'john@example.com', 'meena@example.com', 'rahul@example.com'}
Total Unique: 6
'''