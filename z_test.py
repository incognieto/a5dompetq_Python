import time
import os

def confirmAction(readmeText):
    """
    Meminta konfirmasi user

    Author
    ------
    Farras Ahmad Rasyid - 231524006 - @bamoebin

    parameter : teks pesan konfirmasi

    output : boolean
    """
    while True:
        choice = input(f"{readmeText} (y/n): ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Pilihan tidak valid, coba lagi.")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")

def main():
    readmeText = "Apakah Anda yakin ingin melanjutkan?"
    if confirmAction(readmeText):
        print("Anda memilih 'yes'.")
    else:
        print("Anda memilih 'no'.")

if __name__ == "__main__":
    main()
