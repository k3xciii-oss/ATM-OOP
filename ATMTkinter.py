import tkinter as tk
from tkinter import messagebox

class ATMApp:
    
    def __init__(self,rekening):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.rekening = rekening
        self.halaman_login()
    

    def halaman_login(self):
        label = tk.Label(self.root, text='Login')
        label.pack()
        
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.entry.focus()
        
        btn = tk.Button(self.root, text='Login', command=self.proses_login)
        btn.pack()

    def proses_login(self):
        pin = self.entry.get()
        status, pesan = self.rekening.login(pin)
        if status:
            messagebox.showinfo('STATUS', pesan)
            self.clear_window()
            self.halaman_menu()
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
    def halaman_menu(self):
        # Label 
        label = tk.Label(self.root, text=f'Selamat datang {self.rekening.nama}')
        label.pack(pady=5)
        
        # Tombol untuk lihat saldo
        btn_saldo = tk.Button(self.root, text='Cek Saldo', command=self.cek_saldo)
        btn_saldo.pack(pady=5)
        
        # Tombol untuk setor uang
        btn_setor = tk.Button(self.root, text='Setor Uang', command=self.halaman_setor)
        btn_setor.pack(pady=5)
        
        # Tombol untuk tarik uang
        btn_tarik = tk.Button(self.root, text='Tarik Uang', command=self.halaman_tarik)
        btn_tarik.pack(pady=5)
        
        # Tombol untuk Log out
        btn_logout = tk.Button(self.root, text='Log Out', command=self.logout)
        btn_logout.pack(pady=5)
    
    # fungsi untuk kembali ke menu       
    def kembali_ke_menu(self):
        self.clear_window()
        self.halaman_menu()
    
        
        
    def cek_saldo(self):
        saldo = self.rekening.cek_saldo()
        if saldo is None:
            messagebox.showerror('Error', 'Silahkan login terlebih dahulu')
        else:
            messagebox.showinfo('Saldo', f'Saldo anda: Rp {saldo:,}')
    
    def proses_setor(self):
        try:
            uang = int(self.entry_setor.get())
            status, pesan = self.rekening.setor(uang)
            
            if status:
                messagebox.showinfo('Sukses', pesan)
                self.kembali_ke_menu()
            else:
                messagebox.showinfo('Error', pesan)
        except:
            messagebox.showerror('Error', 'Input harus angka')
    
    def halaman_setor(self):
        self.clear_window()
        
        # Label
        label = tk.Label(self.root, text='Masukkan jumlah uang yang mau di setor')
        label.pack(pady=5)
        
        # Input jumlah setor
        self.entry_setor = tk.Entry(self.root)
        self.entry_setor.pack()
        
        # Tombol setor dan kembali
        btn = tk.Button(self.root, text='Setor', command=self.proses_setor)
        btn.pack()
        
        btn_back = tk.Button(self.root, text='Kembali', command=self.kembali_ke_menu)
        btn_back.pack()
        
    def proses_tarik(self):
        try:
            uang = int(self.entry_tarik.get())
            status, pesan = self.rekening.tarik(uang)
            
            if status:
                messagebox.showinfo('Sukses', pesan)
                self.kembali_ke_menu()
            else:
                messagebox.showinfo('Error', pesan)
                
        except:
            messagebox.showerror('Error', 'Harus memasukkan angka')
        
    def halaman_tarik(self):
        self.clear_window()
        
        # label
        label = tk.Label(self.root, text='Masukkan jumlah tarik')
        label.pack()
        
        # Input jumlah tarik
        self.entry_tarik = tk.Entry(self.root)
        self.entry_tarik.pack()
        
        # Tombol
        btn = tk.Button(self.root, text='Tarik Tunai', command=self.proses_tarik)
        btn.pack()
        
        btn_back = tk.Button(self.root, text='Kembali', command=self.kembali_ke_menu)
        btn_back.pack()
        
    def logout(self):
        self.rekening.logout()
        self.clear_window()
        self.halaman_login()
        
        
class Rekening:
    
    def __init__(self, nama, pin, saldo):
        self.nama = nama
        self.pin = pin
        self.saldo = saldo
        self.riwayat = []
        self.isLogin = False

    def login(self, pin_input):
        if pin_input == self.pin:
            self.isLogin = True
            return True, f"Berhasil login, selamat datang {self.nama}"
        else:
            return False, "PIN salah!"

    def cek_saldo(self):
        if self.isLogin:
            return self.saldo
        else:
            return None

    def setor(self, uang):
        if not self.isLogin:
            return False, "Silakan login terlebih dahulu"
        
        if uang <= 0:
            return False, "Jumlah tidak valid"

        self.saldo += uang
        self.riwayat.append(f"Setor: {uang}")
        return True, f"Berhasil setor Rp {uang}"

    def tarik(self, uang):
        if not self.isLogin:
            return False, "Silakan login terlebih dahulu"
        
        if uang <= 0:
            return False, "Jumlah tidak valid"

        if uang > self.saldo:
            return False, "Saldo tidak cukup"

        self.saldo -= uang
        self.riwayat.append(f"Tarik: {uang}")
        return True, f"Berhasil tarik Rp {uang}"

    def logout(self):
        self.isLogin = False
        return "Berhasil logout"
    
    

rekening = Rekening("Keci", "1234", 100000)

app = ATMApp(rekening)
app.root.mainloop()