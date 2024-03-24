'''
    [🐺🐺🐺]
    Edit. Nieto Salim Maula | 231524019
    a5.d4.polban.proyek1

    Notes:
    24/03/2024 : 06.00 WIB ["nieto : buat file shape.py untuk content"]
    24/03/2024 : 07.00 WIB ["nieto : oop edited"]
'''

#________________getEksternal
import os
from datetime import datetime

def headerLogin():
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

def getParameter():
    with open("data/nowLogin.txt", "r") as file:
        username = file.readline().strip()

    # Read balance from wallet.txt
    with open("data/wallet.txt", "r") as file:
        balance = file.readline().strip()

    return username, balance

def getParameterSav():
    with open("data/nowLogin.txt", "r") as file:
        usernameSav = file.readline().strip()

    # Read balance from wallet.txt
    with open("data/savings.txt", "r") as file:
        balanceSav = file.readline().strip()

    return usernameSav, balanceSav

def printHeader():
    print("\033[94m" + "+-----------------------------------------------------------------------------------+")
    print("\033[94m" + "|    ________     ______  ___      ___   _______   _______ ___________ ______       |")
    print("\033[94m" + "|    |\"      \"\\   /    \" \\|\"  \\    /\"  | |   __ \"\\ /\"     \"(\"     _   \"/    \" \\     |")
    print("\033[94m" + "|    (.  ___  :) // ____  \\\\   \\  //   | (. |__) :(: ______))__/  \\\\__// ____  \\    |")
    print("\033[94m" + "|    |: \\   ) ||/  /    ) :/\\\\  \\/\\.    | |:  ____/ \\/    |     \\\\_ / /  /    ) )   |")
    print("\033[94m" + "|    (| (___\\ |(: (____/ /|: \\.        | (|  /     // ___)_    |.  |(: (____/ //    |")
    print("\033[94m" + "|    |:       :)\        /|.  \\    /:  |/|__/ \\   (:      \"|   \\:  | \\         \\    |")
    print("\033[94m" + "|    (________/  \\\"_____/ |___|\\__/|___(_______)   \\_______)    \\__|  \"____/\\__\\    |")
    print("\033[94m" + "|                                                                                   |")
    print("\033[94m" + "|    Strategize, Organize, and Thrive: Your Financial Companion @a5polbanjtk        |")
    print("\033[94m" + "|                                                                                   |")
    print("\033[94m" + "+-----------------------------------------------------------------------------------+")

def headerWallet():
    username, balance = getParameter()  # Panggil fungsi getParameter() untuk mendapatkan username dan balance
    os.system("cls")
    printHeader()
    print("\033[94m" + "| Hi,  {:<10s}  | Wallet Balance : {:<10s} |  {:<30s}  |".format(username, balance, datetime.now().strftime('%A, %d %B %Y %I:%M %p')))
    print("\033[94m" + "+-----------------------------------------------------------------------------------+")

def headerSavings():
    usernameSav, balanceSav = getParameterSav()  # Panggil fungsi getParameter() untuk mendapatkan username dan balance
    os.system("cls")
    printHeader()
    print("\033[94m" + "| Hi,  {:<10s}  | Savings Balance : {:<10s} |  {:<30s}  |".format(usernameSav, balanceSav, datetime.now().strftime('%A, %d %B %Y %I:%M %p')))
    print("\033[94m" + "+-----------------------------------------------------------------------------------+")

def mainMenu():
    print("|                                                                                   |")
    print("|                            [1] Add Transaction                                    |")
    print("|                            [2] History                                            |")
    print("|                            [3] Recapitulation                                     |")
    print("|                            [4] Savings                                            |")
    print("|                            [5] Show Diagrams                                      |")
    print("|                            [6] My Rating                                          |")
    print("|                            [0] Exit and SignOut                                   |")
    print("|                                                                                   |")
    print("+-----------------------------------------------------------------------------------+")

def menuTransaction():
    print("| [1] Income                                                                        |")
    print("| [2] Outcome                                                                       |")
    print("| [0] Back                                                                          |")
    print("+-----------------------------------------------------------------------------------+")

def menuHistory():
    print("| [1] by Log                                                                        |")
    print("| [2] by Categories                                                                 |")
    print("| [3] by Transaction type                                                           |")
    print("| [0] Back                                                                          |")
    print("+-----------------------------------------------------------------------------------+")

def menuRecap():
    print("| [1] Day                                                                           |")
    print("| [2] Week                                                                          |")
    print("| [3] Month                                                                         |")
    print("| [0] Back                                                                          |")
    print("+-----------------------------------------------------------------------------------+")

def menuDiagram():
    print("| [1] [Bar Chart] Transaction Frequency                                             |")
    print("| [2] [Bar Chart] Transaction type Frequency                                        |")
    print("| [0] Back                                                                          |")
    print("+-----------------------------------------------------------------------------------+")

