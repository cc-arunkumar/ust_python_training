campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}
print("All Unique Emails:",campaign_A | campaign_B)
print("Common Customers:",campaign_A & campaign_B)
print("Only Campaign A:",campaign_A-campaign_B)
print("Only One Campaign:",campaign_A^campaign_B)
unique_set=campaign_A | campaign_B
print("Total Unique:", len(unique_set))
