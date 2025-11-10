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
campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

#  Print all unique emails collected (no duplicates).
unique="unique emails:",campaign_A.union(campaign_B)
print(unique)
# . Find all customers who signed up for both campaigns
print("common customers:",campaign_A.intersection(campaign_B))
# . Find all customers who signed up only for Campaign A
print("only campaign_A:",campaign_A.difference(campaign_B))
# . Find all customers who signed up for exactly one campaign (not both).
print("only in one campaign:",campaign_A.symmetric_difference(campaign_B))


# . Display how many total unique customers you have.
count=campaign_A.union(campaign_B)
print("count of unique  customers :",len(count))



#sample output
# ('unique emails:', {'priya@ust.com', 'amit@ust.com', 'rahul@ust.com', 'neha@ust.com', 'john@ust.com', 'meena@ust.com'})
# common customers: {'priya@ust.com', 'amit@ust.com'}
# only campaign_A: {'john@ust.com', 'rahul@ust.com'}
# only in one campaign: {'rahul@ust.com', 'neha@ust.com', 'john@ust.com', 'meena@ust.com'}
# count of unique  customers : 6