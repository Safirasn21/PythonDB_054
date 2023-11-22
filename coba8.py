import tkinter as tk
from tkinter import messagebox
import sqlite3

def simpan_data_ke_sqlite(nama_siswa, Biologi, Fisika, Inggris, Prediksi_Fakultas):
    conn = sqlite3.connect("sqlite3.db")
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa
                    (No_Urut INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nama_siswa TEXT, 
                    Biologi INTEGER,
                    Fisika INTEGER,
                    Inggris INTEGER,
                    Prediksi_Fakultas TEXT)''')
    
    cursor.execute("INSERT INTO nilai_siswa (nama_siswa, Biologi, Fisika, Inggris, Prediksi_Fakultas) VALUES (?, ?, ?, ?, ?)",
                   (nama_siswa, Biologi, Fisika, Inggris, Prediksi_Fakultas))

    conn.commit()
    conn.close()

def prediksi_fakultas(Biologi, Fisika, Inggris):
    if Biologi > Fisika and Biologi > Inggris:
        return "Kedokteran"
    elif Fisika > Biologi and Fisika > Inggris:
        return "Teknik"
    else:
        return "Bahasa"

def tampilkan():
    nama_siswa = e1.get()
    Biologi = int(e2.get())
    Fisika = int(e3.get())
    Inggris = int(e4.get())

    prediksi = prediksi_fakultas(Biologi, Fisika, Inggris)

    label_nama_siswa.config(text=f"Nama Mahasiswa: {nama_siswa}")
    label_hasilBio.config(text=f"Nilai Biologi: {Biologi}")
    label_hasilFis.config(text=f"Nilai Fisika: {Fisika}")
    label_hasilIng.config(text=f"Nilai Inggris: {Inggris}")
    label_hasilPrediksi.config(text=f"Hasil Prediksi: {prediksi}")

    simpan_data_ke_sqlite(nama_siswa, Biologi, Fisika, Inggris, prediksi)
    messagebox.showinfo("Info", "Data Tersimpan")

# Buat Jendela Halaman
top = tk.Tk()
top.title("Prediksi fakultas")
top.geometry("500x500")
top.resizable(False, False)

# Buat Frame inputan
inputframe = tk.LabelFrame(top)
inputframe.pack(padx=10, pady=10, fill="x", expand=True)

# Bikin label untuk judul
var = tk.Label(inputframe, text="NILAI MAHASISWA", font=("Times", 14, "bold"))
var.pack()

# Bikin input 1 (label)
Input = tk.Label(inputframe, text="Masukkan Nama Siswa: ")
Input.pack(padx=10, pady=5, fill="x", expand=True)
e1 = tk.Entry(inputframe)
e1.pack(padx=10, pady=5, fill="x", expand=True)

# Bikin input 2 (label)
Input2 = tk.Label(inputframe, text="Masukkan Nilai Biologi: ")
Input2.pack(padx=10, pady=5, fill="x", expand=True)
e2 = tk.Entry(inputframe)
e2.pack(padx=10, pady=5, fill="x", expand=True)

# Bikin input 3
Input3 = tk.Label(inputframe, text="Masukkan Nilai Fisika: ")
Input3.pack(padx=10, pady=5, fill="x", expand=True)
e3 = tk.Entry(inputframe)
e3.pack(padx=10, pady=5, fill="x", expand=True)

# Bikin input 4
Input4 = tk.Label(inputframe, text="Masukkan Nilai Inggris: ")
Input4.pack(padx=10, pady=5, fill="x", expand=True)
e4 = tk.Entry(inputframe)
e4.pack(padx=10, pady=5, fill="x", expand=True)

# Tombol Hasil
btn_hasil = tk.Button(top, text="Submit", command=tampilkan)
btn_hasil.pack(pady=10)

# Label Hasil
label_nama_siswa = tk.Label(top, text="")
label_nama_siswa.pack()

label_hasilBio = tk.Label(top, text="")
label_hasilBio.pack()

label_hasilFis = tk.Label(top, text="")
label_hasilFis.pack()

label_hasilIng = tk.Label(top, text="")
label_hasilIng.pack()

label_hasilPrediksi = tk.Label(top, text="")
label_hasilPrediksi.pack()

# Jalankan Aplikasi
top.mainloop()