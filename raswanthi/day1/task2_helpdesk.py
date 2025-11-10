#UST IT Helpdesk
print("UST IT Helpdesk\n")
print("\nOptions:")
print("1: Raise hardware issue")
print("2: Raise software issue")
print("3: Raise network issue")
print("4: View total tickets raised")
print("5: Exit")
hardware_ticket=0
software_ticket=0    
network_ticket=0
while True:

    choice = input("Enter your choice: ")
    match choice:
        case "1":
            print("Hardware issue recorded. IT team will respond soon.")
            hardware_ticket+=1
        case "2":
            print("Software issue recorded. IT team will respond soon.")
            software_ticket+=1
        case "3":
            print("Network issue recorded. IT team will respond soon.")
            network_ticket+=1

        case "4":
            print(f"Total number of hardware tickets raised : {hardware_ticket}")
            print(f"Total number of software tickets raised : {software_ticket}")
            print(f"Total number of network tickets raised : {network_ticket}")
            total_tickets=hardware_ticket + software_ticket + network_ticket
            print(f"Total tickets issued are : {total_tickets}")
        
        case "5":
            print("Exciting Helpdesk. Thankyou!!!")
            break


'''output:
UST IT Helpdesk

Options:
1: Raise hardware issue
2: Raise software issue
3: Raise network issue
4: View total tickets raised
5: Exit
Enter your choice: 1
Hardware issue recorded. IT team will respond soon.
Enter your choice: 1
Hardware issue recorded. IT team will respond soon.
Enter your choice: 2
Software issue recorded. IT team will respond soon.
Enter your choice: 2
Software issue recorded. IT team will respond soon.
Enter your choice: 2
Software issue recorded. IT team will respond soon.
Enter your choice: 3
Network issue recorded. IT team will respond soon.
Enter your choice: 4
Total number of hardware tickets raised : 2
Total number of software tickets raised : 3
Total number of network tickets raised : 1
Total tickets issued are : 6
Enter your choice: 5
Exciting Helpdesk. Thankyou!!!
'''