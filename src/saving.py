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
        with open("data/history_savings.txt", "r") as log_file:
            for line in log_file:
                data = line.strip().split("|")
                if len(data) == 2:
                    jenis, jumlah = data
                    print(f"Jumlah: {jumlah}, Jenis: {jenis}")
                else:
                    print("(!) Format log tidak valid:", line.strip())
    except FileNotFoundError:
        print("Error: File history_savings.txt tidak ditemukan")

#menu tabungan
def menu():
    while True:
        print("[ Savings ]")
        print("| 1. Add Savings Balance")
        print("| 2. Subtract Savings Balance")
        print("| 3. History Savings Balance")
        print("| 4. Back")
        pilihan = input("Choose: ")

        if pilihan == "1":
            jumlah = float(input("[ Add Savings Balance ] Amount\t: "))
            addSaving(jumlah)
            updatesaving()
            print("")
        elif pilihan == "2":
            jumlah = float(input("[ Subtract Savings Balance ] Amount\t: "))
            subSaving(jumlah)
            updatesaving()
            print("")
        elif pilihan == "3":
            print("\n[ History Savings Balance ]")
            tampilHistory()
            print("")
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

menu()
