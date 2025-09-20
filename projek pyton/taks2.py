import tkinter as tk

# Buat jendela utama
window = tk.Tk()
window.title("💖 Untukmu, Sayangku 💖")
window.geometry("500x400")
window.configure(bg="#FFD6E0")  # warna pink lembut

# Judul cantik
judul = tk.Label(window, text="💘 Pesan Cinta 💘", 
                 font=("Comic Sans MS", 20, "bold"), 
                 fg="#FF007F", bg="#FFD6E0")
judul.pack(pady=20)

# Pesan cinta
pesan = """
Sayangku tersayang 🌸,
Aku cuma mau bilang...
Kamu adalah alasan aku tersenyum tiap hari 😊
Aku bersyukur banget punya kamu di hidupku 💕
Selamanya kita bersama 💖
"""

label = tk.Label(window, text=pesan, font=("Arial", 12), 
                 fg="#800080", bg="#FFD6E0", wraplength=450, justify="center")
label.pack(pady=10)

# Tambahan emoji hiasan
emoji = tk.Label(window, text="🌹🌹🌹", font=("Arial", 30), bg="#FFD6E0")
emoji.pack()

# Tombol romantis
btn = tk.Button(window, text="💌 Aku juga sayang kamu!", 
                font=("Arial", 12, "bold"), 
                fg="white", bg="#FF69B4", 
                activebackground="#FF1493", activeforeground="white",
                relief="raised", bd=5,
                command=window.destroy)
btn.pack(pady=20)

# Jalankan aplikasi
window.mainloop()

