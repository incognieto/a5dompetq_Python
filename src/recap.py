'''
    [🦊🦊🦊]
    Edit. Jizdan Mulkan Nailan | 231524019
    a5.d4.polban.proyek1

    Notes:
    22/03/2024 : 20.48 WIB ["jizdan : update branch nya"]
    23/03/2024 : 09.45 WIB ["nito : digabungin ke template"]
    23/03/2024 : 09.45 WIB ["nito : script program lebih di modular kan"]
    23/03/2024 : 09.55 WIB ["nito : hapus program write karena mengubah data wallet"]
    24/03/2024 : 07.00 WIB ["nieto : oop edited"]
'''

#________________getLocally
from src import menu
from src import z_total #ambil z_total.py
from src import shape

#________________getEksternal
import os
from datetime import datetime
       
def update_saldo_harian(tanggal):
    total_pemasukan = 0.0
    total_pengeluaran = 0.0

    # Accumulate total income
    with open("data/pemasukan_transaksi.txt", "r") as pemasukan_file:
        for line in pemasukan_file:
            parts = line.strip().split('|')
            if len(parts) == 4:  # Ensure the line has the correct format
                amount, _, date = parts[1:]
                if date == tanggal:
                    total_pemasukan += float(amount)

    # Accumulate total outcome
    with open("data/pengeluaran_transaksi.txt", "r") as pengeluaran_file:
        for line in pengeluaran_file:
            parts = line.strip().split('|')
            if len(parts) == 4:  # Ensure the line has the correct format
                amount, _, date = parts[1:]
                if date == tanggal:
                    total_pengeluaran += float(amount)

    saldo = total_pemasukan - total_pengeluaran

    # Print the daily recap
    print("\n[ @Daily Recap ]")
    print("|__ Date            :", tanggal)
    print("|__ Total Income    :", total_pemasukan)
    print("|__ Total Outcome   :", total_pengeluaran)
    print("|__ Sisa Saldo      :", saldo)

    return total_pemasukan, total_pengeluaran

def update_saldo_mingguan(tgl_awal, tgl_akhir):
    total_pemasukan = 0.0
    total_pengeluaran = 0.0

    # Accumulate total income for the week
    with open("data/pemasukan_transaksi.txt", "r") as pemasukan_file:
        for line in pemasukan_file:
            parts = line.strip().split('|')
            if len(parts) == 4:  # Ensure the line has the correct format
                amount, _, date = parts[1:]
                if tgl_awal <= date <= tgl_akhir:
                    total_pemasukan += float(amount)

    # Accumulate total outcome for the week
    with open("data/pengeluaran_transaksi.txt", "r") as pengeluaran_file:
        for line in pengeluaran_file:
            parts = line.strip().split('|')
            if len(parts) == 4:  # Ensure the line has the correct format
                amount, _, date = parts[1:]
                if tgl_awal <= date <= tgl_akhir:
                    total_pengeluaran += float(amount)

    saldo = total_pemasukan - total_pengeluaran
    
    # Print the weekly recap
    print("\n[ @Weekly Recap ]")
    print("|__ Date            :", tgl_awal, " TO ", tgl_akhir)
    print("|__ Total Income    :", total_pemasukan)
    print("|__ Total Outcome   :", total_pengeluaran)
    print("|__ Sisa Saldo      :", saldo)

    return total_pemasukan, total_pengeluaran

def update_saldo_bulanan(bulan, tahun):
    total_pemasukan = 0.0
    total_pengeluaran = 0.0

    # Accumulate total income for the month
    with open("data/pemasukan_transaksi.txt", "r") as pemasukan_file:
        for line in pemasukan_file:
            parts = line.strip().split('|')
            if len(parts) == 4:  # Ensure the line has the correct format
                amount, _, date = parts[1:]
                if date[3:5] == bulan and date[6:] == tahun:
                    total_pemasukan += float(amount)

    # Accumulate total outcome for the month
    with open("data/pengeluaran_transaksi.txt", "r") as pengeluaran_file:
        for line in pengeluaran_file:
            parts = line.strip().split('|')
            if len(parts) == 4:  # Ensure the line has the correct format
                amount, _, date = parts[1:]
                if date[3:5] == bulan and date[6:] == tahun:
                    total_pengeluaran += float(amount)

    saldo = total_pemasukan - total_pengeluaran
    
    # Print the monthly recap
    print("\n[ @Monthly Recap ]")
    print("|__ Month - Year    :", bulan, "-", tahun)
    print("|__ Total Income    :", total_pemasukan)
    print("|__ Total Outcome   :", total_pengeluaran)
    print("|__ Sisa Saldo      :", saldo)

    return total_pemasukan, total_pengeluaran

def printMenuRecap():

    while True:

        z_total.cetak_wallet() #update the wallet
        
        shape.headerWallet() #get a Header from shape.py

        shape.menuRecap()
        
        optionRecap = input("[ Recap ] Choose an option: ")

        if optionRecap.isdigit():  # Memeriksa apakah input adalah digit
            optionRecap = int(optionRecap)
            if optionRecap == 1:
                tanggal = input("\n[ Daily ] Masukkan Tanggal (DD-MM-YYYY): ")
                # Memanggil fungsi update_saldo_harian dan mencetak rekap harian
                total_pemasukan, total_pengeluaran = update_saldo_harian(tanggal)
                # Melanjutkan ke langkah berikutnya setelah pengguna menekan ENTER
                input("\n(!) Press Enter to continue...")
            elif optionRecap == 2:
                tgl_awal = input("\n[ Weekly ] Masukkan Tanggal Awal (DD-MM-YYYY): ")
                tgl_akhir = input("[ Weekly ] Masukkan Tanggal Akhir (DD-MM-YYYY): ")
                # Memanggil fungsi update_saldo_mingguan dan mencetak rekap mingguan
                total_pemasukan, total_pengeluaran = update_saldo_mingguan(tgl_awal, tgl_akhir)
                # Melanjutkan ke langkah berikutnya setelah pengguna menekan ENTER
                input("\n(!) Press Enter to continue...")
            elif optionRecap == 3:
                bulan = input("\n[ Monthly ] Masukkan Bulan (MM): ")
                tahun = input("[ Monthly ] Masukkan Tahun (YYYY): ")
                # Memanggil fungsi update_saldo_bulanan dan mencetak rekap bulanan
                total_pemasukan, total_pengeluaran = update_saldo_bulanan(bulan, tahun)
                # Melanjutkan ke langkah berikutnya setelah pengguna menekan ENTER
                input("\n(!) Press Enter to continue...")
            elif optionRecap == 0:
                menu.printMenu_main()
                break
            else:
                print("(!) Invalid option! Please try again.")
        else:
            print("(!) Invalid input! Please enter a number.")

'''
def main():
    printMenuRecap()

if __name__ == "__main__":
    main()
'''
