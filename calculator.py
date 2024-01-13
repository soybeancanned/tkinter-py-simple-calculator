import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Calculator")
window.geometry("600x700")

s = ttk.Style()
s.configure("ButtonFrame.TFrame", background="#E0F4FF")
s.configure("calculation_frame.TFrame", background="#EEF5FF")

calculation_frame = ttk.Frame(window, style="calculation_frame.TFrame", padding="5 0 10 10")
button_frame = ttk.Frame(window, style="ButtonFrame.TFrame", padding="5 10 5 5")

calculation_frame.place(relx=0, rely=0, relwidth=1, relheight=0.20)
button_frame.place(relx=0, rely=0.20, relwidth=1, relheight=0.80)
calculation_frame.grid_rowconfigure(0, weight=1)
calculation_frame.grid_columnconfigure(0, weight=1)
calculation_frame.grid_rowconfigure(1, weight=2)
calculation_frame.grid_columnconfigure(0, weight=1)

button_frame.grid_rowconfigure(4, weight=1)
button_frame.grid_columnconfigure(0, weight=1)

Label = ttk.Label(calculation_frame, font=('Arial', 13), background="#E0F4FF", width=25, anchor="e")
Label.grid(sticky="nse", row=0, column=0)

entry = ttk.Entry(calculation_frame, font=('Arial', 35), justify='right')
entry.grid(sticky="nsew", row=1)

result = ""

def check_operations():
    updated_expression = entry.get()
    if "x" in updated_expression:
        updated_expression = updated_expression.replace("x", "*")
    if "÷" in updated_expression:
        updated_expression = updated_expression.replace("÷", "/")
    if "^" in updated_expression:
        updated_expression = updated_expression.replace("^", "**")
    if "−" in updated_expression:
        updated_expression = updated_expression.replace("−", "-")    
    return updated_expression
def button_click(expression):
    entry.insert(tk.END, expression)

def show_mini_label():
    show_text = entry.get()
    Label.config(text=show_text)
    
def calculate():
    try:
        show_mini_label()
        evaluate = check_operations()
        entry.delete(0, tk.END)  
        result = str(eval(evaluate))
        entry.insert(tk.END, result)       
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def delete():
    deleted = entry.get()
    deleted = deleted[:-1]
    entry.delete(0, tk.END)
    entry.insert(tk.END, deleted)

def clear():
    entry.delete(0, tk.END)

Button_clear_all = ttk.Button(button_frame, text="^",command=lambda:button_click("^")).grid(column=0, row=0, sticky="nsew")
Button_clear_number = ttk.Button(button_frame, text="C", command= clear).grid(column=1, row=0, sticky="nsew")
Button_delete_number = ttk.Button(button_frame, text="del", command= delete).grid(column=2, row=0, sticky="nsew")
Button_positive_negative = ttk.Button(button_frame, text="(-)", command=lambda:button_click("-")).grid(column=0, row=4, sticky="nsew")
Button_decimal = ttk.Button(button_frame, text=".", command=lambda:button_click(".")).grid(column=2, row=4, sticky="nsew")
Button_equal = ttk.Button(button_frame, text="=", command = calculate).grid(column=3, row=4, sticky="nsew")
Button_division = ttk.Button(button_frame, text="÷", command=lambda:button_click(" ÷ ")).grid(column=3, row=0, sticky="nsew")
Button_times = ttk.Button(button_frame, text="x", command=lambda:button_click(" x ")).grid(column=3, row=1, sticky="nsew")
Button_minus = ttk.Button(button_frame, text="−", command=lambda:button_click(" - ")).grid(column=3, row=2, sticky="nsew")
Button_add = ttk.Button(button_frame, text="+", command=lambda:button_click(" + ")).grid(column=3, row=3, sticky="nsew")

Button_0 = ttk.Button(button_frame, text="0", command=lambda:button_click(0)).grid(column=1, row=4, sticky="nsew")
Button_1 = ttk.Button(button_frame, text="1", command=lambda:button_click(1)).grid(column=0, row=3, sticky="nsew")
Button_2 = ttk.Button(button_frame, text="2", command=lambda:button_click(2)).grid(column=1, row=3, sticky="nsew")
Button_3 = ttk.Button(button_frame, text="3", command=lambda:button_click(3)).grid(column=2, row=3, sticky="nsew")
Button_4 = ttk.Button(button_frame, text="4", command=lambda:button_click(4)).grid(column=0, row=2, sticky="nsew")
Button_5 = ttk.Button(button_frame, text="5", command=lambda:button_click(5)).grid(column=1, row=2, sticky="nsew")
Button_6 = ttk.Button(button_frame, text="6", command=lambda:button_click(6)).grid(column=2, row=2, sticky="nsew")
Button_7 = ttk.Button(button_frame, text="7", command=lambda:button_click(7)).grid(column=0, row=1, sticky="nsew")
Button_8 = ttk.Button(button_frame, text="8", command=lambda:button_click(8)).grid(column=1, row=1, sticky="nsew")
Button_9 = ttk.Button(button_frame, text="9", command=lambda:button_click(9)).grid(column=2, row=1, sticky="nsew")

for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)
   
window.mainloop()
