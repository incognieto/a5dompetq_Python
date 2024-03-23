def total_savings():
    in_saving = 0
    out_saving = 0
    
    with open('data/history_savings.txt', 'r') as file:
        for line in file:
            jenis_savings, jumlah = line.strip().split('|')
            jumlah = float(jumlah)
            
            if jenis_savings == "incomeSaving":
                in_saving += jumlah
                
            elif jenis_savings == "outcomeSaving":
                out_saving += jumlah
                
    return in_saving, out_saving

def cetak_savings():
    in_saving, out_saving = total_savings()
    total_saving = in_saving - out_saving
    
    with open('data/savings.txt', 'w') as file:
        file.write(f"{total_saving}")

def total_wallets():
    in_wallet = 0
    out_wallet = 0
    
    with open('data/history.txt', 'r') as file:
        for line in file:
            jenis, jumlah, sub_kategori, tanggal = line.strip().split('|')
            jumlah = float(jumlah)
            
            if jenis == "pemasukan":
                in_wallet += jumlah
                
            elif jenis == "pengeluaran":
                out_wallet += jumlah
                
    return in_wallet, out_wallet

def cetak_wallet():
    in_wallet, out_wallet = total_wallets()
    total_wallet = in_wallet - out_wallet
    
    with open('data/wallet.txt', 'w') as file:
        file.write(f"{total_wallet}")
        
cetak_savings()
cetak_wallet() 
