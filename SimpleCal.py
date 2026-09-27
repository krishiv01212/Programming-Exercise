"""
Problem:
Make a simple calculator in python
"""

import tkinter as tk

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

window = tk.Tk()
window.title("Calculator")

entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

row = 1
col = 0

for button in buttons:
    if button == "C":
        command = clear
    elif button == "=":
        command = calculate
    else:
        command = lambda x=button: click(x)

    tk.Button(window, text=button, width=5, height=2,
              command=command).grid(row=row, column=col)

    col += 1
    if col == 4:
        col = 0
        row += 1

window.mainloop()
