import sys

def menu():
    
    menu = 0
    
    print ("#############################################################################")
    print ("########                                                             ########")
    print ("########               My Company Super Client Number 1'             ########")
    print ("######## ----------------------------------------------------------- ########")
    print ("######## Customer relationship management for Super Client Number 1  ########")
    print ("######## ----------------------------------------------------------- ########")
    print ("########                                                             ########")
    print ("########                    Choose a option:                         ########")
    print ("########                                                             ########")
    print ("########        1) Volume Balok    |  2) Volume Kubus                ########")
    print ("########        3) Luas Balok      |  4) Volume Kubus                ########")
    print ("########        5) Exit                                              ########")
    print ("########                                                             ########")
    print ("#############################################################################")
    menu = input("Enter a number from 1 to 5: ")
    
    if int(menu) == 1:
        print('Adding a Customer!!!')
    elif int(menu) == 2:
        print('Searching a Customer!!!')
    elif int(menu) == 3:
        print('Update Customers!!!')
    elif int(menu) == 4:
        print('Delete a Customer!!!')
    elif int(menu) == 5:
        sys.exit()
    else:
        print('Sorry, the value entered must be a number from 1 to 5, then try again!')

    
    menu()