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
""".strip()

label = tk.Label(window, text="", font=("Arial", 12), 
                 fg="#800080", bg="#FFD6E0", wraplength=window.winfo_width()-50, justify="center")
label.pack(pady=10)

def update_wraplength(event):
    label.config(wraplength=event.width - 50)

window.bind("<Configure>", update_wraplength)

# Tambahan emoji hiasan
emoji = tk.Label(window, text="🌹🌹🌹", font=("Arial", 30), bg="#FFD6E0")
# emoji.pack()  # Jangan gunakan pack, akan menggunakan place di animasi

# Tombol romantis
btn = tk.Button(window, text="💌 Aku juga sayang kamu!", 
                font=("Arial", 12, "bold"), 
                fg="white", bg="#FF69B4", 
                activebackground="#FF1493", activeforeground="white",
                relief="raised", bd=5,
                command=window.destroy)
btn.pack(pady=20)

# --- Animasi Fade-in untuk pesan ---
def fade_in_message(text, idx=0):
    if idx <= len(text):
        label.config(text=text[:idx])
        window.after(40, fade_in_message, text, idx+1)

# --- Animasi bouncing emoji ---
direction = 1
def bounce_emoji():
    global direction
    y = emoji.winfo_y()
    if y == -1:
        y = 90  # Default starting y position if not yet placed
        emoji.place(x=(window.winfo_width()//2)-70, y=y)
    if y < 60:
        direction = 1
    elif y > 120:
        direction = -1
    emoji.place(x=(window.winfo_width()//2)-70, y=y+direction*2)
    window.after(15, bounce_emoji)

# Mulai animasi setelah window siap
def start_animations():
    fade_in_message(pesan)
    emoji.place(x=(window.winfo_width()//2)-70, y=90)
    bounce_emoji()

window.after(300, start_animations)

window.mainloop()
