#import datetime

#struct??
class Saldo:
    def __init__(self):
        self.gaji = 0
        self.bonus = 0
        self.sampingan = 0
        self.pinjaman = 0
        self.uangKaget = 0
        self.inAll = 0
        self.outAll = 0
        self.tanggal = ""

#pengeluaran/outcome
def Outcome(saldo, jum, kategori, tgl):
    if saldo.inAll < jum:
        print("Saldo tidak cukup! Silakan isi pemasukan terlebih dahulu.")
    else:
        saldo.outAll += jum
        print(f"\nRiwayat pada {tgl}")
        print(f"Pengeluaran untuk {kategori}: Rp{jum}")
        saldo.inAll -= jum
        print(f"Sisa saldo: Rp{saldo.inAll}")

#operasi catat ke file
def catat_pemasukan(saldo, jenis):
    with open("pemasukan_transaksi.txt", "a") as pemasukan_file:
        pemasukan_file.write(f"pemasukan|{saldo.inAll:.2f}|{jenis}|{saldo.tanggal}\n")

def catat_pengeluaran(saldo, jumlah, kategori):
    with open("pengeluaran_transaksi.txt", "a") as pengeluaran_file:
        pengeluaran_file.write(f"pengeluaran|{jumlah:.2f}|{kategori}|{saldo.tanggal}\n")

def catat_transaksi(saldo, jenis, jumlah, kategori=None):
    with open("history.txt", "a") as transaksi_file:
        if jenis == 'pemasukan':
            transaksi_file.write(f"{jenis}|{jumlah:.2f}|{kategori}|{saldo.tanggal}\n")
        elif jenis == 'pengeluaran':
            transaksi_file.write(f"{jenis}|{jumlah:.2f}|{kategori}|{saldo.tanggal}\n")

#menu ketika ingin transaksi
def menuTransaksi():
    saldo = Saldo()
    
    while True:
        print("\n[ Transaksi ]")
        print("| 1. Pemasukan")
        print("| 2. Pengeluaran")
        print("| 3. Kembali")
        pilih = int(input("Masukkan Pilihan: "))
        
        if pilih == 1:  #Pemasukan
            saldo.tanggal = input("\nMasukkan tangal (DD-MM-YYYY): ")
            print("\n[ Jenis Pemasukan ]")
            print("| 1. Gaji")
            print("| 2. Bonus")
            print("| 3. Sampingan")
            print("| 4. Pinjaman")
            print("| 5. Uang Kaget")
            pilJenis = int(input("Masukkan Pilihan: "))
            
            if pilJenis in range(1, 6):
                jml = int(input(f"\nMasukkan jumlah uang: Rp"))
                if pilJenis == 1:
                    saldo.gaji += jml
                    kategori = "Gaji"
                elif pilJenis == 2:
                    saldo.bonus += jml
                    kategori = "Bonus"
                elif pilJenis == 3:
                    saldo.sampingan += jml
                    kategori = "Sampingan"
                elif pilJenis == 4:
                    saldo.pinjaman += jml
                    kategori = "Pinjaman"
                elif pilJenis == 5:
                    saldo.uangKaget += jml
                    kategori = "Uang Kaget"
                
                saldo.inAll += jml
                print(f"Pemasukan berhasil dicatat: Rp{jml}")
                catat_pemasukan(saldo, kategori)
                catat_transaksi(saldo, 'pemasukan', jml, kategori)
            else:
                print("Pilihan tidak valid!")
        
        elif pilih == 2:    #Pengeluaran
            saldo.tanggal = input("\nMasukkan tanggal (DD-MM-YYYY): ")
            print("\n[ Jenis Pengeluaran ]")
            print("| 1. Belanja")
            print("| 2. Hiburan")
            print("| 3. Investasi")
            print("| 4. Kesehatan")
            print("| 5. Transportasi")
            print("| 6. Makanan")
            print("| 7. Minuman")
            print("| 8. Pajak")
            print("| 9. Pakaian")
            print("| 10. Pendidikan")
            print("| 11. Hutang")
            print("| 12. Sedekah")
            pilJenis = int(input("Masukkan Pilihan: "))
            
            if pilJenis in range(1, 13):
                jml = int(input(f"\nMasukkan jumlah pengeluaran: Rp"))
                kategori = {
                    1: "Belanja", 2: "Hiburan", 3: "Investasi", 4: "Kesehatan", 5: "Transportasi",
                    6: "Makanan", 7: "Minuman", 8: "Pajak", 9: "Pakaian", 10: "Pendidikan",
                    11: "Hutang", 12: "Sedekah"
                }[pilJenis]
                Outcome(saldo, jml, kategori, saldo.tanggal)
                catat_pengeluaran(saldo, jml, kategori)
                catat_transaksi(saldo, 'pengeluaran', jml, kategori)
            else:
                print("Pilihan tidak valid!")
        
        elif pilih == 3:    #Kembali
            break
        
        else:
            print("Pilihan tidak valid!")

#if __name__ == "__menuTransaksi__":
menuTransaksi()