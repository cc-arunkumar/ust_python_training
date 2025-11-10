# Unique Customer Email Filter


# Scenario:
# Your marketing team collected email addresses from two different campaigns.
# Some customers appear in both lists. You need to find unique and overlapping
# customers.
# Instructions:
# campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@u
# st.com"}
# campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena
# @ust.com"}
# Tasks:
# 1. Print all unique emails collected (no duplicates).
# (Hint: union)
# 2. Find all customers who signed up for both campaigns.
# (Hint: intersection)
# 3. Find all customers who signed up only for Campaign A.
# (Hint: difference)
# 4. Find all customers who signed up for exactly one campaign (not both).
# (Hint: symmetric difference)
# 5. Display how many total unique customers you have.


campaign_a = {'john@ust.com', 'priya@ust.com', 'amit@ust.com', 'rahul@ust.com'}
campaign_b = {'amit@ust.com', 'priya@ust.com', 'neha@ust.com', 'meena@ust.com'}
all_unique_emails = campaign_a.union(campaign_b)
print("All Unique Emails:", all_unique_emails)
common_customers = campaign_a.intersection(campaign_b)
print("Common Customers:", common_customers)
only_campaign_a = campaign_a.difference(campaign_b)
print("Only Campaign A:", only_campaign_a)
only_one_campaign = campaign_a.symmetric_difference(campaign_b)
print("Only One Campaign:", only_one_campaign)
total_unique_customers = len(all_unique_emails)
print("Total Unique:", total_unique_customers)

#o/p:
# All Unique Emails: {'john@ust.com', 'priya@ust.com', 'amit@ust.com', 'meena@ust.com', 'neha@ust.com', 'rahul@ust.com'}
# Common Customers: {'priya@ust.com', 'amit@ust.com'}
# Only Campaign A: {'john@ust.com', 'rahul@ust.com'}
# Only One Campaign: {'john@ust.com', 'meena@ust.com', 'neha@ust.com', 'rahul@ust.com'}
# Total Unique: 6