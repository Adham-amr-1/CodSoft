import tkinter as tk
from tkinter import messagebox

def button_click(char):
    global expression
    if char == '=':
        calculate_result()
    elif char == 'C':
        clear_display()
    else:
        expression += str(char)
        display.delete(0, tk.END)
        display.insert(tk.END, expression)

def calculate_result():
    global expression
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
        expression = str(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        clear_display()

def clear_display():
    global expression
    expression = ""
    display.delete(0, tk.END)

def create_button(text, row, col):
    button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18),
                       command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, sticky="nsew")

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")

expression = ""

# Create display widget
display = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
display.grid(row=0, column=0, columnspan=4)

# Create buttons
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for text in button_texts:
    create_button(text, row_val, col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Make sure the buttons resize with the window
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
