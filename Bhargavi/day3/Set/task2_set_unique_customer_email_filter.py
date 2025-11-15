# Unique Customer Email Filter

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
# 5. Display how many total unique customers you have

# Define sets of customers in Campaign A and Campaign B
campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

# Find all unique emails across both campaigns (union of sets)
Unique_mails = campaign_A.union(campaign_B)
print("All Unique emails :", Unique_mails)

# Find customers common to both campaigns (intersection of sets)
Both_sign = campaign_A.intersection(campaign_B)
print("Common Customer :", Both_sign)

# Find customers only in Campaign A (difference of sets)
Only_Campaign_A = campaign_A.difference(campaign_B)
print("Only Campaign A :", Only_Campaign_A)

# Find customers in exactly one campaign (symmetric difference of sets)
Exactly_one = campaign_A.symmetric_difference(campaign_B)
print("Only one Campaign :", Exactly_one)

# Count total unique customers across both campaigns
total_unique = len(Unique_mails)
print("Total Unique Customers:", total_unique)

# Output:
# All Unique emails :  {'neha@ust.com', 'amit@ust.com', 'rahul@ust.com', 'meena@ust.com', 'priya@ust.com', 'john@ust.com'}
# Common Customer : {'amit@ust.com', 'priya@ust.com'}
# Only Campaign A : {'john@ust.com', 'rahul@ust.com'}
# Only one Campaign : {'neha@ust.com', 'rahul@ust.com', 'meena@ust.com', 'john@ust.com'}
# Total Unique Customers: 6
