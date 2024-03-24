'''
    [🐺🐺🐺]
    Edit. Nieto Salim Maula | 231524019
    a5.d4.polban.proyek1

    Notes:
    24/03/2024 : 03.00 WIB ["nito : make a menu rating"]
    24/03/2024 : 07.00 WIB ["nieto : oop edited"]
'''

#________________getLocally
from src import menu #ambil menu.py
from src import z_total #ambil z_total.py
from src import shape

#________________getEksternal
import os
from datetime import datetime

def printMenuRating():
    while True:

        z_total.cetak_wallet() #update the wallet
        
        shape.headerWallet() #get a Header from shape.py

        # Baca data dari file history.txt
        with open("data/history.txt", "r") as file:
            data = file.readlines()

        # Hitung total pemasukan dan pengeluaran
        total_pemasukan = 0
        total_pengeluaran = 0
        for line in data:
            parts = line.strip().split("|")
            if parts[0] == "pemasukan":
                total_pemasukan += float(parts[1])
            elif parts[0] == "pengeluaran":
                total_pengeluaran += float(parts[1])

        # Hitung rasio pemasukan ke pengeluaran
        ratio = total_pemasukan / total_pengeluaran if total_pengeluaran != 0 else 0

        # Tentukan level berdasarkan rasio
        if ratio >= 2:
            level = "A"
        elif ratio >= 1:
            level = "B"
        elif ratio >= 0.5:
            level = "C"
        else:
            level = "D"

        # Print informasi level dan kutipan yang sesuai
        print("|" + "\033[95m" + " (!) Rating untuk akun dompetQ mu adalah [{}]".format(level) + "                                       " + '\033[0m' + "|")
        print("|                                                                                   |")
        if level == "A":
            shape.contentLevelA()

        elif level == "B":
            shape.contentLevelB()

        elif level == "C":
            shape.contentLevelC()

        else: #__________________levelD
            shape.contentLevelD()

        print("|                                                                                   |")
        print("+-----------------------------------------------------------------------------------+")
        input("\n(!) Press Enter to continue...")
        menu.printMenu_main()
        os.system("cls")

'''
if __name__ == "__main__":
    printMenuIncomeOutcome()
'''