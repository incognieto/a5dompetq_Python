'''
    [🦊🦊🦊]
    Edit. Jizdan Mulkan Nailan | 231524019
    a5.d4.polban.proyek1

    Notes:
    22/03/2024 : 20.48 WIB ["jizdan : update branch nya"]
    23/03/2024 : 09.45 WIB ["nito : digabungin ke template"]
    23/03/2024 : 09.45 WIB ["nito : script program lebih di modular kan"]
    23/03/2024 : 09.55 WIB ["nito : hapus program write karena mengubah data wallet"]
'''

def printMenuRecap():

    print("+-----------------------------------------------------------------------------------+")
    print("| [1] Day                                                                           |")
    print("| [2] Week                                                                          |")
    print("| [3] Month                                                                         |")
    print("| [0] Back                                                                          |")
    print("+-----------------------------------------------------------------------------------+")

    while True:
        optionRecap = input("[ Recap ] Choose an option: ")

        if optionRecap.isdigit():  # Memeriksa apakah input adalah digit
            optionRecap = int(optionRecap)
            if optionRecap == 1:
                tanggal = input("\n[ Daily ] Masukkan Tanggal (DD-MM-YYYY): ")
                update_saldo_harian(tanggal)
            elif optionRecap == 2:
                tgl_awal = input("\n[ Weekly ] Masukkan Tanggal Awal (DD-MM-YYYY): ")
                tgl_akhir = input("[ Weekly ] Masukkan Tanggal Akhir (DD-MM-YYYY): ")
                update_saldo_mingguan(tgl_awal, tgl_akhir)
            elif optionRecap == 3:
                bulan = input("\n[ Monthly ] Masukkan Bulan (MM): ")
                tahun = input("[ Monthly ] Masukkan Tahun (YYYY): ")
                update_saldo_bulanan(bulan, tahun)
            elif optionRecap == 0:
                print("Exit and Sign Out")
                return "back"  # Kembali ke menu utama
            else:
                print("Invalid optionRecap! Please try again.")
        else:
            print("Invalid input! Please enter a number.")
    
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
    print("|__ Date            :", bulan, "-", tahun)
    print("|__ Total Income    :", total_pemasukan)
    print("|__ Total Outcome   :", total_pengeluaran)
    print("|__ Sisa Saldo      :", saldo)

    return total_pemasukan, total_pengeluaran

'''
def main():
    printMenuRecap()

if __name__ == "__main__":
    main()
'''
