'''
    [🐸🐸🐸]
    Edit. Muhammad Aslim Salman | 231524019
    a5.d4.polban.proyek1

    Notes:
    22/03/2024 : 16.00 WIB ["aslim : update branch nya"]
    23/03/2024 : 10.36 WIB ["nito : edit to modular"]
'''

def savings_overall():
    income_all = 0
    outcome_all = 0
    
    with open('data/history_savings.txt', 'r') as file:
        for line in file:
            savings_type, jumlah = line.strip().split('|')
            jumlah = float(jumlah)
            if savings_type == "incomeSaving":
                income_all += jumlah
            elif savings_type == "outcomeSaving":
                outcome_all += jumlah
                
    return income_all, outcome_all

def cetak_savings():
    income_all, outcome_all = savings_overall()
    savings_all = income_all - outcome_all
    
    with open('data/savings.txt', 'w') as file:
        file.write(f"{savings_all}")

'''
def tambah_transaksi(kategori, jumlah, sub_kategori, tanggal):
    if kategori == "pemasukan":
        with open('data/pemasukan_transaksi.txt', 'a') as file:
            file.write(f"{kategori}|{jumlah}|{sub_kategori}|{tanggal}\n")
    if kategori == 'pengeluaran':
        with open('data/pengeluaran_transaksi.txt', 'a') as file:
            file.write(f"{kategori}|{jumlah}|{sub_kategori}|{tanggal}\n")
'''

def hitung_total():
    total_pemasukan = 0
    total_pengeluaran = 0
    
    with open('data/pemasukan_transaksi.txt', 'r') as file:
        for line in file:
            try:
                kategori, jumlah, sub_kategori, tanggal = line.strip().split('|')
                jumlah = float(jumlah)
                
                if kategori == 'pemasukan':
                    total_pemasukan += jumlah
            except ValueError:
                print("Error: Invalid format in pemasukan_transaksi.txt. Skipping line:", line)
                
    with open('data/pengeluaran_transaksi.txt', 'r') as file:
        for line in file:
            try:
                kategori, jumlah, sub_kategori, tanggal = line.strip().split('|')
                jumlah = float(jumlah)
                
                if kategori == 'pengeluaran':
                    total_pengeluaran += jumlah
            except ValueError:
                print("Error: Invalid format in pengeluaran_transaksi.txt. Skipping line:", line)
                
    return total_pemasukan, total_pengeluaran

def cetak_wallet():
    total_pemasukan, total_pengeluaran = hitung_total()
    wallet_total = total_pemasukan - total_pengeluaran
    
    with open('data/wallet.txt', 'w') as file:
        file.write(f"{wallet_total}")

'''
tambah_transaksi('pemasukan', 5000000, 'Gaji', '01-12-2006')
tambah_transaksi('pengeluaran', 500000, 'Makan', '23-12-2006')
tambah_transaksi('pemasukan', 250000, 'Bonus', '15-12-2006')
tambah_transaksi('pengeluaran', 125000, 'Transportasi', '12-12-2006')
'''
cetak_wallet()
cetak_savings()