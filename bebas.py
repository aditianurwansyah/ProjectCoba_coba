# import string 

# nama = input("masukan nama : ")
# print(f"nama ku adalah {nama}")

# angka = int(input("masukan angka : "))
# if angka > 2 :
#     print("kamu lebih besar dari gajah ")
# else :
#     print("kamu kecil kek semut")

# menu = int(input("silahkan pilih menu : "))
# if menu == 1 :
#      print("nasi goreng")
# elif menu == 2 :
#     print("bala bala ditambah gehu") 
# elif menu == 3:
#     print("tahu bulat ditambah daging krispi") 
# else:
#     print("tidak ada menu dari itu") 
# def main():
#     while True:
#         try:
#             # Meminta input dari pengguna
#             number = int(input("Masukkan angka (atau ketik 'exit' untuk keluar): "))
#             print(f"Anda memasukkan angka: {number}")
#         except ValueError:
#             print("Input tidak valid. Silakan masukkan angka yang benar.")
#         except KeyboardInterrupt:
#             print("\nKeluar dari program.")
#             break  # Keluar dari loop jika pengguna menekan Ctrl+C
#         except Exception as e:
#             print(f"Terjadi kesalahan: {e}")

# # Memanggil fungsi main
# main()    

# def main():
#     while True:
#         print("Menu:")
#         print("1. Pilihan 1")
#         print("2. Pilihan 2")
#         print("3. Keluar")

#         choice = input("Pilih opsi (1/2/3): ")

#         if choice == '1':
#             print("Anda memilih pilihan 1.")
#         elif choice == '2':
#             print("Anda memilih pilihan 2.")
#         elif choice == '3':
#             print("Keluar dari program.")
#             break
#         else:
#             print("Pilihan tidak valid. Silakan coba lagi.")

# # Memanggil fungsi main 
# main() 

print("Hello semua nya disini saya akan melakukan berbagai program yang saya inginkan, namun ini hanya keinginan sendiri yang keluarkan dari pikiran saya")
print("=================================================================================================================================================") 
a = input("Sebelum itu perkenalkan siapa nama mu? : ") 
print(f"Oke, {a} disini kamu akan melakukan sesuatu hal yang luar biasa karena ini program mu") 

aUmur=  int(input("Okee, sebelum itu usia kamu berapa sih? : ")) 
if aUmur < 20 :
    print("Okee kamu masih anak anak dari usia 1-19")
else :
    print("Ohh kamu udah dewasa :) ") 
print("===================================================================")
print("setelah kamu mengisi identitas mu sekarang ke bagian percobaan nya ")

sajawab = input("Apa yang kamu inginkan ? : ") 

def Pilihan():
    if sajawab == "Makanan" :
        print("Yang kamu inginkan adalah makanan")
    elif sajawab == "Minuman" : 
        print("Yang kamu inginkan adalah minuman") 
    elif sajawab == "Barang" : 
        print("Yang kamu inginkan adalah Barang")
        p1 = input("barang apa yang kamu mau? : ")
        if p1 == "elektronik" :
            print("pilihan kamu diantara nya kemungkinan Handphone") 
        else :
            print("Ok, bukan barang yang kamu butuhkan")
    else :
        print("ngapain ngisi udah gausah bikin repot aja :> ") 
Pilihan()  