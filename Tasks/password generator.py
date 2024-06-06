
import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password():
    length = int(length_entry.get())
    if length < 1:
        messagebox.showerror("Error", "Length must be at least 1")
        return
    characters = ''
    if include_letters.get():
        characters += string.ascii_letters
    if include_digits.get():
        characters += string.digits
    if include_specials.get():
        characters += string.punctuation
    if not characters:
        messagebox.showerror("Error", "At least one character set must be selected")
        return

    password = ''.join(random.choice(characters) for i in range(length))
    password_label.config(text="Generated Password: " + password, font=("Helvetica", 12,"bold"))

root = tk.Tk()
root.title("Password Generator")


length_label = tk.Label(root, text="Enter Password Length: ", fg='black', font=("Georgia", 12))
length_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
length_entry = tk.Entry(root, font=("Georgia", 12))
length_entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')

include_letters = tk.BooleanVar(value=True)
letters_check = tk.Checkbutton(root, text="Include Letters", variable=include_letters, fg='black', font=("Georgia", 12))
letters_check.grid(row=2, column=0, padx=10, pady=5, sticky='w')
include_digits = tk.BooleanVar(value=True)
digits_check = tk.Checkbutton(root, text="Include Digits", variable=include_digits, fg='black', font=("Georgia", 12))
digits_check.grid(row=3, column=0, padx=10, pady=5, sticky='w')
include_specials = tk.BooleanVar(value=True)
specials_check = tk.Checkbutton(root, text="Include Special Characters", variable=include_specials, fg='black', font=("Georgia", 12))
specials_check.grid(row=4, column=0, padx=10, pady=5, sticky='w')

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg='green', fg='white', font=("Georgia", 12, "bold"))
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='n')

password_label = tk.Label(root, text="Generated Password: ", fg='black', font=("Georgia", 12))
password_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky='w')


root.mainloop()
