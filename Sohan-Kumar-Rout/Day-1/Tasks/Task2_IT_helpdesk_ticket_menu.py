#Task 2 : IT Helpdesk Ticket Menu

#Code.
print("=====UST IT HelpDesk======")
print("1. Raise Hardware Issue : ")
print("2. Raise Software Issue : ")
print("3. Raise Netword Issue : ")
print("4. View Total Tickets Raised : ")
print("5. Exit")

choice = int(input("Raise Issue : "))
total_tkt_raised=0
hardware=0
software=0
network=0

while(True):
    if(choice==1):
        hardware+=1
        print("Hardware issue recorded.IT team will respond")
    elif(choice==2):
        software+=1
        print("Software issue recorded.IT team will respond")
    elif(choice==3):
        network+=1
        print("Network issue recorded.It team will respond")
    elif(choice==4):
        print("Hardware Tickets : ",hardware)
        print("Software Tickets : ",software)
        print("Network Ticket : ",network)
        total_tkt_raised=hardware+software+network
        print("Total Ticket Raised : ",total_tkt_raised)
    else:
        break
    choice=int(input("Raise issue : "))
print("Stop the program")

#Sample Output
# =====UST IT HelpDesk======
# 1. Raise Hardware Issue :
# 2. Raise Software Issue :
# 3. Raise Netword Issue :
# 4. View Total Tickets Raised :
# 5. Exit
# Raise Issue : 1
# Hardware issue recorded.IT team will respond
# Raise issue : 2
# Software issue recorded.IT team will respond
# Raise issue : 3
# Network issue recorded.It team will respond
# Raise issue : 1
# Hardware issue recorded.IT team will respond
# Raise issue : 4
# Hardware Tickets :  2
# Software Tickets :  1
# Network Ticket :  1
# Total Ticket Raised :  4
# Raise issue : 5
# Stop the program




        

