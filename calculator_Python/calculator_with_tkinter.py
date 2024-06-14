import tkinter as tk

def calculate(operation, num1, num2):
    if operation == "+":
        return add(num1, num2)
    elif operation == "-":
        return subtract(num1, num2)
    elif operation == "*":
        return multiply(num1, num2)
    elif operation == "/":
        return divide(num1, num2)
    else:
        return "Invalid operation"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def display_result(result):
    result_text = str(result)  
    color = "green" if result >= 0 else "red"  
    result_label.config(text=result_text, fg=color)  

def button_click(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = calculate(operation, num1, num2)
        display_result(result)
    except ValueError:
        display_result("Invalid Input")

window = tk.Tk()
window.title("Colorful Calculator")
window.configure(bg="lightblue") 

label_font = ("Arial", 14, "bold")  
entry_font = ("Arial", 16)  

label1 = tk.Label(window, text="Number 1:", font=label_font)
label1.grid(row=0, column=0, sticky="W")

entry1 = tk.Entry(window, font=entry_font, width=10)
entry1.grid(row=0, column=1, padx=10)

label2 = tk.Label(window, text="Number 2:", font=label_font)
label2.grid(row=1, column=0, sticky="W")

entry2 = tk.Entry(window, font=entry_font, width=10)
entry2.grid(row=1, column=1, padx=10)

result_label = tk.Label(window, text="", font=("Arial", 18, "bold"))
result_label.grid(row=2, columnspan=2)
button_font = ("Arial", 14, "bold")  
button_width = 5  

button_add = tk.Button(window, text="+", font=button_font, width=button_width,
                       command=lambda: button_click("+"), bg="lightgreen")
button_add.grid(row=3, column=0)

button_subtract = tk.Button(window, text="-", font=button_font, width=button_width,
                       command=lambda: button_click("-"), bg="lightcoral")
button_subtract.grid(row=3, column=1)

button_multiply = tk.Button(window, text="*", font=button_font, width=button_width,
                       command=lambda: button_click("*"), bg="lightyellow")
button_multiply.grid(row=4, column=0)

button_divide = tk.Button(window, text="/", font=button_font, width=button_width,
                       command=lambda: button_click("/"), bg="lightblue")
button_divide.grid(row=4, column=1)

window.mainloop()
