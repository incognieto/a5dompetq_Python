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
    print("|" + "\033[94m" + "\033[1m" +  "     ________     ______  ___      ___   _______   _______ ___________ ______      "+ "\033[0m" +"|")
    print("|" + "\033[94m" + "\033[1m" +  "    |\"      \"\\   /    \" \\|\"  \\    /\"  | |   __ \"\\ /\"     \"(\"     _   \"/    \" \\     "+ "\033[0m" +"|")
    print("|" + "\033[94m" + "\033[1m" +  "    (.  ___  :) // ____  \\\\   \\  //   | (. |__) :(: ______))__/  \\\\__// ____  \\    "+ "\033[0m" +"|")
    print("|" + "\033[94m" + "\033[1m" +  "    |: \\   ) ||/  /    ) :/\\\\  \\/\\.    | |:  ____/ \\/    |     \\\\_ / /  /    ) )   "+ "\033[0m" +"|")
    print("|" + "\033[94m" + "\033[1m" +  "    (| (___\\ |(: (____/ /|: \\.        | (|  /     // ___)_    |.  |(: (____/ //    "+ "\033[0m" +"|")
    print("|" + "\033[94m" + "\033[1m" +  "    |:       :)\        /|.  \\    /:  |/|__/ \\   (:      \"|   \\:  | \\         \\    "+ "\033[0m" +"|")
    print("|" + "\033[94m" + "\033[1m" +  "    (________/  \\\"_____/ |___|\\__/|___(_______)   \\_______)    \\__|  \"____/\\__\\    "+ "\033[0m" +"|")
    print("|                                                                                   |")
    print("|" + "\033[94m" + "\033[1m" + "    Strategize, Organize, and Thrive: Your Financial Companion @a5polbanjtk        "+ "\033[0m" +"|")
    print("|                                                                                   |")
    print("|                                 " + "\033[1m" + "\033[96m" + "[1] Login                                         "+ "\033[0m" +"|")
    print("|                                 " + "\033[1m" + "\033[96m" + "[2] Register                                      "+ "\033[0m" +"|")
    print("|                                 " + "\033[1m" + "\033[96m" + "[0] Exit                                          "+ "\033[0m" +"|")
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
    print("+-----------------------------------------------------------------------------------+")
    print("|" + "\033[94m" + "\033[1m" +  "     ________     ______  ___      ___   _______   _______ ___________ ______      "+ "\033[0m" +"|")
    print("|" + "\033[94m" + "\033[1m" +  "    |\"      \"\\   /    \" \\|\"  \\    /\"  | |   __ \"\\ /\"     \"(\"     _   \"/    \" \\     "+ "\033[0m" +"|")
    print("|" + "\033[94m" + "\033[1m" +  "    (.  ___  :) // ____  \\\\   \\  //   | (. |__) :(: ______))__/  \\\\__// ____  \\    "+ "\033[0m" +"|")
    print("|" + "\033[94m" + "\033[1m" +  "    |: \\   ) ||/  /    ) :/\\\\  \\/\\.    | |:  ____/ \\/    |     \\\\_ / /  /    ) )   "+ "\033[0m" +"|")
    print("|" + "\033[94m" + "\033[1m" +  "    (| (___\\ |(: (____/ /|: \\.        | (|  /     // ___)_    |.  |(: (____/ //    "+ "\033[0m" +"|")
    print("|" + "\033[94m" + "\033[1m" +  "    |:       :)\        /|.  \\    /:  |/|__/ \\   (:      \"|   \\:  | \\         \\    "+ "\033[0m" +"|")
    print("|" + "\033[94m" + "\033[1m" +  "    (________/  \\\"_____/ |___|\\__/|___(_______)   \\_______)    \\__|  \"____/\\__\\    "+ "\033[0m" +"|")
    print("|                                                                                   |")
    print("|" + "\033[94m" + "\033[1m" + "    Strategize, Organize, and Thrive: Your Financial Companion @a5polbanjtk        "+ "\033[0m" +"|")
    print("|                                                                                   |")
    print("+-----------------------------------------------------------------------------------+")

