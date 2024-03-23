import os
from inoutcome import printMenuIncomeOutcome
from history import printMenuHistory
from recap import printMenuRecap
from savings import printMenuSavings
from export import printMenuExport
from datetime import datetime

def printHeader_b(username, balance):
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
    print("| Hi, {:<10s} |  {:<30s}  | Wallet Balance : {:<10s} |".format(username, datetime.now().strftime('%A, %d %B %Y %I:%M %p'), balance))
    print("+-----------------------------------------------------------------------------------+")

#def printHeader_c(username):
def printHeader_c():
    #savings_balance = bacasaving()
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
    #print("| Hi, {:<20s} | Savings Balance : {:<10.2f}  |".format(username, savings_balance))
    print("+-----------------------------------------------------------------------------------+")

def printMenu_b(username, balance):
    while True:
        printHeader_b(username, balance)
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
                printMenuIncomeOutcome()
            elif option == 2:
                printMenuHistory()
            elif option == 3:
                printMenuRecap()
            elif option == 4:
                printMenuSavings()
            elif option == 5:
                printMenuExport()
            elif option == 6:
                print("About")
            elif option == 0:
                print("Exit and Sign Out")
                break  # Keluar dari loop utama dan program selesai
            else:
                print("Invalid option! Please try again.")
        else:
            print("Invalid input! Please enter a number.")


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