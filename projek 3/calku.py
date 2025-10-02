import tkinter as tk

def click(event):
    current = entry.get()
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Modern Calculator")
root.configure(bg="#2e2e2e")

entry = tk.Entry(root, font=("Segoe UI", 24), borderwidth=8, relief=tk.RIDGE, justify='right', bg="#3c3f41", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','C','=','+'
]

for i, b in enumerate(buttons):
    color = "#4a4d4f" if b.isdigit() or b == '0' else "#f39c12" if b in "+-*/" else "#c0392b" if b == "C" else "#27ae60"
    btn = tk.Button(root, text=b, font=("Segoe UI", 20, "bold"), bg=color, fg="white", activebackground="#16a085", relief=tk.RAISED, bd=4)
    btn.grid(row=1 + i//4, column=i%4, padx=5, pady=5, sticky="nsew")
    btn.bind("<Button-1>", click)

# Responsif: tombol menyesuaikan ukuran jendela
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
