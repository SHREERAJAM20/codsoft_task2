import tkinter as tk


def click(symbol):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + symbol)


def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        result_label.config(text=" " + str(result))
    except Exception as e:
        result_label.config(text="Error")
        
    display.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, width=40, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=30, pady=10)

result_label = tk.Label(root, text="", padx=10, pady=10)
result_label.grid(row=1, column=0, columnspan=4)

buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
    ('C', 6, 0)  
]

for (text, row, column) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=10, command=calculate)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=20, pady=10, command=clear)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=10, command=lambda symbol=text:click(symbol))
    btn.grid(row=row, column=column, padx=5, pady=5)

root.mainloop()
