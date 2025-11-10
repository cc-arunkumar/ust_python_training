# Unique_Customer_Email_Filter

campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

print("All Unique Emails: ",campaign_A | campaign_B)
print("Common Customers: ",campaign_A & campaign_B)
print("Only Campaign A: ",campaign_A - campaign_B)
print("Only One Campaign: ",campaign_A ^ campaign_B)
print("Total Unique: ",len(campaign_A | campaign_B))

# output

# All Unique Emails:  {'neha@ust.com', 'rahul@ust.com', 'priya@ust.com', 'amit@ust.com', 'meena@ust.com', 'john@ust.com'}
# Common Customers:  {'amit@ust.com', 'priya@ust.com'}
# Only Campaign A:  {'rahul@ust.com', 'john@ust.com'}
# Only One Campaign:  {'neha@ust.com', 'rahul@ust.com', 'meena@ust.com', 'john@ust.com'}
# Total Unique:  6