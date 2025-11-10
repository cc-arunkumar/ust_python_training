hardwaret=0
softwaret=0
networkt=0
total=0
print("====== UST IT Helpdesk ======")
print("1. Raie Hardware Issue")
print("2. Raie Software Issue")
print("3. Raie Network Issue")
print("4. View Total Tickets Raised")
print("5. Exit")
while(True):
    
    n=int(input("Enter your choice: "))
    
    if(n==1):
        hardwaret=hardwaret+1
        total=total+1
        print("Hardware issue recorded. IT team will respond soon.")
    elif(n==2):
        softwaret=softwaret+1
        total=total+1
        print("Software issue recorded. IT team will respond soon.")
    elif(n==3):
        networkt=networkt+1
        total=total+1
        print("Network issue recorded. IT team will respond soon.")
    elif(n==4):
        print(f"HardwarecTickets: {hardwaret}")
        print(f"Software Tickets: {softwaret}")
        print(f"Network Ticket: {networkt}")
        print(f"Total Tickets Raised: {total}")
    elif(n==5):
        print("Exiting Helpdesk.Thank you!")
        break
    else:
        print("Enter proper choice")