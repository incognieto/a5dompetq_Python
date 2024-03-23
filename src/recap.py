def printMenuRecap():
    print("| [1] Day					   	                          |")
    print("| [2] Week			   		                              |")
    print("| [3] Month			   		                              |")
    print("| [0] Back   						                      |")
    print("+----------------------------------------------------------+")

    while True:
        optionRecap = input("Choose an optionRecap: ")

        if optionRecap.isdigit():  # Memeriksa apakah input adalah digit
            optionRecap = int(optionRecap)
            if optionRecap == 1:
                #historyBylog()
                print("you accessed: Day")
            elif optionRecap == 2:
                #historyCategories()
                print("you accessed: Week")
            elif optionRecap == 3:
                #historyTransactionType()
                print("you accessed: Month")
            elif optionRecap == 0:
                print("Exit and Sign Out")
                return "back"  # Kembali ke menu utama
            else:
                print("Invalid optionRecap! Please try again.")
        else:
            print("Invalid input! Please enter a number.")
