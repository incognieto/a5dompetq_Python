def printMenuExport():
    print("| [1] Export                                               |")
    print("| [2] Import                                               |")
    print("| [0] Back                                                 |")
    print("+----------------------------------------------------------+")

    while True:
        optionExport = input("Choose an optionExport: ")

        if optionExport.isdigit():  # Memeriksa apakah input adalah digit
            optionExport = int(optionExport)
            if optionExport == 1:
                #historyBylog()
                print("you accessed: Export")
            elif optionExport == 2:
                #historyCategories()
                print("you accessed: Import")
            elif optionExport == 0:
                print("Exit and Sign Out")
                return "back"  # Kembali ke menu utama
            else:
                print("Invalid optionExport! Please try again.")
        else:
            print("Invalid input! Please enter a number.")