def contentLevelA():
    print("| (*) Anda telah menunjukkan keahlian dalam mengelola keuangan Anda dengan baik.    |")
    print("|     Anda memiliki kontrol yang kuat atas pemasukan dan pengeluaran Anda, yang     |")
    print("|     memungkinkan Anda untuk memiliki surplus finansial secara konsisten.          |")
    print("| (*) Anda termasuk dalam kelompok orang yang sangat bijaksana dalam pengelolaan    |")
    print("|     keuangan pribadi.                                                             |")
    print("| (*) Dengan stabilitas keuangan yang Anda miliki, Anda memiliki kesempatan untuk   |")
    print("|     mencapai banyak hal. Anda bisa mempertimbangkan investasi jangka panjang,     |")
    print("|     merencanakan liburan impian, atau bahkan memulai bisnis baru.                 |")
    print("| (*) Teruslah memantau keuangan Anda meskipun dalam keadaan stabil. Pertimbangkan  |")
    print("|     untuk melakukan diversifikasi investasi untuk meningkatkan keamanan finansial |")
    print("|     Anda di masa depan.                                                           |")
    print("|                                                                                   |")
    print("| (!) \"Kekayaan bukanlah tentang berapa banyak yang Anda miliki, tetapi tentang     |")
    print("|     bagaimana Anda mengelolanya.\" - Andrew Carnegie                               |")

def contentLevelB():
    print("| (*) Anda telah menunjukkan disiplin yang baik dalam mengelola keuangan Anda,      |")
    print("|     meskipun ada sedikit ruang untuk perbaikan. Meskipun demikian, Anda secara    |")
    print("|     umum memiliki kontrol yang baik atas keuangan Anda.                           |")
    print("| (*) Anda termasuk dalam kelompok orang yang cermat dalam mengatur keuangan        |")
    print("|     pribadi mereka.                                                               |")
    print("| (*) Dengan sedikit penyesuaian, Anda dapat meningkatkan keamanan finansial Anda   |")
    print("|     lebih lanjut. Anda mungkin perlu mempertimbangkan tabungan atau investasi     |")
    print("|     tambahan untuk mengoptimalkan potensi keuangan Anda.                          |")
    print("| (*) Teruslah memantau dan evaluasi keuangan Anda secara teratur. Perhatikan       |")
    print("|     pola pengeluaran Anda dan pastikan untuk mengalokasikan dana untuk tabungan   |")
    print("|     darurat dan kebutuhan masa depan.                                             |")
    print("|                                                                                   |")
    print("| (!) \"Orang bijaksana membangun kebahagiaan mereka sendiri dengan melepaskan       |")
    print("|     beban hutang, dan menciptakan kehidupan yang sederhana dan memadai untuk      |")
    print("|     diri mereka sendiri.\" - Confucius                                             |")

def contentLevelC():
    print("| (*) Anda mungkin menghadapi beberapa tantangan dalam mengelola keuangan Anda,     |")
    print("|     tetapi Anda masih memiliki kesempatan untuk memperbaikinya. Penting untuk     |")
    print("|     mengidentifikasi area di mana Anda bisa mengurangi pengeluaran atau           |")
    print("|     meningkatkan pemasukan.                                                       |")
    print("| (*) Anda termasuk dalam kelompok orang yang perlu sedikit bantuan dalam mengatur  |")
    print("|     keuangan pribadi mereka.                                                      |")
    print("| (*) Dengan perencanaan dan disiplin yang tepat, Anda masih dapat mencapai banyak  |")
    print("|     hal. Fokuslah pada membangun kebiasaan pengelolaan keuangan yang sehat dan    |")
    print("|     memprioritaskan tujuan keuangan jangka panjang.                               |")
    print("| (*) Buatlah anggaran yang realistis dan ikuti dengan disiplin. Jangan ragu        |")
    print("|     untuk mencari saran dari profesional keuangan jika Anda memerlukan bantuan    |")
    print("|     dalam merencanakan keuangan Anda.                                             |")
    print("|                                                                                   |")
    print("| (!) \"Kemiskinan bukanlah keadaan alamiah. Manusia membuat kemiskinan dan karena   |")
    print("|     itu bisa diatasi dan dihilangkan.\" - Nelson Mandela                          |")

def contentLevelD():
    print("| (*) Anda mungkin menghadapi tantangan yang signifikan dalam mengelola keuangan    |")
    print("|     Anda, tetapi jangan putus asa. Ada langkah-langkah yang dapat Anda ambil      |")
    print("|     untuk memperbaiki situasi keuangan Anda.                                      |")
    print("| (*) Anda termasuk dalam kelompok orang yang memerlukan bantuan mendesak dalam     |")
    print("|     mengatur keuangan pribadi mereka.                                             |")
    print("| (*) Meskipun situasi Anda mungkin sulit saat ini, tetapi dengan upaya dan fokus   |")
    print("|     yang tepat, Anda masih dapat meraih stabilitas keuangan dan mencapai tujuan   |")
    print("|     Anda.                                                                         |")
    print("| (*) Mulailah dengan membuat anggaran yang jelas dan berkomitmen untuk mengikutinya|")
    print("|     mengikutinya Segera cari bantuan dari ahli keuangan atau konselor keuangan    |")
    print("|     untuk membantu Anda merencanakan strategi pemulihan keuangan yang efektif.    |")
    print("| (*) Jangan ragu untuk meminta dukungan dari keluarga dan teman-teman Anda dalam   |")
    print("|     perjalanan ini.                                                               |")
    print("|                                                                                   |")
    print("| (!) \"Kemiskinan adalah keadaan sementara, tidak pernah keadaan alamiah.\"          |") 
    print("|     - Muhammad Yunus                                                              |")