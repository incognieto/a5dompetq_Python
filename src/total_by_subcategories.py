def total_savings():
    in_savings = 0
    out_savings = 0
    
    with open('data/addsavings.txt', 'r') as file:
        for line in file:
            incomeSaving, jumlah = line.strip().split('|')
            jumlah = float(jumlah)
            if incomeSaving == "incomeSaving":
                in_savings += jumlah
                
    with open('data/subsavings.txt', 'r') as file:
        for line in file:
            outcomeSaving, jumlah = line.strip().split('|')
            jumlah = float(jumlah)
            if outcomeSaving == "outcomeSaving":
                out_savings += jumlah
                
    return in_savings, out_savings

def cetak_savings():
    in_savings, out_savings = total_savings()
    total_saving = in_savings - out_savings
    
    with open('data/savings.txt', 'w') as file:
        file.write(f"{total_saving}")
        
def total_wallets():
    in_wallet = 0
    out_wallet = 0
    
    with open('data/pemasukan_transaksi.txt', 'r') as file:
        for line in file:
            pemasukan, jumlah, sub_kategori, tanggal = line.strip().split('|')
            jumlah = float(jumlah)
            if pemasukan == "pemasukan":
                in_wallet += jumlah
                
    with open('data/pengeluaran_transaksi.txt', 'r') as file:
        for line in file:
            pengeluaran, jumlah, sub_kategori, tanggal = line.strip().split('|')
            jumlah = float(jumlah)
            if pengeluaran == "pengeluaran":
                out_wallet += jumlah
                
    return in_wallet, out_wallet

def cetak_wallet():
    in_wallet, out_wallet = total_wallets()
    total_wallet = in_wallet - out_wallet
    
    with open('data/wallet.txt', 'w') as file:
        file.write(f"{total_wallet}")
        
cetak_savings()
cetak_wallet()    
                