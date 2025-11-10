#Task 2 : Unique Customer Email Filter

#Code 
campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

union_set= campaign_A | campaign_B
iteration_set= campaign_A & campaign_B
diff_set= campaign_A-campaign_B
only_one_campaign = (campaign_A ^ campaign_B)
print("All Unique Emails : ",union_set)
print("Common Customers : ",iteration_set)
print("Only Compaign A : ",diff_set)
print("Only One Compaign : ",only_one_campaign)
print("Total Unique : ",len(union_set))

#Output
# All Unique Emails :  {'amit@ust.com', 'neha@ust.com', 'priya@ust.com', 'meena@ust.com', 'rahul@ust.com', 'john@ust.com'}
# Common Customers :  {'priya@ust.com', 'amit@ust.com'}
# Only Compaign A :  {'rahul@ust.com', 'john@ust.com'}
# Only One Compaign :  {'neha@ust.com', 'meena@ust.com', 'rahul@ust.com', 'john@ust.com'}
# Total Unique :  6
