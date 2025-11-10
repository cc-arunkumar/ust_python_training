# Unique Customer Email Filter
campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

Unique_mails = campaign_A.union(campaign_B)
print("All Unique emails : " , Unique_mails)

Both_sign = campaign_A.intersection(campaign_B)
print("Common Customer :" ,Both_sign)

Only_Campaign_A = campaign_A.difference(campaign_B)
print("Only Campaign A :" ,Only_Campaign_A)

Exactly_one = campaign_A.symmetric_difference(campaign_B)
print("Only one Campaign :", Exactly_one)

total_unique = len(Unique_mails)
print("Total Unique Customers:", total_unique)

# All Unique emails :  {'neha@ust.com', 'amit@ust.com', 'rahul@ust.com', 'meena@ust.com', 'priya@ust.com', 'john@ust.com'}
# Common Customer : {'amit@ust.com', 'priya@ust.com'}
# Only Campaign A : {'john@ust.com', 'rahul@ust.com'}
# Only one Campaign : {'neha@ust.com', 'rahul@ust.com', 'meena@ust.com', 'john@ust.com'}
# Total Unique Customers: 6


  
