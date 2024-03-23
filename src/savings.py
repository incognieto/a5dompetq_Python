'''
    [🐨🐨🐨]
    Edit. Naomi Erica | 231524019
    a5.d4.polban.proyek1

    Notes:
    22/03/2024 : 18.30 WIB ["naomi : update branch nya"]
    23/03/2024 : 12.40 WIB ["nito : digabungin ke template"]
    23/03/2024 : 12.50 WIB ["nito : solve tidak ke implement menu"]
'''

import os
from datetime import datetime

def getParameter():
    with open("data/nowLogin.txt", "r") as file:
        username2 = file.readline().strip()

    # Read balance from wallet.txt
    with open("data/savings.txt", "r") as file:
        balance2 = file.readline().strip()

    return username2, balance2

def printHeader_c():
    username2, balance2 = getParameter()  # Panggil fungsi getParameter() untuk mendapatkan username dan balance
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
    print("| Hi, {:<10s} | Savings Balance : {:<10s}|  {:<30s}  |".format(username2, balance2, datetime.now().strftime('%A, %d %B %Y %I:%M %p')))
    print("+-----------------------------------------------------------------------------------+")

#baca file savings
def bacasaving():
    try:
        with open("data/savings.txt", "r") as savings_file:
            saving = float(savings_file.readline())
            return saving
    except FileNotFoundError:
        print("Error: File savings.txt tidak ditemukan")
        return -1.0
    except ValueError:
        print("Error: Data tidak valid dalam file savings.txt")
        return -1.0

#tampil sisa tabungan
def printsisa(saving):
    print(f"Sisa saving Anda adalah: {saving:.2f}")

#update tabungan
def updatesaving():
    total_savings = 0.0
    total_pengeluaran = 0.0

    # Baca file addsavings.txt
    try:
        with open("data/addsavings.txt", "r") as pemasukan_savings:
            for line in pemasukan_savings:
                if line.startswith("incomeSaving|"):
                    amount = float(line.split("|")[1])
                    total_savings += amount
    except FileNotFoundError:
        print("Error: File addsavings.txt tidak ditemukan")

    # Baca file subsavings.txt
    try:
        with open("data/subsavings.txt", "r") as pengeluaran_savings:
            for line in pengeluaran_savings:
                if line.startswith("outcomeSaving|"):
                    amount = float(line.split("|")[1])
                    total_pengeluaran += amount
    except FileNotFoundError:
        print("Error: File subsavings.txt tidak ditemukan")

    saving = total_savings - total_pengeluaran

    # Simpan saving ke dalam file savings.txt
    try:
        with open("data/savings.txt", "w") as savings_file:
            savings_file.write(f"{saving:.2f}")
            print("saving berhasil diupdate pada file savings.txt")
            # Baca dan cetak sisa saving
            printsisa(saving)
    except FileNotFoundError:
        print("Error: File savings.txt tidak ditemukan")
    
    # Membersihkan layar sebelum mencetak header dan menu
    os.system('cls' if os.name == 'nt' else 'clear')

#tambah tabungan
def addSaving(jumlah):
    writeSaving("data/addsavings.txt", "incomeSaving", jumlah)

#kurangi tabungan
def subSaving(jumlah):
    writeSaving("data/subsavings.txt", "outcomeSaving", jumlah)

#tulis ke file
def writeSaving(nama_file, jenis, jumlah):
    try:
        with open(nama_file, "a") as file:
            file.write(f"{jenis}|{jumlah:.2f}\n")
    except FileNotFoundError:
        print(f"Error: File {nama_file} tidak ditemukan")

    try:
        with open("data/history_savings.txt", "a") as history_file:
            history_file.write(f"{jenis}|{jumlah:.2f}\n")
    except FileNotFoundError:
        print("Error: File history_savings.txt tidak ditemukan")

#tampil history
def tampilHistory():
    try:
        print("\n[ History Savings Balance ]")
        with open("data/history_savings.txt", "r") as log_file:
            for line in log_file:
                data = line.strip().split("|")
                if len(data) == 2:
                    jenis, jumlah = data
                    print(f"|__ Jumlah: {jumlah}, Jenis: {jenis}")
                else:
                    print("(!) Format log tidak valid:", line.strip())
    except FileNotFoundError:
        print("Error: File history_savings.txt tidak ditemukan")

    input("\n(!) Press ENTER to return to Savings Menu")
    os.system("cls")
    updatesaving()

#menu tabungan
def printMenuSavings():
    while True:
        
        printHeader_c()

        # Mendapatkan saldo tabungan
        saldo = bacasaving()
        if saldo == -1.0:
            return
        
        print("| [1] Add Savings Balance                                                           |")
        print("| [2] Subtract Savings Balance                                                      |")
        print("| [3] History Savings Balance                                                       |")
        print("| [0] Back                                                                          |")
        print("+-----------------------------------------------------------------------------------+")
        
        pilihan = input("[ Savings ] Choose an option: ")

        if pilihan == "1":
            jumlah = float(input("\n[ Add Savings Balance ] Amount\t: Rp"))
            addSaving(jumlah)
            updatesaving()
            print("")
        elif pilihan == "2":
            jumlah = float(input("\n[ Subtract Savings Balance ] Amount\t: Rp"))
            subSaving(jumlah)
            updatesaving()
            print("")
        elif pilihan == "3":
            print("\n[ History Savings Balance ]")
            tampilHistory()
            print("")
        elif pilihan == "0":
            print("Exit and Sign Out")
            return "back"  # Mengembalikan string 'back' agar menu utama diaktifkan kembali
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

#printMenuSavings()