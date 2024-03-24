'''
    [🐺🐺🐺]
    Edit. Nieto Salim Maula | 231524019
    a5.d4.polban.proyek1

    Notes:
    23/03/2024 : 21.00 WIB ["nito : make a diagram"]
'''

import turtle

def draw_bar(label, height, color):
    """
    Fungsi untuk menggambar batang diagram.
    """
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(height)
    turtle.write(f"{label}: {height}", align="center", font=("Arial", 12, "normal"))
    turtle.right(90)
    turtle.forward(30)  # Jarak antara bar
    turtle.right(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()
    turtle.forward(10)  # Jarak antara bar

def main():
    # Membaca data dari file history.txt
    with open('data/history.txt', 'r') as file:
        lines = file.readlines()

    # Membuat dictionary untuk menyimpan jumlah uang untuk setiap jenis transaksi
    transactions = {'pemasukan': 0, 'pengeluaran': 0}

    # Proses data
    for line in lines:
        data = line.strip().split('|')
        jenis_transaksi = data[0]
        jumlah_uang = float(data[1])
        if jenis_transaksi in transactions:
            transactions[jenis_transaksi] += jumlah_uang

    # Set up turtle
    turtle.title("Frekuensi Transaksi by DompetQ")
    turtle.setup(300, 600)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-25, -250)
    turtle.pendown()

    # Menggambar diagram batang
    max_value = max(transactions.values())
    scale_factor = 400 / max_value  # Faktor skala untuk menggambar batang
    for jenis_transaksi, jumlah_uang in transactions.items():
        scaled_height = jumlah_uang * scale_factor
        if jenis_transaksi == 'pemasukan':
            draw_bar(jenis_transaksi, scaled_height, 'blue')
        else:
            draw_bar(jenis_transaksi, scaled_height, 'red')

    # Menutup jendela saat di-klik
    turtle.hideturtle()
    turtle.exitonclick()

if __name__ == "__main__":
    main()
