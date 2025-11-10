print("==========Ust IT Help Desk===========")
print("Raise Hardware Issues 1")
print("Raise Software Issues 2")
print("Raise Network Issues 3")
print("View Total TIckets Raised")
print("Exit")
print("Please choose between 1 to 5")

hardware_tickets = 0
software_tickets = 0
network_tickets=0
total_tickets =0
while True:
    n = int(input("Enter the number"))
    if n==1:
        hardware_tickets+=1
        total_tickets+=1
        print("Hardware issue recorded . IT team will respond soon")
    if n==2:
        software_tickets+=1
        total_tickets+=1
        print("software issue recorded . IT team will respond soon")
    if n==3:
        network_tickets+=1
        total_tickets+=1
        print("network issue recorded . IT team will respond soon")
    if n==4:
        print(f"Hardware tickets {hardware_tickets}")
        print(f"software tickets {software_tickets}")
        print(f"network tickets {network_tickets}")
        print(f"total tickets {total_tickets}")
    if n==5:
        break
    if n>5 or n<1:
         print("please choose between 1 to 5")    