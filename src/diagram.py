'''
    [🐺🐺🐺]
    Edit. Nieto Salim Maula | 231524019
    a5.d4.polban.proyek1

    Notes:
    23/03/2024 : 20.00 WIB ["nito : make a menu diagram"]
    24/03/2024 : 13.00 WIB ["ratna : nambah break"]
'''

#________________getLocally
from src import menu #ambil menu.py
from src import z_total #ambil z_total.py
from src import shape
from src import z_frekuensi_transaksi
from src import z_frekuensi_type

#________________getEksternal
import os
from datetime import datetime
    
def printMenuDiagram():
    while True:

        z_total.cetak_wallet() #update the wallet
        
        shape.headerWallet() #get a Header from shape.py

        shape.menuDiagram()

        optionDiagram = input("\033[93m" + "[ Diagram ]" + "\033[0m" + "Choose an option: ")

        if optionDiagram.isdigit():  # Memeriksa apakah input adalah digit
            optionDiagram = int(optionDiagram)
            if optionDiagram == 1:
                #print("Accessed: Satu")
                z_frekuensi_transaksi.main()
                break
            elif optionDiagram == 2:
                #print("Accessed: Dua")
                z_frekuensi_type.main()
                break
            elif optionDiagram == 0:
                menu.printMenu_main()
                break
            else:
                print("Invalid optionDiagram! Please try again.")
        else:
            print("Invalid input! Please enter a number.")
            
        input("\n(!) Press Enter to continue...")
        
        os.system("cls")
        
'''
if __name__ == "__main__":
    printMenuIncomeOutcome()
'''