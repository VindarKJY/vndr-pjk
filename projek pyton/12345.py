import tkinter as tk

def generate_html(color):
    html_code = f"""
    <html>
      <head>
        <title>Background Demo</title>
        <style>
          body {{
            background-color: {color};
          }}
        </style>
      </head>
      <body>
        <h1>Halo! Background saya {color}</h1>
      </body>
    </html>
    """
    # Simpan ke file
    with open("demo.html", "w", encoding="utf-8") as file:
        file.write(html_code)
    print(f"✅ File HTML dibuat dengan background {color}")

# UI dengan Tkinter
root = tk.Tk()
root.title("Pengubah Background")

# Tombol pilihan warna
tk.Button(root, text="Merah", command=lambda: generate_html("red")).pack(pady=5)
tk.Button(root, text="Biru", command=lambda: generate_html("blue")).pack(pady=5)
tk.Button(root, text="Hijau", command=lambda: generate_html("green")).pack(pady=5)

root.mainloop()
