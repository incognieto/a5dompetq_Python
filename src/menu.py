'''
    [🐺🐺🐺]
    Edit. Nieto Salim Maula | 231524019
    a5.d4.polban.proyek1

    Notes:
    23/03/2024 : 13.00 WIB ["nito : update branch nya"]
    23/03/2024 : 15.00 WIB ["nito : solving"]
    24/03/2024 : 07.00 WIB ["nieto : oop edited"]
    24/03/2024 : 13.00 WIB ["ratna : nambah break"]
'''

#________________getLocally
from src import diagram
from src import inoutcome, history, recap, savings, z_total, rating
from src import shape

#________________getEksternal
import os
<<<<<<< HEAD
from datetime import datetime

def printMenu_main():
    while True:
=======
from src import inoutcome, history, recap, savings, export, z_total

from datetime import datetime

def getParameter_main():
    with open("data/nowLogin.txt", "r") as file:
        username_main = file.readline().strip()

    # Read balance from wallet.txt
    with open("data/wallet.txt", "r") as file:
        balance_main = file.readline().strip()

    return username_main, balance_main

def printHeader_main():
    username_main, balance_main = getParameter_main()  # Panggil fungsi getParameter() untuk mendapatkan username dan balance
    os.system("cls")
    print("+-----------------------------------------------------------------------------------+")
    print("|    ________     ______  ___      ___   _______   _______ ___________ ______       |")
    print("|    |\"      \"\\   /    \" \\|\"  \\    /\"  | |   __ \"\\ /\"     \"(\"     _   \"/    \" \\     |")
    print("|    (.  ___  :) // ____  \\\\   \\  //   | (. |__) :(: ______))__/  \\\\__// ____  \\    |")
    print("|    |: \\   ) ||/  /    ) :/\\\\  \\/\\.    | |:  ____/ \\/    |     \\\\_ / /  /    ) )   |")
    print("|    (| (___\\ |(: (____/ /|: \\.        | (|  /     // ___)_    |.  |(: (____/ //    |")
    print("|    |:       :)\        /|.  \\    /:  |/|__/ \\   (:      \"|   \\:  | \\         \\    |")
    print("|    (________/  \\\"_____/ |___|\\__/|___(_______)   \\_______)    \\__|  \"____/\\__\\    |")
    print("|                                                                                   |")
    print("|    Strategize, Organize, and Thrive: Your Financial Companion @a5polbanjtk        |")
    print("|                                                                                   |")
    print("+-----------------------------------------------------------------------------------+")
    print("| Hi, {:<10s} | Wallet Balance : {:<10s} |  {:<30s}  |".format(username_main, balance_main, datetime.now().strftime('%A, %d %B %Y %I:%M %p')))
    print("+-----------------------------------------------------------------------------------+")

def printMenu_main():
    while True:

        z_total.cetak_wallet()
        
        printHeader_main()

        print("|                                                                                   |")
        print("|                            [1] Add Transaction                                    |")
        print("|                            [2] History                                            |")
        print("|                            [3] Recapitulation                                     |")
        print("|                            [4] Savings                                            |")
        print("|                            [5] Export and Import                                  |")
        print("|                            [6] About                                              |")
        print("|                            [0] Exit and SignOut                                   |")
        print("|                                                                                   |")
        print("+-----------------------------------------------------------------------------------+")
>>>>>>> c153946038cc5e8840ac745c25958748a2c28b49

        z_total.cetak_wallet() #update the wallet
        
        shape.headerWallet() #get a Header from shape.py

        shape.mainMenu()

        option = input("\033[93m" + "[ Menu ]" + "\033[0m" + " Choose an option: ")

        if option.isdigit():  # Memeriksa apakah input adalah digit
            option = int(option)
            if option == 1:
                os.system("cls")
                inoutcome.printMenuIncomeOutcome()
<<<<<<< HEAD
                break
            elif option == 2:
                os.system("cls")
                history.printMenuHistory()
                break
            elif option == 3:
                os.system("cls")
                recap.printMenuRecap()
                break
            elif option == 4:
                os.system("cls")
                savings.printMenuSavings()
                break
            elif option == 5:
                os.system("cls")
                diagram.printMenuDiagram()
                break
=======
            elif option == 2:
                os.system("cls")
                history.printMenuHistory()
            elif option == 3:
                os.system("cls")
                recap.printMenuRecap()
            elif option == 4:
                os.system("cls")
                savings.printMenuSavings()
            elif option == 5:
                os.system("cls")
                export.printMenuExport()
>>>>>>> c153946038cc5e8840ac745c25958748a2c28b49
            elif option == 6:
                os.system("cls")
                rating.printMenuRating()
                break
            elif option == 0:
                print("Exit and Sign Out")
                break  # Keluar dari loop utama dan program selesai
            else:
                print("Invalid option! Please try again.")
        else:
            print("Invalid input! Please enter a number.")

'''
def main():
    # Read username from nowLogin.txt
    with open("data/nowLogin.txt", "r") as file:
        username = file.readline().strip()

    # Read balance from wallet.txt
    with open("data/wallet.txt", "r") as file:
        balance = file.readline().strip()

    printHeader_b(username, balance)

if __name__ == "__main__":
    main()
'''