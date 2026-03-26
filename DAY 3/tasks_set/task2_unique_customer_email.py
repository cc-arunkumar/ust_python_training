"""
Task 2: Unique Customer Email Filter
Scenario:
Your marketing team collected email addresses from two different campaigns.
Some customers appear in both lists. You need to find unique and overlapping
customers.

"""

# Sets storing email addresses from two campaigns
campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

# All unique emails from both campaigns
unique_emails=campaign_A.union(campaign_B)
print(f"All Unique Emails: {unique_emails}")

# Emails present in both campaigns
both_campaign=campaign_A.intersection(campaign_B)
print(both_campaign)

# Emails only in Campaign A
only_campaignA=campaign_A.difference(campaign_B)
print(only_campaignA)


"""
SAMPLE OUTPUT

All Unique Emails: {'priya@ust.com', 'rahul@ust.com', 'amit@ust.com', 'neha@ust.com', 'john@ust.com', 'meena@ust.com'}
{'amit@ust.com', 'priya@ust.com'}
{'rahul@ust.com', 'john@ust.com'}

"""
