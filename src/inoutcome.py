'''
    [🐱🐱🐱]
    Edit. Ratna Puspitasari | 231524019
    a5.d4.polban.proyek1

    Notes:
    22/03/2024 : 21.26 WIB ["ratna : update branch nya"]
    23/03/2024 : 04.40 WIB ["nito : digabungin ke template"]
    23/03/2024 : 05.10 WIB ["nito : script program lebih di modular kan"]
    23/03/2024 : 11.48 WIB ["ratna : edit printMenuIncomeOutcome() dan update ke branch"]
<<<<<<< HEAD
    24/03/2024 : 07.00 WIB ["nieto : oop edited"]
    24/03/2024 : 13.00 WIB ["ratna : nambah break"]
'''

#________________getLocally
from src import menu #ambil menu.py
from src import z_total #ambil z_total.py
from src import shape

#________________getEksternal
import os
from datetime import datetime
    
=======
    23/03/2024 : 23.25 WIB ["ratna : edit Outcome() ngebaca wallet dan update ke branch"]
'''

from src import menu #ambil menu.py

from src import z_total #ambil z_total.py
import os
from datetime import datetime

def getParameter_transaction():
    with open("data/nowLogin.txt", "r") as file:
        username_transaction = file.readline().strip()

    # Read balance from wallet.txt
    with open("data/wallet.txt", "r") as file:
        balance_transaction = file.readline().strip()

    return username_transaction, balance_transaction

def printHeader_transaction():
    username_transaction, balance_transaction = getParameter_transaction()  # Panggil fungsi getParameter() untuk mendapatkan username dan balance
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
    print("| Hi, {:<10s} | Wallet Balance : {:<10s} |  {:<30s}  |".format(username_transaction, balance_transaction, datetime.now().strftime('%A, %d %B %Y %I:%M %p')))
    print("+-----------------------------------------------------------------------------------+")

>>>>>>> c153946038cc5e8840ac745c25958748a2c28b49
#maybe Struct in Python??
class Saldo:
    def __init__(self):
        self.gaji = 0
        self.bonus = 0
        self.sampingan = 0
        self.pinjaman = 0
        self.uangKaget = 0
        self.inAll = 0
        self.tanggal = ""

#pengeluaran/outcome
def Outcome(saldo, jum, kategori, tgl):
    # Membaca saldo dari file wallet
    with open("data/wallet.txt", "r") as file:
<<<<<<< HEAD
        dompet = float(file.readline().strip())
        
    if dompet < jum:
=======
        wallet_balance = float(file.readline().strip())
        
    if wallet_balance < jum:
>>>>>>> c153946038cc5e8840ac745c25958748a2c28b49
        print("Saldo tidak mencukupi! Silakan isi pemasukan terlebih dahulu.")
    else:
        print(f"\nRiwayat pada {tgl}")
        print(f"Pengeluaran untuk {kategori}: Rp{jum}")
<<<<<<< HEAD
        newdompet = dompet - jum  # Menghitung sisa saldo baru setelah pengeluaran
        print(f"Sisa saldo: Rp{newdompet}")
        
        # Memperbarui saldo dalam file wallet setelah pengeluaran
        with open("data/wallet.txt", "w") as file:
            file.write(str(newdompet))
=======
        new_wallet_balance = wallet_balance - jum  # Menghitung sisa saldo baru setelah pengeluaran
        print(f"Sisa saldo: Rp{new_wallet_balance}")
        
        # Memperbarui saldo dalam file wallet setelah pengeluaran
        with open("data/wallet.txt", "w") as file:
            file.write(str(new_wallet_balance))
>>>>>>> c153946038cc5e8840ac745c25958748a2c28b49

#operasi catat ke file
def catat_pemasukan(saldo, jenis):
    with open("data/pemasukan_transaksi.txt", "a") as pemasukan_file:
        pemasukan_file.write(f"pemasukan|{saldo.inAll:.2f}|{jenis}|{saldo.tanggal}\n")

def catat_pengeluaran(saldo, jumlah, kategori):
    with open("data/pengeluaran_transaksi.txt", "a") as pengeluaran_file:
        pengeluaran_file.write(f"pengeluaran|{jumlah:.2f}|{kategori}|{saldo.tanggal}\n")

def catat_transaksi(saldo, jenis, jumlah, kategori=None):
    with open("data/history.txt", "a") as transaksi_file:
        if jenis == 'pemasukan':
            transaksi_file.write(f"{jenis}|{jumlah:.2f}|{kategori}|{saldo.tanggal}\n")
        elif jenis == 'pengeluaran':
            transaksi_file.write(f"{jenis}|{jumlah:.2f}|{kategori}|{saldo.tanggal}\n")

# ______________________Income Modul______________________________
def incomeModul(saldo):
<<<<<<< HEAD
    saldo.tanggal = input("\033[93m" + "\n[ Income ]" + "\033[0m" + " Masukkan tangal (DD-MM-YYYY): ")
=======
    saldo.tanggal = input("\n[ Income ] Masukkan tangal (DD-MM-YYYY): ")
>>>>>>> c153946038cc5e8840ac745c25958748a2c28b49
    print("\n[ Jenis Pemasukan ]")
    print("|___ [1] Gaji")
    print("|___ [2] Bonus")
    print("|___ [3] Sampingan")
    print("|___ [4] Pinjaman")
    print("|___ [5] Uang Kaget")
    
    pilJenis = int(input("\033[93m" + "\n[ Income Type ]" + "\033[0m" + " Masukkan Pilihan: "))
    
    if pilJenis in range(1, 6):
        jml = int(input("\033[93m" + f"\n[ Income Type ]" + "\033[om" + " Amount: Rp"))
        if pilJenis == 1:
            saldo.gaji += jml
            kategori = "Gaji"
        elif pilJenis == 2:
            saldo.bonus += jml
            kategori = "Bonus"
        elif pilJenis == 3:
            saldo.sampingan += jml
            kategori = "Sampingan"
        elif pilJenis == 4:
            saldo.pinjaman += jml
            kategori = "Pinjaman"
        elif pilJenis == 5:
            saldo.uangKaget += jml
            kategori = "Uang Kaget"
        
        saldo.inAll += jml

        print(f"(!) Pemasukan berhasil dicatat: Rp{jml}")
        catat_pemasukan(saldo, kategori)
        catat_transaksi(saldo, 'pemasukan', jml, kategori)

        #printMenuIncomeOutcome()

    else:
        print("Pilihan tidak valid!")

# ______________________Outcome Modul______________________________
def outcomeModul(saldo):
<<<<<<< HEAD
    saldo.tanggal = input("\033[93m" + "\n[ Outcome ]" + "\033[0m" + " Masukkan tanggal (DD-MM-YYYY): ")
=======
    saldo.tanggal = input("\n[ Outcome ] Masukkan tanggal (DD-MM-YYYY): ")
>>>>>>> c153946038cc5e8840ac745c25958748a2c28b49
    print("\n[ Jenis Pengeluaran ]")
    print("|___ [1] Belanja")
    print("|___ [2] Hiburan")
    print("|___ [3] Investasi")
    print("|___ [4] Kesehatan")
    print("|___ [5] Transportasi")
    print("|___ [6] Makanan")
    print("|___ [7] Minuman")
    print("|___ [8] Pajak")
    print("|___ [9] Pakaian")
    print("|___ [10] Pendidikan")
    print("|___ [11] Hutang")
    print("|___ [12] Sedekah")
    pilJenis = int(input("\033[93m" + "\n[ Outcome Type ]" + "\033[0m" + " Masukkan Pilihan: "))
    
    if pilJenis in range(1, 13):
        jml = int(input("\033[93m" + f"\n[ Outcome Type ]" + "\033[0m" + " Amount: Rp"))
        kategori = {
            1: "Belanja", 2: "Hiburan", 3: "Investasi", 4: "Kesehatan", 5: "Transportasi",
            6: "Makanan", 7: "Minuman", 8: "Pajak", 9: "Pakaian", 10: "Pendidikan",
            11: "Hutang", 12: "Sedekah"
        }[pilJenis]
        Outcome(saldo, jml, kategori, saldo.tanggal)
        catat_pengeluaran(saldo, jml, kategori)
        catat_transaksi(saldo, 'pengeluaran', jml, kategori)

        #printMenuIncomeOutcome()
    
    else:
        print("Pilihan tidak valid!")

def printMenuIncomeOutcome():
<<<<<<< HEAD
    while True:

        saldo = Saldo()

        z_total.cetak_wallet() #update the wallet
        
        shape.headerWallet() #get a Header from shape.py

        shape.menuTransaction()

        optionInoutcome = input("\033[93m" + "[ Transaction ]" "\033[0m" " Choose an option: ")
=======
    saldo = Saldo()
    
    while True:
        z_total.cetak_wallet()
        printHeader_transaction()
        print("| [1] Income                                                                        |")
        print("| [2] Outcome                                                                       |")
        print("| [0] Back                                                                          |")
        print("+-----------------------------------------------------------------------------------+")

        optionInoutcome = input("[ Transaction ] Choose an option: ")
>>>>>>> c153946038cc5e8840ac745c25958748a2c28b49

        if optionInoutcome.isdigit():  # Memeriksa apakah input adalah digit
            optionInoutcome = int(optionInoutcome)
            if optionInoutcome == 1:
                incomeModul(saldo)  # Memanggil fungsi incomeModul dengan objek saldo sebagai argumen
            elif optionInoutcome == 2:
                outcomeModul(saldo)  # Memanggil fungsi outcomeModul dengan objek saldo sebagai argumen
            elif optionInoutcome == 0:
                menu.printMenu_main()
                break
            else:
                print("Invalid optionInoutcome! Please try again.")
        else:
            print("Invalid input! Please enter a number.")
            
        input("(!) Press Enter to continue...")
        os.system("cls")

'''
def main():
    print("Welcome to Income and Outcome Tracker")

    while True:
        printMenuIncomeOutcome()
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice != 'yes':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
'''