def headerWallet():
    username, balance = getParameter()  # Panggil fungsi getParameter() untuk mendapatkan username dan balance
    os.system("cls")
    printHeader()
    print("| Hi," + "\033[92m" + "  {:<10s}  ".format(username) + "\033[0m" + "| Wallet Balance :" + "\033[92m" + " {:<10s} ".format(balance) + "\033[0m" + "|  " + "\033[92m" + "{:<30s}".format(datetime.now().strftime('%A, %d %B %Y %I:%M %p')) + "\033[0m" + "  |")
    print("+-----------------------------------------------------------------------------------+")

def headerSavings():
    usernameSav, balanceSav = getParameterSav()  # Panggil fungsi getParameter() untuk mendapatkan username dan balance
    os.system("cls")
    printHeader()
    print("| Hi," + "\033[92m" + "  {:<10s}  ".format(usernameSav) + "\033[0m" + "| Savings Balance :" + "\033[92m" + " {:<10s} ".format(balanceSav) + "\033[0m" + "| " + "\033[92m" + "{:<30s}".format(datetime.now().strftime('%A, %d %B %Y %I:%M %p')) + "\033[0m" + "  |")
    print("+-----------------------------------------------------------------------------------+")

def mainMenu():
    print("|                                                                                   |")
    print("|                            " + "\033[1m" + "\033[96m" + "[1] Add Transaction                                    " + "\033[0m" + "|")
    print("|                            " + "\033[1m" + "\033[96m" + "[2] History                                            " + "\033[0m" + "|")
    print("|                            " + "\033[1m" + "\033[96m" + "[3] Recapitulation                                     " + "\033[0m" + "|")
    print("|                            " + "\033[1m" + "\033[96m" + "[4] Savings                                            " + "\033[0m" + "|")
    print("|                            " + "\033[1m" + "\033[96m" + "[5] Show Diagrams                                      " + "\033[0m" + "|")
    print("|                            " + "\033[1m" + "\033[96m" + "[6] My Rating                                          " + "\033[0m" + "|")
    print("|                            " + "\033[1m" + "\033[96m" + "[0] Exit and SignOut                                   " + "\033[0m" + "|")
    print("|                                                                                   |")
    print("+-----------------------------------------------------------------------------------+")

def menuTransaction():
    print("| " + "\033[96m" + "\033[1m" + "[1] Income                                             " + "\033[0m" + "                           |")
    print("| " + "\033[96m" + "\033[1m" + "[2] Outcome                                            " + "\033[0m" + "                           |")
    print("| " + "\033[96m" + "\033[1m" + "[0] Back                                               " + "\033[0m" + "                           |")
    print("+-----------------------------------------------------------------------------------+")

def menuHistory():
    print("| " + "\033[96m" + "\033[1m" + "[1] by Log                                             " + "\033[0m" + "                           |")
    print("| " + "\033[96m" + "\033[1m" + "[2] by Categories                                      " + "\033[0m" + "                           |")
    print("| " + "\033[96m" + "\033[1m" + "[3] by Transaction type                                " + "\033[0m" + "                           |")
    print("| " + "\033[96m" + "\033[1m" + "[0] Back                                               " + "\033[0m" + "                           |")
    print("+-----------------------------------------------------------------------------------+")

def menuRecap():
    print("| " + "\033[96m" + "\033[1m" + "[1] Day                                                " + "\033[0m" + "                           |")
    print("| " + "\033[96m" + "\033[1m" + "[2] Week                                               " + "\033[0m" + "                           |")
    print("| " + "\033[96m" + "\033[1m" + "[3] Month                                              " + "\033[0m" + "                           |")
    print("| " + "\033[96m" + "\033[1m" + "[0] Back                                               " + "\033[0m" + "                           |")
    print("+-----------------------------------------------------------------------------------+")

