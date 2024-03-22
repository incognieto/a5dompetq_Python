def update_saldo_harian(tanggal):
    total_pemasukan = 0.0
    total_pengeluaran = 0.0

    # Accumulate total income
    with open("a5dompetq_Python/data/pemasukan_transaksi.txt", "r") as pemasukan_file:
        for line in pemasukan_file:
            parts = line.strip().split('|')
            if len(parts) == 4:  # Ensure the line has the correct format
                amount, _, date = parts[1:]
                if date == tanggal:
                    total_pemasukan += float(amount)

    # Accumulate total outcome
    with open("a5dompetq_Python/data/pengeluaran_transaksi.txt", "r") as pengeluaran_file:
        for line in pengeluaran_file:
            parts = line.strip().split('|')
            if len(parts) == 4:  # Ensure the line has the correct format
                amount, _, date = parts[1:]
                if date == tanggal:
                    total_pengeluaran += float(amount)

    saldo = total_pemasukan - total_pengeluaran

    # Write the balance to the wallet.txt file
    with open("a5dompetq_Python/data/wallet.txt", "w") as wallet_file:
        wallet_file.write("{:.2f}".format(saldo))

    print("Saldo berhasil diupdate pada file wallet.txt")

    # Print the daily recap
    print("\nDAILY RECAP")
    print("Date            :", tanggal)
    print("Total Income    :", total_pemasukan)
    print("Total Outcome   :", total_pengeluaran)
    print("Sisa Saldo      :", saldo)

    return total_pemasukan, total_pengeluaran

def input_user_day():
    tanggal = input("Masukkan Tanggal (dd-mm-yyyy): ")
    return tanggal

def update_saldo_mingguan(tgl_awal, tgl_akhir):
    total_pemasukan = 0.0
    total_pengeluaran = 0.0

    # Accumulate total income for the week
    with open("a5dompetq_Python/data/pemasukan_transaksi.txt", "r") as pemasukan_file:
        for line in pemasukan_file:
            parts = line.strip().split('|')
            if len(parts) == 4:  # Ensure the line has the correct format
                amount, _, date = parts[1:]
                if tgl_awal <= date <= tgl_akhir:
                    total_pemasukan += float(amount)

    # Accumulate total outcome for the week
    with open("a5dompetq_Python/data/pengeluaran_transaksi.txt", "r") as pengeluaran_file:
        for line in pengeluaran_file:
            parts = line.strip().split('|')
            if len(parts) == 4:  # Ensure the line has the correct format
                amount, _, date = parts[1:]
                if tgl_awal <= date <= tgl_akhir:
                    total_pengeluaran += float(amount)

    saldo = total_pemasukan - total_pengeluaran

    # Write the balance to the wallet.txt file
    with open("a5dompetq_Python/data/wallet.txt", "w") as wallet_file:
        wallet_file.write("{:.2f}".format(saldo))

    print("Saldo berhasil diupdate pada file wallet.txt")

    # Print the weekly recap
    print("\nWEEKLY RECAP")
    print("Date            :", tgl_awal, "-", tgl_akhir)
    print("Total Income    :", total_pemasukan)
    print("Total Outcome   :", total_pengeluaran)
    print("Sisa Saldo      :", saldo)

    return total_pemasukan, total_pengeluaran

def input_user_week():
    tgl_awal = input("Masukkan Tanggal Awal (dd-mm-yyyy): ")
    tgl_akhir = input("Masukkan Tanggal Akhir (dd-mm-yyyy): ")
    return tgl_awal, tgl_akhir

def update_saldo_bulanan(bulan, tahun):
    total_pemasukan = 0.0
    total_pengeluaran = 0.0

    # Accumulate total income for the month
    with open("a5dompetq_Python/data/pemasukan_transaksi.txt", "r") as pemasukan_file:
        for line in pemasukan_file:
            parts = line.strip().split('|')
            if len(parts) == 4:  # Ensure the line has the correct format
                amount, _, date = parts[1:]
                if date[3:5] == bulan and date[6:] == tahun:
                    total_pemasukan += float(amount)

    # Accumulate total outcome for the month
    with open("a5dompetq_Python/data/pengeluaran_transaksi.txt", "r") as pengeluaran_file:
        for line in pengeluaran_file:
            parts = line.strip().split('|')
            if len(parts) == 4:  # Ensure the line has the correct format
                amount, _, date = parts[1:]
                if date[3:5] == bulan and date[6:] == tahun:
                    total_pengeluaran += float(amount)

    saldo = total_pemasukan - total_pengeluaran

    # Write the balance to the wallet.txt file
    with open("a5dompetq_Python/data/wallet.txt", "w") as wallet_file:
        wallet_file.write("{:.2f}".format(saldo))

    print("Saldo berhasil diupdate pada file wallet.txt")

    # Print the monthly recap
    print("\nMONTHLY RECAP")
    print("Month           :", bulan, "-", tahun)
    print("Total Income    :", total_pemasukan)
    print("Total Outcome   :", total_pengeluaran)
    print("Sisa Saldo      :", saldo)

    return total_pemasukan, total_pengeluaran

def input_user_month():
    bulan = input("Masukkan Bulan (mm): ")
    tahun = input("Masukkan Tahun (yyyy): ")
    return bulan, tahun

if __name__ == "__main__":
    # Meminta input dari pengguna untuk tanggal harian
    tanggal = input_user_day()
    
    # Memperbarui saldo harian dan mendapatkan total pemasukan dan pengeluaran
    total_pemasukan, total_pengeluaran = update_saldo_harian(tanggal)

    # Meminta input dari pengguna untuk rentang mingguan
    tgl_awal, tgl_akhir = input_user_week()
    
    # Memperbarui saldo mingguan dan mendapatkan total pemasukan dan pengeluaran
    total_pemasukan, total_pengeluaran = update_saldo_mingguan(tgl_awal, tgl_akhir)

    # Meminta input dari pengguna untuk bulan dan tahun
    bulan, tahun = input_user_month()
    
    # Memperbarui saldo bulanan dan mendapatkan total pemasukan dan pengeluaran
    total_pemasukan, total_pengeluaran = update_saldo_bulanan(bulan, tahun)
