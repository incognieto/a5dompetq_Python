#membaca file tabungan
def bacasaving():
    try:
        with open("savings.txt", "r") as tabungan:
            content = tabungan.read()
            if content.strip():  # Cek apakah isi file tidak kosong
                saving = float(content)
                return saving
            else:
                print("File savings.txt kosong.")
                return 0.0  # Mengembalikan nilai 0 jika file kosong
    except FileNotFoundError:
        print("Error membuka file savings.txt")
        return -1.0

# Tampilkan sisa tabungan 
def printSisaSaving():
    saving = updatesaving()  # Memperbarui tabungan dan mendapatkan nilai yang diperbarui
    if saving is not None:  # Memeriksa apakah nilai tabungan berhasil diperbarui
        print(f"Sisa tabungan Anda adalah: {saving:.2f}")
    else:
        print("Gagal membaca sisa tabungan.")
    

# Perbarui tabungan dan tampilkan sisa tabungan yang diperbarui
def updatesaving():
    totTabungan = 0.0
    totPengeluaran = 0.0
    
    # Membaca dan menghitung pemasukan
    try:
        with open("addsavings.txt", "r") as addTabungan:
            for line in addTabungan:
                if line.strip():  # Pemeriksaan untuk baris tidak kosong
                    parts = line.strip().split("|")
                    if len(parts) == 2 and parts[0] == "incomeSaving":
                        jum = float(parts[1])
                        totTabungan += jum
    except FileNotFoundError:
        print("Error membuka file addsavings.txt")
    
    # Membaca dan menghitung pengeluaran
    try:
        with open("subsavings.txt", "r") as outTabungan:
            for line in outTabungan:
                if line.strip():  # Pemeriksaan untuk baris tidak kosong
                    parts = line.strip().split("|")
                    if len(parts) == 2 and parts[0] == "outcomeSaving":
                        jum = float(parts[1])
                        totPengeluaran += jum
    except FileNotFoundError:
        print("Error membuka file subsavings.txt")
    
    # Hitung sisa tabungan
    saving = totTabungan - totPengeluaran
    
    # Simpan ke savings.txt
    try:
        with open("savings.txt", "w") as tabungan:
            tabungan.write(f"{saving:.2f}")
            print ("saving berhasil diupdate pada file savings.txt")
            
            # Kembalikan sisa tabungan yang diperbarui
            return saving
    except FileNotFoundError:
        print("Error membuka file savings.txt")
        return None  # Jika terjadi kesalahan, kembalikan None  
    
#tulis ke file
def writeSavings(nmFile, tipe, jum):
    try:
        with open(nmFile, "a") as file:
            file.write(f"{tipe}|{jum:.2f}\n")
            with open("history_savings.txt", "a") as history:
                history.write(f"{tipe}|{jum:.2f}\n")
    except FileNotFoundError:
        print(f"Error opening file {nmFile}")

#tampil
def displaySavingsHistory():
    try:
        with open("history_savings.txt", "r") as logfile:
            for line in logfile:
                parts = line.strip().split("|")
                if len(parts) == 2:
                    print(f"Jumlah: {float(parts[1]):.2f}, Jenis: {parts[0]}")
                else:
                    print("(!) Format log tidak valid: ", line)
    except FileNotFoundError:
        print("(!) Gagal membuka file history_savings.txt")

#menu pilihan saving
def printMenuSavings():
    while True:

        printSisaSaving()

        print("[ Savings ]")
        print("| 1. Add Savings Balance")
        print("| 2. Subtract Savings Balance")
        print("| 3. History Savings Balance")
        print("| 4. Back")
        pilih = int(input("Choose: "))
        
        if pilih == 1:  #add
            incomeSaving = float(input("[ Add Savings Balance ] Amount\t: "))
            writeSavings("addsavings.txt", "incomeSaving", incomeSaving)
            updatesaving()
            
        elif pilih == 2:    #sub
            outcomeSaving = float(input("[ Subtract Savings Balance ] Amount\t: "))
            writeSavings("subsavings.txt", "outcomeSaving", outcomeSaving)
            updatesaving()
            
        elif pilih == 3:    #history
            print("[ History Savings Balance ]\n")
            displaySavingsHistory()
            
        elif pilih == 4:    #back
            break
        
        else:
            print("Pilihan tidak valid!")

printMenuSavings()
