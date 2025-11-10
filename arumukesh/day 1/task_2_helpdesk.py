
def helpdesk():
    print('''IT HelpDesk Menu
          1.Raise hardware issue
          2.Raise software issue
          3.RAise network issue
          4.View report
          5.Exit''')
    choice = int(input("Enter your choice: "))
    total_issues,hardware,software,network=0,0,0,0
    if (choice <0 and choice >5):
        print("Invalid Choice")
    while(True):
        if choice == 1:
            hardware+=1
            total_issues+=1
        if choice == 2:
            total_issues+=1
            software+=1
        if choice == 3:
            total_issues+=1
            network+=1
        if choice == 4:
         print(f'''Total issues raised: {total_issues}
        Hardware issues: {hardware}
        Software issues: {software}
        Network issues: {network}''')
        if choice == 5:
            print("Exiting the HelpDesk.Thank you!")
            break
        choice = int(input("Enter your choice: "))
    return
helpdesk()

# IT HelpDesk Menu
#           1.Raise hardware issue
#           2.Raise software issue
#           3.RAise network issue
#           4.View report
#           5.Exit
# Enter your choice: 1
# Enter your choice: 2
# Enter your choice: 3
# Enter your choice: 2
# Enter your choice: 4
# Total issues raised: 4
#         Hardware issues: 1
#         Software issues: 2
#         Network issues: 1
# Enter your choice: 5
# Exiting the HelpDesk.Thank you!