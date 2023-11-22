import tkinter as tk
import sqlite3
from tkinter import messagebox

# Parameter nya tergantung isi dari content
def simpan_data_ke_sqlite(Nama_Siswa, Biologi, Fisika, Inggris, prediksi_fakultas):
    # Connect Database
    con = sqlite3.connect("sqlite3.db")
    cursore = con.cursor()

    # Membuat Table jika Table belum di buat
    cursore.execute('''CREATE TABLE IF NOT EXISTS hasil_nilai
                    (No_Urut PRIMARY KEY AUTOINCREMENT, 
                    Nama_Siswa TEXT,
                    Biologi INTEGER,
                    Fisika INTEGER,
                    Inggris INTEGER)''')
            

    # Insert Data kedalam Table hasil_prediksi
    cursore.execute('''INSERT INTO hasil_prediksi(Nama_Siswa, Biologi, Fisika, Inggris, prediksi_fakultas) VALUES (?,?,?)''', (Nama_Siswa, Biologi, Fisika, Inggris, prediksi_fakultas))

    con.commit()
    con.close()

    
#fungsi untuk menampilkan
def tampilkan():
    nama_siswa = e1.get()
    Biologi = e2.get()
    Fisika = e3.get()
    Inggris = e4.get()

    nama_siswa = f"Nama Mahasiswa: {nama_siswa}"
    hasilBio = f"Nilai Biologi: {Biologi}"
    hasilFis = f"Nilai Fisika: {Fisika}"
    hasilIng = f"Nilai Inggris: {Inggris}"


    label_nama_siswa.config(text=nama_siswa)
    label_hasilBio.config(text=hasilBio)
    label_hasilFis.config(text=hasilFis)
    label_hasilIng.config(text=hasilIng)


    messagebox.showinfo("Info","Data Telah Disimpan")

    if not Biologi and not Fisika and not Inggris and not nama_siswa:
        frame_input.pack_forget()
    else:
        frame_input.pack()
        Prediksi_fakultas = Prediksi_fakultas(Biologi, Fisika, Inggris)
        simpan_data_ke_sqlite(nama_siswa, Biologi, Fisika, Inggris, Prediksi_fakultas)

#fungsi prediksi fakultas
def Prediksi_Fakultas(nilai_biologi, nilai_fisika, nilai_inggris):
    if nilai_biologi> nilai_fisika and nilai_biologi > nilai_inggris:
        print ("Kedokteran")
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        print ("Teknik")
    else:
        print ("Bahasa")
    
    hasil_prediksi = Prediksi_Fakultas(nilai_biologi, nilai_fisika, nilai_inggris)
    print("Prediksi Fakultas:", hasil_prediksi)


# Buat Jendela Halaman
root = tk.Tk()
root.title("Prediksi fakultas")
root.geometry("500x500")
root.resizable(False, False)

# Bikin label untuk judul
label_judul = tk.Label(root, text="Prediksi Fakultas Pilihan", font=("Times",14,"bold"))
label_judul.pack(pady=20)

# Buat Frame inputan
frame_input = tk.LabelFrame(root, labelanchor="n",pady=10, padx=10)
frame_input.pack()

# bikin input nama mahasiswa(label)
Input = tk.Label(frame_input, text="Masukkan Nama Siswa: ")
Input.pack(padx=10, pady=5, fill="x", expand=True)
e1 = tk.Entry(frame_input)
e1.pack(padx=10, pady=5, fill="x", expand=True)

# bikin input nilai Biologi (label)
Input2 = tk.Label(frame_input, text="Masukkan Nilai Biologi: ")
Input2.pack(padx=10, pady=5, fill="x", expand=True)
e2 = tk.Entry(frame_input)
e2.pack(padx=10, pady=5, fill="x", expand=True)

# bikin input nilai fisika (label)
Input3 = tk.Label(frame_input, text="Masukkan Nilai Fisika: ")
Input3.pack(padx=10, pady=5, fill="x", expand=True)
e3 = tk.Entry(frame_input)
e3.pack(padx=10, pady=5, fill="x", expand=True)

# bikin input nilai Inggris (label)
Input4 = tk.Label(frame_input, text="Masukkan Nilai Inggris: ")
Input4.pack(padx=10, pady=5, fill="x", expand=True)
e4 = tk.Entry(frame_input)
e4.pack(padx=10, pady=5, fill="x", expand=True)

# Tombol Hasil
btn_hasil = tk.Button(root, text="Submit", command=tampilkan)
btn_hasil.pack(pady=10)

frame_input = tk.LabelFrame(root,labelanchor="n", padx=10,pady=10)
frame_input.pack_forget()

# Label Hasil
label_nama_siswa = tk.Label(frame_input, text="")
label_nama_siswa.pack()

label_hasilBio = tk.Label(frame_input, text="")
label_hasilBio.pack()

label_hasilFis = tk.Label(frame_input, text="")
label_hasilFis.pack()

label_hasilIng = tk.Label(frame_input, text="")
label_hasilIng.pack()


# Jalankan Aplikasi
root.mainloop()