#Task2: UST IT Helpdesk

# Display the UST IT Helpdesk menu
print("====== UST IT Helpdesk ======")
print("1. Raise Hardware Issue")
print("2. Raise Software Issue")
print("3. Raise Network Issue")
print("4. View Total Tickets Raised")
print("5. Exit")

# Initialize counters for each type of issue
total_tickets_raised = 0
hardware_issue_count = 0
software_issue_count = 0
network_issue_count = 0

# Start an infinite loop to accept user input until exit option is chosen
while True:
    # Prompt the user to enter a choice
    choice = int(input("Enter your choice: "))

    # Match the user's choice to corresponding action
    match choice:
        case 1:
            # Increment hardware issue count and notify user
            hardware_issue_count += 1
            print("Hardware issue recorded. IT team will respond soon")
        case 2:
            # Increment software issue count and notify user
            software_issue_count += 1
            print("Software issue recorded. IT team will respond soon")
        case 3:
            # Increment network issue count and notify user
            network_issue_count += 1
            print("Network issue recorded. IT team will respond soon")
        case 4:
            # Display the count of each type of issue and the total tickets raised
            print("Hardware Tickets: ", hardware_issue_count)
            print("Software Tickets: ", software_issue_count)
            print("Network Tickets: ", network_issue_count)
            total_tickets_raised = hardware_issue_count + software_issue_count + network_issue_count
            print("Total tickets Raised: ", total_tickets_raised)
        case 5:
            # Exit the loop and terminate the program
            print("Exiting helpdesk. Have a great day!")
            break
        case _:
            # Handle invalid choices
            print("Wrong Choice")




#Sample Execution
# ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 1
# Hardware issue recorded. IT team will respond soon
# Enter your choice: 2
# Software issue recorded. IT team will respond soon
# Enter your choice: 3
# Network issue recorded. IT team will respond soon
# Enter your choice: 4
# Hardware Tickets:  1
# Software Tickets:  1
# Network Tickets:  1
# Total tickets Raised:  3
# Enter your choice: 5
# Exiting helpdesk. Have a great day!