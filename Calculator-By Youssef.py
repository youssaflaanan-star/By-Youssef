from tkinter import *

def click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(value))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "خطأ")

root = Tk()
root.title("Calculator - By Youssef")

# ملء الشاشة (يعمل على Pydroid 3)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

root.configure(bg="#222222")

# ===== العنوان مع أنيميشن =====
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
index = 0

title = Label(
    root,
    text="Calculator\nBy Youssef",
    font=("Arial", 28, "bold"),
    bg="#222222"
)
title.pack(pady=20)

def animate():
    global index
    title.config(fg=colors[index])
    index = (index + 1) % len(colors)
    root.after(300, animate)

animate()

# ===== شاشة العرض =====
entry = Entry(root, font=("Arial", 24), justify="right")
entry.pack(fill="x", padx=20, pady=10)

# ===== الأزرار =====
frame = Frame(root, bg="#222222")
frame.pack()

buttons = [
    ("7", "#3498db"), ("8", "#9b59b6"), ("9", "#e67e22"), ("/", "#e74c3c"),
    ("4", "#1abc9c"), ("5", "#2ecc71"), ("6", "#f1c40f"), ("*", "#c0392b"),
    ("1", "#16a085"), ("2", "#27ae60"), ("3", "#f39c12"), ("-", "#8e44ad"),
    ("0", "#2980b9"), (".", "#7f8c8d"), ("=", "#2ecc71"), ("+", "#d35400"),
]

row = 0
col = 0

for (text, color) in buttons:
    if text == "=":
        cmd = calculate
    else:
        cmd = lambda t=text: click(t)

    Button(
        frame,
        text=text,
        width=8,
        height=3,
        bg=color,
        fg="white",
        font=("Arial", 16, "bold"),
        activebackground="white",
        command=cmd
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

Button(
    root,
    text="C",
    bg="red",
    fg="white",
    font=("Arial", 16, "bold"),
    command=clear
).pack(fill="x", padx=20, pady=15)

root.mainloop()