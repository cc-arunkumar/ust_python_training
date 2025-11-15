#Task 2: Unique Customer Email Filter

# Sets representing emails of customers in two different marketing campaigns
campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

# Printing all unique emails (union of both sets)
print("All Unique Emails:", campaign_A.union(campaign_B))

# Printing common customers (intersection of both sets)
print("Common Customers:", campaign_A.intersection(campaign_B))

# Printing customers who are only in Campaign A (difference between A and B)
print("Only Campaign A:", campaign_A.difference(campaign_B))

# Printing customers who are in either campaign but not both (symmetric difference)
print("Only One Campaign:", campaign_A.symmetric_difference(campaign_B))

# Printing the total number of unique emails (size of the union of both sets)
print("Total Unique:", len(campaign_A.union(campaign_B)))


#Sample Execution
# All Unique Emails: {'amit@ust.com', 'priya@ust.com', 'rahul@ust.com', 'meena@ust.com', 'john@ust.com', 'neha@ust.com'}
# Common Customers: {'amit@ust.com', 'priya@ust.com'}
# Only Campaign A: {'john@ust.com', 'rahul@ust.com'}
# Only One Campaign: {'rahul@ust.com', 'meena@ust.com', 'john@ust.com', 'neha@ust.com'}
# Total Unique: 6