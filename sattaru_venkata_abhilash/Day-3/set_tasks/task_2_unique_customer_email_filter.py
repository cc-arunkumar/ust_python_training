# Task 2: Unique Customer Email Filter
# Scenario:
# Your marketing team collected email addresses from two campaigns.
# Some customers appear in both lists — find unique and overlapping customers.

campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

# 1. All unique emails collected (no duplicates)
all_unique = campaign_A | campaign_B
print("All Unique Emails:", all_unique)

# 2. Customers who signed up for both campaigns
common_customers = campaign_A & campaign_B
print("Common Customers:", common_customers)

# 3. Customers who signed up only for Campaign A
only_A = campaign_A - campaign_B
print("Only Campaign A:", only_A)

# 4. Customers who signed up for exactly one campaign (not both)
only_one = campaign_A ^ campaign_B
print("Only One Campaign:", only_one)

# 5. Total number of unique customers
print("Total Unique:", len(all_unique))


# Sample Output:
# All Unique Emails: {'john@ust.com', 'rahul@ust.com', 'amit@ust.com', 'neha@ust.com', 'meena@ust.com', 'priya@ust.com'}
# Common Customers: {'amit@ust.com', 'priya@ust.com'}
# Only Campaign A: {'john@ust.com', 'rahul@ust.com'}
# Only One Campaign: {'john@ust.com', 'rahul@ust.com', 'neha@ust.com', 'meena@ust.com'}
# Total Unique: 6