def menuDiagram():
    print("| " + "\033[96m" + "\033[1m" + "[1] [Bar Chart] Transaction Frequency                  " + "\033[0m" + "                           |")
    print("| " + "\033[96m" + "\033[1m" + "[2] [Bar Chart] Transaction type Frequency             " + "\033[0m" + "                           |")
    print("| " + "\033[96m" + "\033[1m" + "[0] Back                                               " + "\033[0m" + "                           |")
    print("+-----------------------------------------------------------------------------------+")

def menuSav():
    print("| " + "\033[96m" + "\033[1m" + "[1] Add Savings Balance                                " + "\033[0m" + "                           |")
    print("| " + "\033[96m" + "\033[1m" + "[2] Subtract Savings Balance                           " + "\033[0m" + "                           |")
    print("| " + "\033[96m" + "\033[1m" + "[3] History Savings Balance                            " + "\033[0m" + "                           |")
    print("| " + "\033[96m" + "\033[1m" + "[0] Back                                               " + "\033[0m" + "                           |")
    print("+-----------------------------------------------------------------------------------+")

def contentLevelA():
    print("|" + "\033[93m" + " (*) Anda telah menunjukkan keahlian dalam mengelola keuangan Anda dengan baik.    " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     Anda memiliki kontrol yang kuat atas pemasukan dan pengeluaran Anda, yang     " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     memungkinkan Anda untuk memiliki surplus finansial secara konsisten.          " + "\033[0m" + "|")
    print("|" + "\033[93m" + " (*) Anda termasuk dalam kelompok orang yang sangat bijaksana dalam pengelolaan    " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     keuangan pribadi.                                                             " + "\033[0m" + "|")
    print("|" + "\033[93m" + " (*) Dengan stabilitas keuangan yang Anda miliki, Anda memiliki kesempatan untuk   " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     mencapai banyak hal. Anda bisa mempertimbangkan investasi jangka panjang,     " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     merencanakan liburan impian, atau bahkan memulai bisnis baru.                 " + "\033[0m" + "|")
    print("|" + "\033[93m" + " (*) Teruslah memantau keuangan Anda meskipun dalam keadaan stabil. Pertimbangkan  " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     untuk melakukan diversifikasi investasi untuk meningkatkan keamanan finansial " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     Anda di masa depan.                                                           " + "\033[0m" + "|")
    print("|" + "\033[93m" + "                                                                                   " + "\033[0m" + "|")
    print("|" + "\033[93m" + " (!) \"Kekayaan bukanlah tentang berapa banyak yang Anda miliki, tetapi tentang     " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     bagaimana Anda mengelolanya.\" - Andrew Carnegie                               " + "\033[0m" + "|")

def contentLevelB():
    print("|" + "\033[93m" + " (*) Anda telah menunjukkan disiplin yang baik dalam mengelola keuangan Anda,      " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     meskipun ada sedikit ruang untuk perbaikan. Meskipun demikian, Anda secara    " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     umum memiliki kontrol yang baik atas keuangan Anda.                           " + "\033[0m" + "|")
    print("|" + "\033[93m" + " (*) Anda termasuk dalam kelompok orang yang cermat dalam mengatur keuangan        " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     pribadi mereka.                                                               " + "\033[0m" + "|")
    print("|" + "\033[93m" + " (*) Dengan sedikit penyesuaian, Anda dapat meningkatkan keamanan finansial Anda   " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     lebih lanjut. Anda mungkin perlu mempertimbangkan tabungan atau investasi     " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     tambahan untuk mengoptimalkan potensi keuangan Anda.                          " + "\033[0m" + "|")
    print("|" + "\033[93m" + " (*) Teruslah memantau dan evaluasi keuangan Anda secara teratur. Perhatikan       " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     pola pengeluaran Anda dan pastikan untuk mengalokasikan dana untuk tabungan   " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     darurat dan kebutuhan masa depan.                                             " + "\033[0m" + "|")
    print("|" + "\033[93m" + "                                                                                   " + "\033[0m" + "|")
    print("|" + "\033[93m" + " (!) \"Orang bijaksana membangun kebahagiaan mereka sendiri dengan melepaskan       " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     beban hutang, dan menciptakan kehidupan yang sederhana dan memadai untuk      " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     diri mereka sendiri.\" - Confucius                                             " + "\033[0m" + "|")

def contentLevelC():
    print("|" + "\033[93m" + " (*) Anda mungkin menghadapi beberapa tantangan dalam mengelola keuangan Anda,     " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     tetapi Anda masih memiliki kesempatan untuk memperbaikinya. Penting untuk     " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     mengidentifikasi area di mana Anda bisa mengurangi pengeluaran atau           " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     meningkatkan pemasukan.                                                       " + "\033[0m" + "|")
    print("|" + "\033[93m" + " (*) Anda termasuk dalam kelompok orang yang perlu sedikit bantuan dalam mengatur  " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     keuangan pribadi mereka.                                                      " + "\033[0m" + "|")
    print("|" + "\033[93m" + " (*) Dengan perencanaan dan disiplin yang tepat, Anda masih dapat mencapai banyak  " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     hal. Fokuslah pada membangun kebiasaan pengelolaan keuangan yang sehat dan    " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     memprioritaskan tujuan keuangan jangka panjang.                               " + "\033[0m" + "|")
    print("|" + "\033[93m" + " (*) Buatlah anggaran yang realistis dan ikuti dengan disiplin. Jangan ragu        " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     untuk mencari saran dari profesional keuangan jika Anda memerlukan bantuan    " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     dalam merencanakan keuangan Anda.                                             " + "\033[0m" + "|")
    print("|" + "\033[93m" + "                                                                                   " + "\033[0m" + "|")
    print("|" + "\033[93m" + " (!) \"Kemiskinan bukanlah keadaan alamiah. Manusia membuat kemiskinan dan karena   " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     itu bisa diatasi dan dihilangkan.\" - Nelson Mandela                          " + "\033[0m" + "|")

def contentLevelD():
    print("|" + "\033[93m" + " (*) Anda mungkin menghadapi tantangan yang signifikan dalam mengelola keuangan    " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     Anda, tetapi jangan putus asa. Ada langkah-langkah yang dapat Anda ambil      " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     untuk memperbaiki situasi keuangan Anda.                                      " + "\033[0m" + "|")
    print("|" + "\033[93m" + " (*) Anda termasuk dalam kelompok orang yang memerlukan bantuan mendesak dalam     " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     mengatur keuangan pribadi mereka.                                             " + "\033[0m" + "|")
    print("|" + "\033[93m" + " (*) Meskipun situasi Anda mungkin sulit saat ini, tetapi dengan upaya dan fokus   " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     yang tepat, Anda masih dapat meraih stabilitas keuangan dan mencapai tujuan   " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     Anda.                                                                         " + "\033[0m" + "|")
    print("|" + "\033[93m" + " (*) Mulailah dengan membuat anggaran yang jelas dan berkomitmen untuk mengikutinya" + "\033[0m" + "|")
    print("|" + "\033[93m" + "     mengikutinya Segera cari bantuan dari ahli keuangan atau konselor keuangan    " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     untuk membantu Anda merencanakan strategi pemulihan keuangan yang efektif.    " + "\033[0m" + "|")
    print("|" + "\033[93m" + " (*) Jangan ragu untuk meminta dukungan dari keluarga dan teman-teman Anda dalam   " + "\033[0m" + "|")
    print("|" + "\033[93m" + "     perjalanan ini.                                                               " + "\033[0m" + "|")
    print("|" + "\033[93m" + "                                                                                   " + "\033[0m" + "|")
    print("|" + "\033[93m" + " (!) \"Kemiskinan adalah keadaan sementara, tidak pernah keadaan alamiah.\"          " + "\033[0m" + "|") 
    print("|" + "\033[93m" + "     - Muhammad Yunus                                                              " + "\033[0m" + "|")