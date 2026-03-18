import os

def clear():
    os.system('cls')
# class dan fungsi/method

class Rekening:
    def __init__(self,nama,pin,saldo):
        self.nama = nama
        self.pin = pin
        self.saldo = saldo
        self.isLogin = False
    def login(self,pin_input):
        if pin_input == self.pin:
            self.isLogin = True
            print(f'berhasil login {self.nama}')
        else:
            print('PIN salah!')
            
    def cek_saldo(self):
        if self.isLogin:
            print(f'Saldo kamu: {self.saldo}')
        else:
            print('Loin terlebih dahulu')
            
    def setor(self,uang):
        if self.isLogin:
            self.saldo += uang
            print(f'Berhasil setor uang sebanyak Rp {uang}')
        else:
            print('login terlebih dahulu')
            
    def tarik(self,uang):
        if self.isLogin:
            if uang > self.saldo:
                print('Saldo tidak cukup')
            else:
                self.saldo -= uang
                print(f'Berhasil tarik uang dair saldo sebesar Rp {uang}')
        else:
            print('Silahkan login terlebih dahulu')
            
    def logOut(self):
        self.isLogin = False 
        print('Berhasil log out')
        
# PROGRAM UTAMA

nama = input('Buat Nama Rekening: ')
pin = int(input('Buat PIN: '))
saldo = int(input('Masukkan saldo: '))
rekening1 = Rekening(nama,pin,saldo)
clear()

# LOGIN
for i in range(3):
    pin = int(input('Login dengan PIN: '))
    rekening1.login(pin)
    if rekening1.isLogin:
        break
else:
    print('Akun Diblokir')
    exit()
        
# MENU

while rekening1.isLogin:
    clear()
    print('\n=====Menu ATM=====')
    print('1. cek saldo')
    print('2. Setor uang')
    print('3.Tarik uang')
    print('4. Log out')
    
    pilihan = input('Pilih Menu (1,2,3,4): ')
    
    if pilihan == '1':
        rekening1.cek_saldo()
        input('Tekan Enter kalau mau kembali ke menu')
    
    elif pilihan =='2':
        jumlah = int(input('Masukkan jumlah yang ingin di setor: '))
        rekening1.setor(jumlah)
        input('Tekan Enter kalau mau kembali ke menu')
        
    elif pilihan == '3':
        jumlah = int(input('Masukkan jumlah yang mau di tarik: '))
        rekening1.tarik(jumlah) 
        input('Tekan Enter kalau mau kembali ke menu')
    
    elif pilihan == '4':
        rekening1.logOut()
 
        
    else:
        print('Pilihan tidak valid')   

