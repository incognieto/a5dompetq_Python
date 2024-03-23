import os
import inoutcome, history, recap, savings, export, z_total

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

        option = input("[ Menu ] Choose an option: ")

        if option.isdigit():  # Memeriksa apakah input adalah digit
            option = int(option)
            if option == 1:
                os.system("cls")
                inoutcome.printMenuIncomeOutcome()
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
            elif option == 6:
                print("About")
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