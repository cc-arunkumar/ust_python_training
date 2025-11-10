#IT Helpdesk Ticket Menu
#Create a command-line helpdesk ticket system for employees to raise and track IT issues such as hardware, software, or network problems.
hardware_tickets=0
software_tickets=0
network_tickets=0
while True:
    print("1.raise hardware issue")
    print("2.raise software issue")
    print("3.raise network issue")
    print("4.view total tickets raised")
    print("5.exit")
    choice=input("enter your choice:")
    if choice=='1':
        hardware_tickets+=1
        print("hardware issue recorded IT team will respond soon")
    elif choice=='2':
        software_tickets+=1
        print("software issue recorded IT team will respond soon")
    elif choice=='3':
        network_tickets+=1
        print("network issue recorded IT team will respond soon")
    elif choice=='4':
        total=hardware_tickets+software_tickets+network_tickets
        print("hardware tickets:",hardware_tickets)
        print("software tickets:",software_tickets)
        print("network tickets:",network_tickets)
        print("total tickets raised:",total)
    elif choice=='5':
        print("existing helpdesk.\nthank you")
        break
    else:
        print("invalid")
 
 #sample execution
# 1.raise hardware issue
# 2.raise software issue
# 3.raise network issue
# 4.view total tickets raised
# 5.exit
# enter your choice:1
# hardware issue recorded IT team will respond soon
# 1.raise hardware issue
# 2.raise software issue
# 3.raise network issue
# 4.view total tickets raised
# 5.exit
# enter your choice:2
# software issue recorded IT team will respond soon
# 1.raise hardware issue
# 2.raise software issue
# 3.raise network issue
# 4.view total tickets raised
# 5.exit
# enter your choice:3
# network issue recorded IT team will respond soon
# 1.raise hardware issue
# 2.raise software issue
# 3.raise network issue
# 4.view total tickets raised
# 5.exit
# enter your choice:4
# hardware tickets: 1
# software tickets: 1
# network tickets: 1
# total tickets raised: 3
# 1.raise hardware issue
# 2.raise software issue
# 3.raise n1etwork issue
# 4.view total tickets raised
# 5.exit
# enter your choice: