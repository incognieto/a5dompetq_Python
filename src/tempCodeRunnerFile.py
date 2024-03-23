import os
import curses
import menu

# Fungsi untuk membersihkan isi file nowLogin.txt
def clearNowLogin():
    with open("data/nowLogin.txt", "w"):
        pass

# Fungsi untuk menambahkan username ke dalam file nowLogin.txt
def addToNowLogin(username):
    with open("data/nowLogin.txt", "a") as file:
        file.write(username + "\n")

def printHeader_a(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "+----------------------------------------------------------+")
    stdscr.addstr(1, 0, "|							   |")
    stdscr.addstr(2, 0, "|							   |")
    stdscr.addstr(3, 0, "|							   |")
    stdscr.addstr(4, 0, "|	     _                            _   _____ 	   |")
    stdscr.addstr(5, 0, "|	    | |                          | | |  _  |	   |")
    stdscr.addstr(6, 0, "|	  __| | ___  _ __ ___  _ __   ___| |_| | | |	   |")
    stdscr.addstr(7, 0, "|	 / _` |/ _ \| '_ ` _ \| '_ \ / _ \ __| | | |	   |")
    stdscr.addstr(8, 0, "|	| (_| | (_) | | | | | | |_) |  __/ |_\\ \/ /	   |")
    stdscr.addstr(9, 0, "|	 \__,_|\___/|_| |_| |_| .__/ \___|\__|\_/\\_\	   |")
    stdscr.addstr(10, 0, "|	                      | |                   	   |")
    stdscr.addstr(11, 0, "|	                      |_|                   	   |")
    stdscr.addstr(12, 0, "|							   |")
    stdscr.refresh()

def printMenu_a(stdscr, selectedIndex):
    stdscr.addstr(13, 0, "|	[%s] Login\t [%s] Register\t     [%s] Exit\t   |" % ("X" if selectedIndex == 1 else " ", "X" if selectedIndex == 2 else " ", "X" if selectedIndex == 3 else " "))
    stdscr.addstr(14, 0, "|							   |")
    stdscr.addstr(15, 0, "|							   |")
    stdscr.addstr(16, 0, "+----------------------------------------------------------+")
    stdscr.refresh()

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

# Fungsi untuk melakukan login pengguna
def loginUser(stdscr):
    curses.echo()
    stdscr.addstr(17, 0, "Login | Username: ")
    stdscr.refresh()
    username = stdscr.getstr(18, 0).decode(encoding="utf-8")
    stdscr.addstr(19, 0, "Login | Password: ")
    stdscr.refresh()
    password = stdscr.getstr(20, 0).decode(encoding="utf-8")
    if not isUserExist(username):
        stdscr.addstr(21, 0, "User tidak ditemukan, segera lakukan registrasi.")
        stdscr.refresh()
        stdscr.getch()
        return
    with open("data/users.txt", "r") as file:
        for line in file:
            temp_username, temp_password = line.split()
            if username == temp_username and password == temp_password:
                stdscr.addstr(21, 0, "Login berhasil.")
                stdscr.refresh()
                stdscr.getch()
                writeNowLogin(username)
                menu.main()  # Panggil fungsi main dari menu.py
                return
    stdscr.addstr(21, 0, "Username atau password salah.")
    stdscr.refresh()
    stdscr.getch()
    os.remove("data/nowLogin.txt")

# Fungsi untuk logout, membersihkan nowLogin.txt
def logoutUser():
    clearNowLogin()
    print("Logout berhasil.")

def tampilHome(username):
    pass  # Fungsi ini dapat diimplementasikan sesuai kebutuhan

# Fungsi untuk menampilkan login
def tampilLogin(stdscr):
    selectedIndex = 1  # Pilihan menu awal
    while True:
        printHeader_a(stdscr)
        printMenu_a(stdscr, selectedIndex)
        key = stdscr.getch()

        if key == curses.KEY_UP:
            selectedIndex = (selectedIndex - 2 + 3) % 3 + 1
        elif key == curses.KEY_DOWN:
            selectedIndex = (selectedIndex % 3) + 1
        elif key == curses.KEY_LEFT:
            selectedIndex = (selectedIndex - 2 + 3) % 3 + 1
        elif key == curses.KEY_RIGHT:
            selectedIndex = (selectedIndex % 3) + 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if selectedIndex == 1:
                loginUser(stdscr)
            elif selectedIndex == 2:
                registerUser(stdscr)  # Meneruskan stdscr ke registerUser()
            elif selectedIndex == 3:
                logoutUser()  # Logout sebelum keluar program
                stdscr.addstr(22, 0, "Good bye ...")
                stdscr.refresh()
                stdscr.getch()
                break

# Fungsi untuk melakukan registrasi pengguna
def registerUser(stdscr):  # Menambahkan stdscr sebagai parameter
    curses.echo()
    stdscr.addstr(17, 0, "Register | Username: ")
    stdscr.refresh()
    username = stdscr.getstr(18, 0).decode(encoding="utf-8")
    if isUserExist(username):
        stdscr.addstr(19, 0, "Registrasi Gagal. Username telah digunakan.")
        stdscr.refresh()
        stdscr.getch()
        return
    stdscr.addstr(19, 0, "Register | Password: ")
    stdscr.refresh()
    password = stdscr.getstr(20, 0).decode(encoding="utf-8")
    with open("data/users.txt", "a") as file:
        file.write(username + " " + password + "\n")
    stdscr.addstr(21, 0, "Registrasi berhasil.")
    stdscr.refresh()
    stdscr.getch()

# Fungsi utama untuk menjalankan aplikasi login
def main(stdscr):
    curses.curs_set(0)  # Sembunyikan kursor
    tampilLogin(stdscr)  # Berikan stdscr ke tampilLogin()

#Testing Main
if __name__ == "__main__":
    curses.wrapper(main)


