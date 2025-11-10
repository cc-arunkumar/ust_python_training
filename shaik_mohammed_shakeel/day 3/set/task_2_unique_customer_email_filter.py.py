# Task 2 - Unique Customer Email Filter

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
print("Unique Emails:", campaign_A | campaign_B)
print("customers who signed up for both campaigns:",campaign_A & campaign_B)
print("customers who signed up only for Campaign A: ", campaign_A - campaign_B)
print("customers who signed up for exactly one campaign: ", campaign_A.symmetric_difference(campaign_B))
total_unique = len(campaign_A | campaign_B)
print("Total unique customers:", total_unique)

#Sample output
# Unique Emails: {'rahul@ust.com', 'meena@ust.com', 'neha@ust.com', 'amit@ust.com', 'priya@ust.com', 'john@ust.com'}
# customers who signed up for both campaigns: {'priya@ust.com', 'amit@ust.com'}
# customers who signed up only for Campaign A:  {'rahul@ust.com', 'john@ust.com'}
# customers who signed up for exactly one campaign:  {'rahul@ust.com', 'meena@ust.com', 'neha@ust.com', 'john@ust.com'}
# Total unique customers: 6