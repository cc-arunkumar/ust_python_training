# Task 2: Unique Customer Email Filter
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