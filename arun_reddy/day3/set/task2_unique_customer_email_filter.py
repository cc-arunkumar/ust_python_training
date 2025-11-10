campaign_A = {"john@ust.com", "priya@ust.com", "amit@ust.com", "rahul@ust.com"}
campaign_B = {"neha@ust.com", "amit@ust.com", "priya@ust.com", "meena@ust.com"}

print("All Unique Emails:",campaign_A | campaign_B)
print("All Unique Emails:",campaign_A & campaign_B)
print("Only Campaign A:",campaign_A-campaign_B)
print("Only One Campaign:",campaign_A^campaign_B)
my_set=campaign_A | campaign_B
print(len(my_set))

# =======sample Execution==========
# All Unique Emails: {'rahul@ust.com', 'meena@ust.com', 'john@ust.com', 'amit@ust.com', 'priya@ust.com', 'neha@ust.com'}
# All Unique Emails: {'priya@ust.com', 'amit@ust.com'}
# Only Campaign A: {'rahul@ust.com', 'john@ust.com'}
# Only One Campaign: {'rahul@ust.com', 'meena@ust.com', 'john@ust.com', 'neha@ust.com'}
# 6
