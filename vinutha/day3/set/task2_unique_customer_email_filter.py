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

#Code

campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}
print("All Unique Emails:",campaign_A.union(campaign_B))
print("Common Customers:",campaign_A.intersection(campaign_B))
print("Only Campaign A:",campaign_A-campaign_B)
print("Only One Campaign:",campaign_A^campaign_B)
print("Total Unique",len(campaign_A.union(campaign_B)))

#output
# PS C:\Users\303379\day3_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day3_training/task2_Unique_Customer_Email_Filter.py
# All Unique Emails: {'rahul@ust.com', 'amit@ust.com', 'john@ust.com', 'meena@ust.com', 'priya@ust.com', 'neha@ust.com'}
# Common Customers: {'priya@ust.com', 'amit@ust.com'}
# Only Campaign A: {'john@ust.com', 'rahul@ust.com'}
# Only One Campaign: {'rahul@ust.com', 'john@ust.com', 'meena@ust.com', 'neha@ust.com'}
# Total Unique 6
# PS C:\Users\303379\day3_training> 
