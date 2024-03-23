def printMenuHistory():
    print("| [1] by Log                                               |")
    print("| [2] by Categories                                        |")
    print("| [3] by Transaction type                                  |")
    print("| [0] Back                                                 |")
    print("+----------------------------------------------------------+")

    while True:
        optionHistory = input("Choose an optionHistory: ")

        if optionHistory.isdigit():  # Memeriksa apakah input adalah digit
            optionHistory = int(optionHistory)
            if optionHistory == 1:
                #historyBylog()
                print("you accessed: by log")
            elif optionHistory == 2:
                #historyCategories()
                print("you accessed: categories")
            elif optionHistory == 3:
                #historyTransactionType()
                print("you accessed: transaction type")
            elif optionHistory == 0:
                print("Exit and Sign Out")
                return "back"  # Kembali ke menu utama
            else:
                print("Invalid optionHistory! Please try again.")
        else:
            print("Invalid input! Please enter a number.")

