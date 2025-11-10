# TASK 2 - Unique Customer Email Filter

campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

print("All Unique Emails:",campaign_A | campaign_B)

print("Common Customers:",campaign_A & campaign_B)

print("Only Campaign A:",campaign_A - campaign_B)

print("Only One Campaign:",campaign_A ^ campaign_B )

total_unique = len(campaign_A | campaign_B)
print("Total Unique Emails:", total_unique)


# --------------------------------------------------------------------------

# Sample Output
# All Unique Emails: {'amit@ust.com', 'neha@ust.com', 'priya@ust.com', 'meena@ust.com', 'john@ust.com', 'rahul@ust.com'}
# Common Customers: {'priya@ust.com', 'amit@ust.com'}
# Only Campaign A: {'rahul@ust.com', 'john@ust.com'}
# Only One Campaign: {'neha@ust.com', 'meena@ust.com', 'john@ust.com', 'rahul@ust.com'}
# Total Unique Emails: 6
