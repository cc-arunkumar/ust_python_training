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
# 5. Display how many total unique customers you hav

campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

print("All Unique Emails:",campaign_A | campaign_B)

print("Common Customers:",campaign_A & campaign_B)

print("Only Campaign A:",campaign_A-campaign_B)

print("Only One Campaign:",campaign_A^campaign_B)

unique_set=campaign_A | campaign_B

print("Total Unique:", len(unique_set))


# Sample Output

# All Unique Emails: {'neha@ust.com', 'meena@ust.com', 'john@ust.com', 'priya@ust.com', 'amit@ust.com', 'rahul@ust.com'}

# Common Customers: {'amit@ust.com', 'priya@ust.com'}

# Only Campaign A: {'john@ust.com', 'rahul@ust.com'}

# Only One Campaign: {'neha@ust.com', 'meena@ust.com', 'john@ust.com', 'rahul@ust.com'}

# Total Unique: 6