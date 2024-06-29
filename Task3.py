import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to get the password length and display the password
def display_password():
    try:
        length = int(entry.get())
        if length < 1:
            raise ValueError
        password = generate_password(length)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid positive integer.")

# Application Window
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x200")

# Add widgets
tk.Label(app, text="Enter the desired length of the password:").pack(pady=10)
entry = tk.Entry(app)
entry.pack(pady=5)

generate_button = tk.Button(app, text="Generate Password", command=display_password)
generate_button.pack(pady=20)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)

# Run the application
app.mainloop()
