import os

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

def printsisa(saving):
    print(f"Sisa saving Anda adalah: {saving:.2f}")

def updatesaving():
    total_savings = 0.0
    total_pengeluaran = 0.0

    try:
        with open("data/addsavings.txt", "r") as pemasukan_savings:
            for line in pemasukan_savings:
                if line.startswith("incomeSaving|"):
                    amount = float(line.split("|")[1])
                    total_savings += amount
    except FileNotFoundError:
        print("Error: File addsavings.txt tidak ditemukan")

    try:
        with open("data/subsavings.txt", "r") as pengeluaran_savings:
            for line in pengeluaran_savings:
                if line.startswith("outcomeSaving|"):
                    amount = float(line.split("|")[1])
                    total_pengeluaran += amount
    except FileNotFoundError:
        print("Error: File subsavings.txt tidak ditemukan")

    saving = total_savings - total_pengeluaran

    try:
        with open("data/savings.txt", "w") as savings_file:
            savings_file.write(f"{saving:.2f}")
            print("saving berhasil diupdate pada file savings.txt")
            printsisa(saving)
    except FileNotFoundError:
        print("Error: File savings.txt tidak ditemukan")
    
    os.system('cls' if os.name == 'nt' else 'clear')
