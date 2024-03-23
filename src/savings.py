def printMenuSavings():
    print("| [1] Add Savings Balance                                  |")
    print("| [2] Subtract Savings Balance                             |")
    print("| [3] History Savings Balance                              |")
    print("| [0] Back                                                 |")
    print("+----------------------------------------------------------+")

    while True:
        optionSavings = input("Choose an optionSavings: ")

        if optionSavings.isdigit():  # Memeriksa apakah input adalah digit
            optionSavings = int(optionSavings)
            if optionSavings == 1:
                #historyBylog()
                print("you accessed: add savings")
            elif optionSavings == 2:
                #historyCategories()
                print("you accessed: sub savings")
            elif optionSavings == 3:
                #historyTransactionType()
                print("you accessed: history savings")
            elif optionSavings == 0:
                print("Exit and Sign Out")
                return "back"  # Kembali ke menu utama
            else:
                print("Invalid optionSavings! Please try again.")
        else:
            print("Invalid input! Please enter a number.")
