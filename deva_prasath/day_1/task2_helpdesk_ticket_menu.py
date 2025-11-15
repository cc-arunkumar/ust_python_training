## Task 2: IT Helpdesk Ticket Menu
# Create a command-line helpdesk ticket system for employees to raise and track IT issues 
# such as hardware, software, or network problems.
# Initialize counters for different types of issues
soft_iss, hard_iss, net_iss = 0, 0, 0

# Start a continuous loop for the helpdesk menu system
while(True):
    print("\n===UAT IT Helpdesk===")
    print("1. Raise hardware issue")
    print("2. Raise software issue")
    print("3. Raise network issue")
    print("4. View total tickets raised")
    print("5. Exit")
    
    # Get user's choice
    chc = input("Enter your choice: ")
    
    # Handle hardware issue
    if chc == '1':
        hard_iss += 1  # Increment hardware issue counter
        print("Hardware issue recorded. IT team will respond soon")
        
    # Handle software issue
    elif chc == '2':
        soft_iss += 1  # Increment software issue counter
        print("Software issue recorded. IT team will respond soon")
        
    # Handle network issue
    elif chc == '3':
        net_iss += 1  # Increment network issue counter
        print("Network issue recorded. IT team will respond soon")
        
    # Display total issues raised
    elif chc == '4':
        print(f"Hardware tickets: {hard_iss}")
        print(f"Software tickets: {soft_iss}")
        print(f"Network tickets: {net_iss}")
        print(f"Total tickets raised: {hard_iss + soft_iss + net_iss}")
        
    # Exit the program
    elif chc == '5':
        print("Exiting Helpdesk. Thank You!")
        break
        
    # Invalid choice
    else:
        print("Invalid choice. Please enter a number between 1 and 5")


## Sample output

# ===UAT IT Helpdesk===
# 1.Raise hardware issue
# 2.Raise software issue
# 3.Raise network issue
# 4.View total tickets raised
# 5.Exit
# Enter your choice: 1
# Hardware issue recorded. IT team will repsond soon

# ===UAT IT Helpdesk===
# 1.Raise hardware issue
# 2.Raise software issue
# 3.Raise network issue
# 4.View total tickets raised
# 5.Exit
# Enter your choice: 2
# Software issue recorded. IT team will repsond soon

# ===UAT IT Helpdesk===
# 1.Raise hardware issue
# 2.Raise software issue
# 3.Raise network issue
# 4.View total tickets raised
# 5.Exit
# Enter your choice: 3
# Expense added successfully
# Network issue recorded. IT team will repsond soon

# ===UAT IT Helpdesk===
# 1.Raise hardware issue
# 2.Raise software issue
# 3.Raise network issue
# 4.View total tickets raised
# 5.Exit
# Enter your choice: 4
# Hardware tickets: 1
# Software tickets: 1
# Network tickets: 1
# Total tickets raised: 3

# ===UAT IT Helpdesk===
# 1.Raise hardware issue
# 2.Raise software issue
# 3.Raise network issue
# 4.View total tickets raised
# 5.Exit
# Enter your choice: 5
# Exiting Helpdesk.Thank You!