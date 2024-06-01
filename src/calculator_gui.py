import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator by Lizzy & Rohaan")

        self.entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
        self.entry.grid(row=0, column=0, columnspan=5)

        # C is for clear everything in the entry field
        buttons = [
            '7', '8', '9', '/', 'sin',
            '4', '5', '6', '*', 'cos',
            '1', '2', '3', '-', 'tan',
            '0', '.', '=', '+', 'log',
            'C'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            b = tk.Button(root, text=button, width=5, height=2, command=action)
            b.grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.entry.delete(0, tk.END)
        elif char in ['sin', 'cos', 'tan', 'log']:
            try:
                expression = self.entry.get()
                if char == 'sin':
                    result = math.degrees(math.sin(math.radians(float(expression))))
                elif char == 'cos':
                    result = math.degrees(math.cos(math.radians(float(expression))))
                elif char == 'tan':
                    result = math.degrees(math.tan(math.radians(float(expression))))
                elif char == 'log':
                    result = math.log10(float(expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.entry.delete(0, tk.END)
        elif char == 'C':
            self.entry.delete(0, tk.END)
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + char)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
