import tkinter as tk

# Function to perform calculations
def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to append characters to the input field
def append_character(character):
    current_text = entry.get()
    if current_text == "0" and character != ".":
        entry.delete(0, tk.END)
    entry.insert(tk.END, character)

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)
    entry.insert(tk.END, "0")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create and configure the entry field
entry = tk.Entry(root, font=("Helvetica", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4)
entry.insert(0, "0")

# Create and configure the number and operator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val, col_val = 1, 0
for button_text in buttons:
    tk.Button(root, text=button_text, padx=20, pady=20, font=("Helvetica", 16),
              command=lambda char=button_text: append_character(char) if char != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Add a Clear button
clear_button = tk.Button(root, text="Clear", padx=20, pady=20, font=("Helvetica", 16), command=clear)
clear_button.grid(row=row_val, column=col_val)

# Start the Tkinter main loop
root.mainloop()
