'''
    [🐺🐺🐺]
    Edit. Nieto Salim Maula | 231524019
    a5.d4.polban.proyek1

    Notes:
    23/03/2024 : 21.00 WIB ["nito : make a diagram"]
'''

import turtle

def main():
    # Membaca data dari file history.txt
    with open('data/history.txt', 'r') as file:
        lines = file.readlines()

    # Membuat dictionary untuk menyimpan frekuensi transaksi
    frekuensi_transaksi = {'Gaji': 0, 'Bonus': 0, 'Sampingan': 0, 'Pinjaman': 0, 'Uang Kaget': 0, 'Belanja': 0,
                           'Hiburan': 0, 'Investasi': 0, 'Kesehatan': 0, 'Transportasi': 0, 'Makanan': 0,
                           'Minuman': 0, 'Pajak': 0, 'Pakaian': 0, 'Pendidikan': 0, 'Hutang': 0, 'Sedekah': 0}

    # Menghitung frekuensi transaksi
    for line in lines:
        _, _, kategori, _ = line.strip().split('|')
        if kategori in frekuensi_transaksi:
            frekuensi_transaksi[kategori] += 1
        else:
            frekuensi_transaksi[kategori] = 1

    # Set up turtle
    turtle.title("Frekuensi Banyak Transaksi")
    turtle.setup(1400, 400)
    turtle.speed(0)

    # Menggambar diagram batang
    colors = ['blue', 'green', 'brown', 'black']
    other_color = ['orange', 'cyan', 'pink', 'purple', 'yellow', 'magenta', 'teal', 'lime', 'olive', 'maroon',
                   'navy', 'indigo', 'gold', 'coral', 'salmon', 'silver', 'tan']
    start_x = -670
    start_y = -100
    bar_width = 40
    max_height = max(frekuensi_transaksi.values())

    # Memulai menggambar setiap batang
    for kategori, jumlah in frekuensi_transaksi.items():
        # Menentukan warna
        if kategori in ['Gaji', 'Bonus', 'Sampingan', 'Pinjaman']:
            color = colors.pop(0)
        else:
            color = other_color.pop(0)

        # Menggambar batang
        height = jumlah / max_height * 200
        turtle.penup()
        turtle.goto(start_x, start_y)
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(bar_width)
            turtle.left(90)
            turtle.forward(height)
            turtle.left(90)
        turtle.end_fill()
        # Menulis label kategori
        turtle.penup()
        turtle.goto(start_x + bar_width / 2, start_y - 20)
        turtle.write(kategori, align="center", font=("Arial", 10, "normal"))
        # Update posisi untuk batang berikutnya
        start_x += bar_width * 2

    # Menutup jendela saat di-klik
    turtle.hideturtle()
    turtle.exitonclick()

if __name__ == "__main__":
    main()