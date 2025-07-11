print ("hello world") 

print ("Hai disini saya akan memulai mencoba sebuah program yang saya inginkan") 
 
namaa = input("siapa nama mu : ") 

print(f"Okee {namaa}, kamu akan menentukan pilihan disini, pilihan mu akan menjadi sebuah kenyataan")   

def menupilihan() :
    while True:
        print("1. area I") 
        print("2. area II")
        print("3. area III")
        print("4. area IV")
        print("5. area V")
    
        Angka = input("Masukan menu pilihan mu : ") 
        
        if Angka == "1" :
            print("===========================================") 
            print(f"Yooo, {namaa} akan menjelajahi kata kata") 
            a1 = input("kata kata apa yang kamu inginkan ?") 
            print(f"{a1}, diterima") 
            print("===========================================")
            menupilihan() 
            break 
        elif Angka == "2" : 
            print(f"{namaa}, akan mendapatkan kekuatan kata-kata")
            break
        elif Angka == "3" :
            print(f"{namaa} akan mengendaki kata-kata mu")
            break
        elif Angka == "4" :
            print("Suka suka dalam berkata namun tidak dengan makna nya")
            break
        else :  
            print(f"{namaa} akan keluar") 
            break 
menupilihan() 

print("disini kamu telah mencoba nya yaa, nah nanti saya akan membuat nya sesuai kemampuan saya yang telah di pelajari") 
print("Heyy, kamu disana lagi bahagia dan tertarik lagi kan, ayo belajar lagi dan kembangkan skill program mu")
