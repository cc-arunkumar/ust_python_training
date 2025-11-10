"""
Task 2: Unique Customer Email Filter
Scenario:
Your marketing team collected email addresses from two different campaigns.
Some customers appear in both lists. You need to find unique and overlapping
customers.

"""

campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

#unique email
unique_emails=campaign_A.union(campaign_B)
print(f"All Unique Emails: {unique_emails}")

both_campaign=campaign_A.intersection(campaign_B)
print(both_campaign)

#difference
only_campaignA=campaign_A.difference(campaign_B)
print(only_campaignA)


"""
SAMPLE OUTPUT

All Unique Emails: {'priya@ust.com', 'rahul@ust.com', 'amit@ust.com', 'neha@ust.com', 'john@ust.com', 'meena@ust.com'}
{'amit@ust.com', 'priya@ust.com'}
{'rahul@ust.com', 'john@ust.com'}

"""