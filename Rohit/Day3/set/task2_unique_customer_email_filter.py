# Task 2: Unique Customer Email Filter
# Scenario:
# Your marketing team collected email addresses from two different campaigns.
# Some customers appear in both lists. You need to find unique and overlapping


# Step 1: Initialize sets for two email campaigns
campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

# Step 2: Union of campaign_B with itself (no change, just returns the same set)
print("Union of campaign_B with itself")
print(campaign_B.union(campaign_B))  

# Step 3: Find common emails between both campaigns
print("Common emails")
print(campaign_A.intersection(campaign_B)) 

# Step 4: Emails in campaign_A but not in campaign_B
print("Emails in campaign_A but not in campaign_B")
print(campaign_A.difference(campaign_B)) 

# Step 5: Emails in either campaign but not both (symmetric difference)
print("Emails in either campaign but not both ")
print(campaign_B.symmetric_difference(campaign_A))  

# Step 6: Combine both sets using list conversion and set to remove duplicates
finalList = set(list(campaign_B) + list(campaign_A))
print("Combine both sets using list conversion and set to remove duplicates")
print(finalList)


# ===========sample output===============
# Union of campaign_B with itself
# {'priya@ust.com', 'amit@ust.com', 'meena@ust.com', 'neha@ust.com'}
# Common emails
# {'priya@ust.com', 'amit@ust.com'}
# Emails in campaign_A but not in campaign_B
# {'john@ust.com', 'rahul@ust.com'}
# Emails in either campaign but not both 
# {'meena@ust.com', 'rahul@ust.com', 'john@ust.com', 'neha@ust.com'}
# Combine both sets using list conversion and set to remove duplicates
# {'rahul@ust.com', 'john@ust.com', 'priya@ust.com', 'neha@ust.com', 'meena@ust.com', 'amit@ust.com'}


