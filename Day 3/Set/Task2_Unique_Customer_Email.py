#Task 2: Unique Customer Email Filter
campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}
print(f"Unique email : {campaign_A | campaign_B}")
print(f"Both campaign : { campaign_A & campaign_B}")
print(f"Only A : { campaign_A - campaign_B}")
print(f"Only one : {campaign_B.symmetric_difference(campaign_A)}")
print(f"Total unique : { len(list(campaign_A | campaign_B))}")
#Output
# Unique email : {'priya@ust.com', 'rahul@ust.com', 'john@ust.com', 'neha@ust.com', 'amit@ust.com', 'meena@ust.com'}
# Both campaign : {'priya@ust.com', 'amit@ust.com'}
# Only A : {'john@ust.com', 'rahul@ust.com'}
# Only one : {'rahul@ust.com', 'neha@ust.com', 'john@ust.com', 'meena@ust.com'}
# Total unique : 6