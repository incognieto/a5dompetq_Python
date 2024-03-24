from src import menu #ambil menu.py

from src import z_total #ambil z_total.py
import os
from datetime import datetime

def getParameter_history():
    with open("data/nowLogin.txt", "r") as file:
        username_history = file.readline().strip()

    # Read balance from wallet.txt
    with open("data/wallet.txt", "r") as file:
        balance_history = file.readline().strip()

    return username_history, balance_history

def printHeader_history():
    username_history, balance_history = getParameter_history()  # Panggil fungsi getParameter() untuk mendapatkan username dan balance
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
    print("| Hi, {:<10s} | Wallet Balance : {:<10s} |  {:<30s}  |".format(username_history, balance_history, datetime.now().strftime('%A, %d %B %Y %I:%M %p')))
    print("+-----------------------------------------------------------------------------------+")

def display_transaction_log():
    try:
        with open("data/history.txt", "r") as history_file:
            for line in history_file:
                print(line, end="")
        print("----------------------[Transaction Log]---------------------")
    except FileNotFoundError:
        print("Error opening file history.txt")

def display_sorted_by_categories():
    try:
        with open("data/history.txt", "r") as history_file:
            # Read all transactions into a list
            transactions = [line.strip() for line in history_file]

        # Sort the transactions based on categories
        transactions.sort(key=lambda x: x.split('|')[2])

        for transaction in transactions:
            print(transaction)

        # Display the sorted transactions
        print("--------------------[Sort By Categories]-------------------")
    except FileNotFoundError:
        print("Error opening file history.txt")

def print_pengeluaran_contents():
    try:
        with open("data/pengeluaran_transaksi.txt", "r") as file:
            print("\n--------------------[Outcome History]-------------------\n")
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print("Error opening file pengeluaran_transaksi.txt")

def print_pemasukan_contents():
    try:
        with open("data/pemasukan_transaksi.txt", "r") as file:
            print("\n--------------------[Income History]-------------------\n")
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print("Error opening file pemasukan_transaksi.txt")

def printMenuHistory():
    while True:
        optionHistory = input("Choose an optionHistory: ")

        z_total.cetak_wallet()

        printHeader_history()

        print("| [1] by Log                                                                         |")
        print("| [2] by Categories                                                                  |")
        print("| [3] by Transaction type                                                            |")
        print("| [0] Back                                                                           |")
        print("+------------------------------------------------------------------------------------+")

        if optionHistory.isdigit():  # Memeriksa apakah input adalah digit
            optionHistory = int(optionHistory)
            if optionHistory == 1:
                printHeader_history()
                display_transaction_log()  # Panggil fungsi untuk menampilkan log transaksi
            elif optionHistory == 2:
                printHeader_history()
                display_sorted_by_categories()  # Panggil fungsi untuk menampilkan transaksi yang telah diurutkan berdasarkan kategori
            elif optionHistory == 3:
                # Panggil fungsi untuk menampilkan transaksi berdasarkan jenis transaksi
                print_pemasukan_contents()
                print_pengeluaran_contents()
            elif optionHistory == 0:
                menu.printMenu_main()
                #print("Exit and Sign Out")
                #return "back"  # Kembali ke menu utama
            else:
                print("Invalid optionHistory! Please try again.")
        else:
            print("Invalid input! Please enter a number.")

def main():
    printMenuHistory()

if __name__ == "__main__":
    main()

