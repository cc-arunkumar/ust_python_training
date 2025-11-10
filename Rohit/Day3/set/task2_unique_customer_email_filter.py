campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}
print(campaign_B.union(campaign_B))
print(campaign_A.intersection(campaign_B))
print(campaign_A.difference(campaign_B))
print(campaign_B.symmetric_difference(campaign_A))
finalList = set(list(campaign_B)+list(campaign_A))
print(finalList)


# ===========sample output===============
# {'neha@ust.com', 'meena@ust.com', 'priya@ust.com', 'amit@ust.com'}
# {'priya@ust.com', 'amit@ust.com'}
# {'rahul@ust.com', 'john@ust.com'}
# {'meena@ust.com', 'rahul@ust.com', 'john@ust.com', 'neha@ust.com'}
# {'priya@ust.com', 'amit@ust.com', 'meena@ust.com', 'rahul@ust.com', 'john@ust.com', 'neha@ust.com'}



