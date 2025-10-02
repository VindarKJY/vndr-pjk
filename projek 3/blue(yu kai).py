import time, random, pygame
from colorama import init, Fore
import tkinter as tk
from tkinter import ttk

# --- Inisialisasi ---
init(autoreset=True)
pygame.mixer.init()
pygame.mixer.music.load(r"C:\myprojek\vndr-pjk\projek 3\blue.mp3")
durasi_lagu = 120  # ganti dengan durasi lagu dalam detik
pygame.mixer.music.play()

# --- Tkinter UI ---
root = tk.Tk()
root.title("Lirik Player")
root.configure(bg="#7C30BB")

label = tk.Label(root, text="Menunggu musik...", font=("Helvetica", 14),
                 fg= "#FAFAFA", bg="#222831", wraplength=380, justify="center")
label.pack(pady=10)

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=5)

# --- Fungsi ---
warna_opsi = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE,
              Fore.MAGENTA, Fore.CYAN, Fore.LIGHTWHITE_EX]

def ketik_per_huruf(teks, delay=0.05):
    warna = random.choice(warna_opsi)
    for huruf in teks:
        print(warna + huruf, end='', flush=True)
        time.sleep(delay)
    print()

def toggle_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        btn.config(text="▶ Play")
    else:
        pygame.mixer.music.unpause()
        btn.config(text="⏸ Pause")

def stop_music():
    pygame.mixer.music.stop()
    root.destroy()

def restart_music():
    pygame.mixer.music.stop()
    pygame.mixer.music.play()
    global start_time
    start_time = time.time()

btn = tk.Button(root, text="⏸ Pause", command=toggle_music)
btn.pack()
btn_stop = tk.Button(root, text="⏹ Stop", command=stop_music)
btn_stop.pack()
btn_restart = tk.Button(root, text="🔄 Restart", command=restart_music)
btn_restart.pack()

# --- Lirik ---
lirik = [
    (19.0, "⛅Your morning eyes,"
           "✨I could stare like watching stars", 0.2, 0.0),
    (26.0, "I could walk you by and I'll tell without a thought", 0.2, 0.4),
    (32.0, "You'd be mine,"
           "would you mind", 0.2, 0.4),
    (40.0, "🌛If I took your hand tonight? ,"
           "Know you're all that I want this life", 0.25, 0.5),

    (48.0, "💖I'll imagine we fell in love ", 0.15, 0.6),
    (51.0, "🌙 I'll nap under moonlight skies with you", 0.06, 0.8),
    (54.0, "🌊 I think I'll picture us, "
           " you with the waves", 0.05, 0.7),
    (58.0, "🎨 The ocean's colors on your face", 0.08, 0.8),
    (62.5, "💞 I'll leave my heart with your air", 0.08, 0.8), 
    (66.0, "🕊 So let me fly with you", 0.08, 0.5),
    (69.0, "💍 Will you be forever with me?", 0.15, 0.6),


    (107.0, "My love will always stay by you", 0.15, 0.6),
    (112.0, "I'll keep it safe, so don't you worry a thing  ", 0.15, 0.6),
    (118.0, "I'll tell you I love you more  ", 0.15, 0.6),
    (121.0, "💕It's stuck with you foreve, So promise you won't let it go ", 0.15, 0.6),
    (128.0, "💫I'll trust the universe will always bring me to you  ", 0.15, 0.6),

    (137.0, "💖I'll imagine we fell in love ", 0.15, 0.6),
    (139.0, "🌙 I'll nap under moonlight skies with you", 0.06, 0.8),
    (143.0, "🌊 I think I'll picture us, "
           "you with the waves", 0.05, 0.7),
    (157.0, "🎨 The ocean's colors on your face", 0.08, 0.8),
    (160.5, "💞 I'll leave my heart with your air", 0.08, 0.8), 
    (165.0, "🕊 So let me fly with you", 0.08, 0.5),
    (168.0, "💍 Will you be forever with me?", 0.15, 0.6),
]


start_time = time.time()

for t, teks, delay_huruf, jeda_baris in lirik:
    while time.time() - start_time < t:
        if pygame.mixer.music.get_busy():
            progress['value'] = min((time.time()-start_time)/durasi_lagu*100, 100)
            root.update()
        time.sleep(0.01)
    ketik_per_huruf(teks, delay_huruf)
    time.sleep(jeda_baris)

root.mainloop()
