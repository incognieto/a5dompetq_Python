import os
import menu

# Fungsi untuk membersihkan isi file nowLogin.txt
def clearNowLogin():
    with open("data/nowLogin.txt", "w"):
        pass

# Fungsi untuk menambahkan
#  username ke dalam file nowLogin.txt
def addToNowLogin(username):
    with open("data/nowLogin.txt", "a") as file:
        file.write(username + "\n")

def printHeader_a():
    os.system("cls")
    print("+-----------------------------------------------------------------------------------+")
    print("|    ________     ______  ___      ___   _______   _______ ___________ ______       |")
    print("|    |\"      \"\\   /    \" \\|\"  \\    /\"  | |   __ \"\\ /\"     \"(\"     _   \"/    \" \\     |")
    print("|    (.  ___  :) // ____  \\\\   \\  //   | (. |__) :(: ______))__/  \\\\__// ____  \\    |")
    print("|    |: \\   ) ||/  /    ) :/\\\\  \\/\\.    | |:  ____/ \\/    |     \\\\_ / /  /    ) )   |")
    print("|    (| (___\\ |(: (____/ /|: \\.        | (|  /     // ___)_    |.  |(: (____/ //    |")
    print("|    |:       :)\        /|.  \\    /:  |/|__/ \\   (:      \"|   \\:  | \\         \\    |")
    print("|    (________/  \\\"_____/ |___|\\__/|___(_______)   \\_______)    \\__|  \"____/\\__\\    |")
    print("|                                                                                   |")
    print("|    Strategize, Organize, and Thrive: Your Financial Companion @a5polbanjtk        |")
    print("|                                                                                   |")
    print("|                                 [1] Login                                         |")
    print("|                                 [2] Register                                      |")
    print("|                                 [0] Exit                                          |")
    print("|                                                                                   |")
    print("+-----------------------------------------------------------------------------------+")

def loginUser():
    print("\n[Login] Username: ", end="")
    username = input().strip()
    print("[Login] Password: ", end="")
    password = input().strip()
    if not isUserExist(username):
        print("User tidak ditemukan, segera lakukan registrasi.")
        input()
        return None, None  # Mengembalikan None jika login gagal
    with open("data/users.txt", "r") as file:
        for line in file:
            temp_username, temp_password = line.split()
            if username == temp_username and password == temp_password:
                print("\n(!) Login successfull. Press ENTER to Mainmenu")
                input()
                writeNowLogin(username)
                # Baca saldo dari file wallet.txt
                with open("data/wallet.txt", "r") as wallet_file:
                    balance = wallet_file.readline().strip()
                return username, balance  # Mengembalikan username dan balance jika login berhasil
    print("Username atau password salah.")
    input()
    os.remove("data/nowLogin.txt")
    return None, None  # Mengembalikan None jika login gagal

def tampilLogin():
    while True:
        printHeader_a()
        key = input("[dompetQ] Input your option: ").strip()

        if key == "1":
            username, balance = loginUser()
            if username is not None:
                menu.printMenu_main()  # Memanggil menu utama jika login berhasil
        elif key == "2":
            registerUser()
        elif key == "0":
            print("Goodbye ...")
            break

def registerUser():
    print("\n[Register] Username: ", end="")
    username = input().strip()
    if isUserExist(username):
        print("Registrasi Gagal. Username telah digunakan.")
        input()
        return
    print("[Register] Password: ", end="")
    password = input().strip()
    with open("data/users.txt", "a") as file:
        file.write(username + " " + password + "\n")
    print("Registrasi berhasil.")
    input()

# Fungsi untuk memeriksa apakah pengguna sudah terdaftar saat login
def isUserExist(username):
    with open("data/users.txt", "r") as file:
        for line in file:
            user_data = line.split()
            if user_data[0] == username:
                return True
    return False

# Fungsi untuk menulis satu username ke dalam file nowLogin.txt
def writeNowLogin(username):
    with open("data/nowLogin.txt", "w") as file:
        file.write(username + "\n")

# Fungsi untuk membaca username dari file nowLogin.txt
def readNowLogin():
    try:
        with open("data/nowLogin.txt", "r") as file:
            username = file.readline().strip()
            return username
    except FileNotFoundError:
        return ""

# Fungsi untuk logout, membersihkan nowLogin.txt
def logoutUser():
    clearNowLogin()
    print("Logout berhasil.")

def main():
    tampilLogin()

if __name__ == "__main__":
    main()
