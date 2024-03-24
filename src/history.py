'''
    [🐺🐺🐺]
    Edit. Nieto Salim Maula | 231524019
    a5.d4.polban.proyek1

    Notes:
    23/03/2024 : 19.00 WIB ["nito : update branch nya"]
    23/03/2024 : 19.00 WIB ["nito : solving"]
    24/03/2024 : 07.00 WIB ["nieto : oop edited"]
'''

#________________getLocally
from src import menu #ambil menu.py
from src import z_total #ambil z_total.py
from src import shape

#________________getEksternal
import os
from datetime import datetime
    
def display_transaction_log():
    try:
        print("+--------------------------- [ Sort By Log Transaction ] ---------------------------+")
        print("|")
        with open("data/history.txt", "r") as history_file:
            for line in history_file:
                print("|__", line.strip())
    except FileNotFoundError:
        print("Error opening file history.txt")

def display_sorted_by_categories():
    try:
        print("+----------------------------- [ Sort By Categories ] ------------------------------+")
        categories = {}
        
        with open("data/history.txt", "r") as history_file:
            for line in history_file:
                category = line.split("|")[2].strip().upper()
                if category not in categories:
                    categories[category] = []
                categories[category].append(line.strip())

        for category, transactions in categories.items():
            print("|")
            print("|__ (@) [{}]".format(category))
            for transaction in transactions:
                print("|__ (*)", transaction)

    except FileNotFoundError:
        print("Error opening file history.txt")

def display_sorted_by_type():
    try:
        print("+-------------------------- [ Sort By Type Transaction ] ---------------------------+")
        print_pemasukan_contents()
        print_pengeluaran_contents()
    except FileNotFoundError:
        print("Error opening file history.txt")


def print_pengeluaran_contents():
    try:
        print("|")
        print("|_____ [@] Outcome | Pengeluaran")
        with open("data/pengeluaran_transaksi.txt", "r") as file:
            for line in file:
                print("|_________ (*)", line.strip())
    except FileNotFoundError:
        print("Error opening file pengeluaran_transaksi.txt")

def print_pemasukan_contents():
    try:
        print("|")
        print("|_____ [@] Income | Pemasukan")
        with open("data/pemasukan_transaksi.txt", "r") as file:
            for line in file:
                print("|_________ (*)", line.strip())
    except FileNotFoundError:
        print("Error opening file pemasukan_transaksi.txt")


def printMenuHistory():
    while True:
        
        z_total.cetak_wallet() #update the wallet
        
        shape.headerWallet() #get a Header from shape.py
        
        shape.menuHistory()

        optionHistory = input("\033[96m" + "[ History ]" + "\033[0m" + " Choose an option: ")

        if optionHistory.isdigit():  # Memeriksa apakah input adalah digit
            optionHistory = int(optionHistory)
            if optionHistory == 1:
                shape.menuHistory()
                display_transaction_log()  # Panggil fungsi untuk menampilkan log transaksi
                input("\n (!) Press Enter to continue...")
            elif optionHistory == 2:
                shape.menuHistory()
                display_sorted_by_categories()  # Panggil fungsi untuk menampilkan transaksi yang telah diurutkan berdasarkan kategori
                input("\n(!) Press Enter to continue...")
            elif optionHistory == 3:
                display_sorted_by_type() # Panggil fungsi untuk menampilkan transaksi berdasarkan jenis transaksi
                input("\n(!) Press Enter to continue...")
            elif optionHistory == 0:
                menu.printMenu_main()
                break
            else:
                print("Invalid optionHistory! Please try again.")
        else:
            print("Invalid input! Please enter a number.")
'''
def main():
    printMenuHistory()

if __name__ == "__main__":
    main()
'''
