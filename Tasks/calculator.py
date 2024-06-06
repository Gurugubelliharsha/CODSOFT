import tkinter as tk
def update_display(value):
    current = display_var.get()
    if current == "0":
        display_var.set(value)
    else:
        display_var.set(current + value)
def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except Exception as e:
        display_var.set("Error")
def clear():
    display_var.set("0")
def delete_last():
    current = display_var.get()
    if len(current) > 0:
        display_var.set(current[:-1])

        
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="black")
display_var = tk.StringVar()
display_var.set("0")
display = tk.Label(root, textvariable=display_var, anchor="e", font=("Helvetica", 20), bg="gray25", fg="white", bd=5, height=2)
display.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=5)
buttons = [
    ("C", 1, 0), ("%", 1, 1), ("←", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("00", 5, 0), ("0", 5, 1), (".", 5, 2),("=", 5, 3),
]
for (text, row, col) in buttons:
    if text in ("/", "*", "-", "+","%"):
        btn = tk.Button(root, text=text, command=lambda t=text: update_display(t), bg="grey", fg="white", font=("Helvetica", 18))
    elif text == "=":
        btn = tk.Button(root, text=text, command=calculate, bg="silver", fg="black", font=("Helvetica", 18))
    elif text == "C":
        btn = tk.Button(root, text=text, command=clear, bg="orange", fg="black", font=("Helvetica", 18))
    elif text == "←":
        btn = tk.Button(root, text=text, command=delete_last, bg="dark cyan", fg="white", font=("Helvetica", 18))
    else:
        btn = tk.Button(root, text=text, command=lambda t=text: update_display(t), bg="black", fg="white", font=("Helvetica", 18))
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
for i in range(6):
    root.grid_rowconfigure(i, weight=2)
for i in range(4):
    root.grid_columnconfigure(i, weight=2)

root.mainloop()





