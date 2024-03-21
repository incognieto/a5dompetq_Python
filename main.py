from lib import curses
from src import login

def main(stdscr):
    curses.curs_set(0)  # Sembunyikan kursor
    login.main(stdscr)  # Jalankan fungsi main dari login

if __name__ == "__main__":
    curses.wrapper(main)
