# Task 2: Unique Customer Email Filter
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

campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

# Print all unique emails collected
all_unique = campaign_A.union(campaign_B)
print("All Unique Emails:", all_unique)

# Find customers who signed up for both campaigns
common_customers = campaign_A.intersection(campaign_B)
print("Common Customers:", common_customers)

# Find customers who signed up only for Campaign A
only_A = campaign_A.difference(campaign_B)
print("Only Campaign A:", only_A)

# Find customers who signed up for exactly one campaign
only_one_campaign = campaign_A.symmetric_difference(campaign_B)
print("Only One Campaign:", only_one_campaign)

print("Total Unique:", len(all_unique))

# All Unique Emails: {'amit@ust.com', 'meena@ust.com', 'priya@ust.com', 'john@ust.com', 'neha@ust.com', 'rahul@ust.com'}
# Common Customers: {'amit@ust.com', 'priya@ust.com'}
# Only Campaign A: {'rahul@ust.com', 'john@ust.com'}
# Only One Campaign: {'meena@ust.com', 'john@ust.com', 'neha@ust.com', 'rahul@ust.com'}
# Total Unique: 6