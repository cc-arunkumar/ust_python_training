# Unique Customer Email Filter

# Your marketing team collected email addresses from two different campaigns.
# Some customers appear in both lists. You need to find unique and overlapping
# customers

# Sets representing email addresses of customers in two campaigns
campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

# Print all unique emails from both campaigns (union)
print("All unique Emails: ", campaign_A | campaign_B)

# Print the common customers between both campaigns (intersection)
print("Common Customers: ", campaign_A & campaign_B)

# Print customers who are only in campaign A (difference)
print("Only Campaign A: ", campaign_A - campaign_B)

# Print customers who are in either campaign A or B, but not both (symmetric difference)
print("Only One Campaign: ", campaign_A ^ campaign_B)

# Print the total number of unique emails across both campaigns
print("Total Unique: ", len(campaign_A | campaign_B))


# All unique Emails:  {'priya@ust.com', 'rahul@ust.com', 'neha@ust.com', 'meena@ust.com', 'amit@ust.com', 'john@ust.com'}
# Common Customers:  {'priya@ust.com', 'amit@ust.com'}
# Only Campaign A:  {'rahul@ust.com', 'john@ust.com'}
# Only One Campaign : {'rahul@ust.com', 'neha@ust.com', 'meena@ust.com', 'john@ust.com'}
# Total Unique:  6
