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

def tampilan_savings():
    income_all, outcome_all = savings_overall()
    print(f"Saving In : {income_all}")
    print(f"Saving Out : {outcome_all}")

def tambah_transaksi(kategori, jumlah, sub_kategori, tanggal):
    if kategori == "pemasukan":
        with open('data/pemasukan_transaksi.txt', 'a') as file:
            file.write(f"{kategori}|{jumlah}|{sub_kategori}|{tanggal}\n")
    if kategori == 'pengeluaran':
        with open('data/pengeluaran_transaksi.txt', 'a') as file:
            file.write(f"{kategori}|{jumlah}|{sub_kategori}|{tanggal}\n")

def hitung_total():
    total_pemasukan = 0
    total_pengeluaran = 0
    
    with open('data/pemasukan_transaksi.txt', 'r') as file:
        for line in file:
            kategori, jumlah, sub_kategori, tanggal = line.strip().split('|')
            jumlah = float(jumlah)
            
            if kategori == 'pemasukan':
                total_pemasukan += jumlah
                
    with open('data/pengeluaran_transaksi.txt', 'r') as file:
        for line in file:
            kategori, jumlah, sub_kategori, tanggal = line.strip().split('|')
            jumlah = float(jumlah)
            
            if kategori == 'pengeluaran':
                total_pengeluaran += jumlah
                
    return total_pemasukan, total_pengeluaran

def tampilkan_total():
    total_pemasukan, total_pengeluaran = hitung_total()
    print(f"Total Pemasukan: {total_pemasukan}")
    print(f"Total Pengeluaran: {total_pengeluaran}")

tambah_transaksi('pemasukan', 5000000, 'gaji', '01-12-2006')
tambah_transaksi('pengeluaran', 500000, 'makan', '23-12-2006')
tambah_transaksi('pemasukan', 250000, 'Bonus', '15-12-2006')
tambah_transaksi('pengeluaran', 125000, 'Transportasi', '12-12-2006')

tampilkan_total()
tampilan_savings()