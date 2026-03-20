import tkinter as tk
from tkinter import messagebox

class ATMApp:
    
    def __init__(self,rekening):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.configure(bg="#1e1e2f")
        self.rekening = rekening
        self.halaman_login()
    

    def buat_akun(self):
        self.root.configure(bg="#1e1e2f")

        frame = tk.Frame(self.root, bg="#2c2c3e", padx=20, pady=20)
        frame.pack(pady=50)

        # Judul
        tk.Label(
            frame,
            text='Buat Akun',
            font=('Arial', 16, 'bold'),
            bg='#2c2c3e',
            fg='white'
        ).pack(pady=10)

        # Nama
        tk.Label(frame, text='Masukkan Nama:', bg='#2c2c3e', fg='white').pack()
        self.entry_nama = tk.Entry(frame)
        self.entry_nama.pack(pady=5)

        # PIN
        tk.Label(frame, text='Masukkan PIN:', bg='#2c2c3e', fg='white').pack()
        self.entry_pin = tk.Entry(frame, show='*')
        self.entry_pin.pack(pady=5)

        # Saldo
        tk.Label(frame, text='Saldo Awal:', bg='#2c2c3e', fg='white').pack()
        self.entry_saldo = tk.Entry(frame)
        self.entry_saldo.pack(pady=5)

        # Button
        tk.Button(
            frame,
            text='Buat Akun',
            font=('Arial', 10, 'bold'),
            bg='#4CAF50',
            fg='white',
            relief='flat',
            command=self.proses_buat
        ).pack(pady=15)
    
    def proses_buat(self):
        nama = self.entry_nama.get()
        pin = self.entry_pin.get()
        saldo = self.entry_saldo.get()
        
        if nama == '' or pin =='' or saldo == '':
            messagebox.showerror('Error', 'Semua data harus diisi')
            return
        if not pin.isdigit():
            messagebox.showerror('Error', 'PIN harus angka')
            return
        if not saldo.isdigit():
            messagebox.showerror('Error', 'Saldo harus angka')
            return
            
        self.rekening = Rekening(nama, pin, int(saldo))
        messagebox.showinfo('Sukses', 'Akun berhasil di buat')
        self.halaman_login()
        
    
    def halaman_login(self):
        self.clear_window()
        frame = tk.Frame(self.root, bg='#2c2c3e', padx=20, pady=20)
        frame.pack(pady=50)
        
        label = tk.Label(
            frame,
            text='Login',
            font=('Arial', 16, 'bold'),
            bg="#2c2cbd", 
            fg='white'
            ).pack(pady=10)
        
        self.entry = tk.Entry(frame)
        self.entry.pack()
        self.entry.focus()
        
        btn_login = tk.Button(
            frame,
            text='Login',
            bg='#4CAF50',
            fg='white',
            relief='flat',
            command=self.proses_login
            ).pack(pady=10)
        btn_buat = tk.Button(
            frame,
            text='Buat Akun',
            bg='#2196F3',
            fg='white',
            relief='flat',
            command=lambda: [self.clear_window(),self.buat_akun()]
        ).pack(pady=5)
        

    def proses_login(self):
        if self.rekening is None:
            messagebox.showerror('Error', 'Belum ada akun yang di buat')
            return
        pin = self.entry.get()
        status, pesan = self.rekening.login(pin)
        if status:
            messagebox.showinfo('STATUS', pesan)
            self.clear_window()
            self.halaman_menu()
        else:
            messagebox.showerror('Error', pesan)
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
    def halaman_menu(self):
        # Label 
        label = tk.Label(
            self.root,
            text=f'Selamat datang {self.rekening.nama}',
            font=('Arial', 16, 'bold'),
            bg="#2323b8",
            fg='white')
        
        label.pack(pady=50)
        
        # Tombol untuk lihat saldo
        btn_saldo = tk.Button(
            self.root,
            text='Cek Saldo',
            bg='#4CAF50',
            fg='white',
            relief='flat',
            command=self.cek_saldo)
        btn_saldo.pack(pady=5)
        
        # Tombol untuk setor uang
        btn_setor = tk.Button(
            self.root,
            text='Setor Uang',
            bg='#4CAF50',
            fg='white',
            relief='flat',
            command=self.halaman_setor)
        btn_setor.pack(pady=5)
        
        # Tombol untuk tarik uang
        btn_tarik = tk.Button(
            self.root,
            text='Tarik Uang',
            bg='#4CAF50',
            fg='white',
            relief='flat',
            command=self.halaman_tarik)
        btn_tarik.pack(pady=5)
        
        # Tombol untuk Log out
        btn_logout = tk.Button(
            self.root,
            text='Log Out',
            bg='#4CAF50',
            fg='white',
            relief='flat',
            command=self.logout)
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
        label = tk.Label(
            self.root,
            text='Masukkan jumlah uang yang mau di setor',
            font=('Arial', 16, 'bold'),
            bg="#2a2adb",
            fg='white')
        label.pack(pady=50)
        
        # Input jumlah setor
        self.entry_setor = tk.Entry(self.root)
        self.entry_setor.pack(pady=50)
        
        # Tombol setor dan kembali
        btn = tk.Button(
            self.root,
            text='Setor',
            bg='#4CAF50',
            fg='white',
            relief='flat',
            command=self.proses_setor)
        btn.pack(pady=5)
        
        btn_back = tk.Button(
            self.root,
            text='Kembali',
            bg='#4CAF50',
            fg='white',
            relief='flat',
            command=self.kembali_ke_menu)
        btn_back.pack(pady=5)
        
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
        label = tk.Label(
            self.root,
            text='Masukkan jumlah tarik',
            font=('Arial', 16, 'bold'),
            bg='#2a2adb',
            fg='white'
            )
        label.pack(pady=50)
        
        # Input jumlah tarik
        self.entry_tarik = tk.Entry(self.root)
        self.entry_tarik.pack(pady=50)
        
        # Tombol
        btn = tk.Button(
            self.root,
            text='Tarik Tunai',
            bg='#4CAF50',
            fg='white',
            relief='flat',
            command=self.proses_tarik)
        btn.pack(pady=5)
        
        btn_back = tk.Button(
            self.root,
            text='Kembali',
            bg='#4CAF50',
            fg='white',
            relief='flat',
            command=self.kembali_ke_menu)
        btn_back.pack(pady=5)
        
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
    
    

rekening = None

app = ATMApp(rekening)
app.root.mainloop()