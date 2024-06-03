import tkinter as tk
from logic import CalculatorLogic

class CalculatorGUI:
    def __init__(self, root):
        self.calc_logic = CalculatorLogic()
        self.root = root
        self.root.title("Calculator")

        # Initialize display
        self.display = tk.Entry(self.root, font=('Arial', 18), borderwidth=2, relief='solid')
        self.display.pack(fill=tk.BOTH, padx=5, pady=5)

        # Initialize current input
        self.current_input = ""

        # Create buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.BOTH, expand=True)

        buttons = [
            'sin', 'cos', 'tan', 'log',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', 'CE',  '+',
            '='
        ]

        rows = 6
        cols = 4

        for i, text in enumerate(buttons):
            button = tk.Button(button_frame, text=text, font=('Arial', 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=i // cols, column=i % cols, sticky=tk.W+tk.E+tk.N+tk.S, padx=5)

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.current_input)

    def on_button_click(self, char):
        if char in '0123456789':
            self.current_input += char
            self.update_display()
        elif char in '+-*/':
            self.current_input += char
            self.update_display()
        elif char == '=':
            try:
                self.evaluate_expression()
            except Exception as e:
                self.current_input = "Error"
                self.update_display()
                self.current_input = ""
        elif char == 'C':
            self.current_input = ""
            self.update_display()
        elif char == 'CE':
            self.current_input = self.current_input[:-1]
            self.update_display()
        elif char in ['sin', 'cos', 'tan', 'log']:
            try:
                self.evaluate_function(char)
            except Exception as e:
                self.current_input = "Error"
                self.update_display()
                self.current_input = ""

    def evaluate_expression(self):
        try:
            result = eval(self.current_input)
            self.current_input = str(result)
            self.update_display()
        except Exception as e:
            self.current_input = "Error"
            self.update_display()
            self.current_input = ""

    def evaluate_function(self, func):
        try:
            value = float(self.current_input)
            if func == 'sin':
                result = self.calc_logic.sine(value)
            elif func == 'cos':
                result = self.calc_logic.cosine(value)
            elif func == 'tan':
                result = self.calc_logic.tangent(value)
            elif func == 'log':
                result = self.calc_logic.log10(value)
            self.current_input = str(result)
            self.update_display()
        except Exception as e:
            self.current_input = "Error"
            self.update_display()
            self.current_input = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = CalculatorGUI(root)
    root.mainloop()


    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.current_input)

    def on_button_click(self, char):
        if char in '0123456789':
            self.current_input += char
            self.update_display()
        elif char in '+-*/':
            self.current_input += char
            self.update_display()
        elif char == '=':
            try:
                self.evaluate_expression()
            except Exception as e:
                self.current_input = "Error"
                self.update_display()
                self.current_input = ""
        elif char == 'C':
            self.current_input = ""
            self.update_display()
        elif char == 'CE':
            self.current_input = self.current_input[:-1]
            self.update_display()
        elif char in ['sin', 'cos', 'tan', 'log']:
            try:
                self.evaluate_function(char)
            except Exception as e:
                self.current_input = "Error"
                self.update_display()
                self.current_input = ""

    def evaluate_expression(self):
        try:
            result = eval(self.current_input)
            self.current_input = str(result)
            self.update_display()
        except Exception as e:
            self.current_input = "Error"
            self.update_display()
            self.current_input = ""

    def evaluate_function(self, func):
        try:
            value = float(self.current_input)
            if func == 'sin':
                result = self.calc_logic.sine(value)
            elif func == 'cos':
                result = self.calc_logic.cosine(value)
            elif func == 'tan':
                result = self.calc_logic.tangent(value)
            elif func == 'log':
                result = self.calc_logic.log10(value)
            self.current_input = str(result)
            self.update_display()
        except Exception as e:
            self.current_input = "Error"
            self.update_display()
            self.current_input = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = CalculatorGUI(root)
    root.mainloop()
