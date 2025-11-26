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
# 2. Find all customers who signed up for both campaigns.
# 3. Find all customers who signed up only for Campaign A.
# 4. Find all customers who signed up for exactly one campaign (not both).
# 5. Display how many total unique customers you have

campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}
print(campaign_A.union(campaign_B))

print(campaign_A.intersection(campaign_B))

print(campaign_A-campaign_B)

print(campaign_A^campaign_B)
unique_campaign =campaign_A.union(campaign_B)
print(len(unique_campaign))

# EXPECTED OUTPUT:
# {'amit@ust.com', 'rahul@ust.com', 'neha@ust.com', 'priya@ust.com', 'john@ust.com', 'meena@ust.com'}
# {'amit@ust.com', 'priya@ust.com'}
# {'rahul@ust.com', 'john@ust.com'}
# {'rahul@ust.com', 'neha@ust.com', 'john@ust.com', 'meena@ust.com'}
# 6
