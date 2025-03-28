# import GUI- graphical user interface
import tkinter as tk

#created buttons for input,clear and equal
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        
#created window for calculator
window = tk.Tk()
window.title("Calculator")
window.configure(bg="Lightgrey")

#Define the Dimensions of the window
entry = tk.Entry(window, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#created number buttons
button_1 = tk.Button(window, text="1", padx=42, pady=19, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=42, pady=19, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=47, pady=19, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=42, pady=19, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=42, pady=19, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=47, pady=19, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=42, pady=19, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=42, pady=19, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=47, pady=19, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=42, pady=19, command=lambda: button_click(0))
button_add = tk.Button(window, text="+", padx=42, pady=19, command=lambda: button_click("+"))
button_subtract = tk.Button(window, text="-", padx=42, pady=15, command=lambda: button_click("-"))
button_multiply = tk.Button(window, text="*", padx=44, pady=15, command=lambda: button_click("*"))
button_divide = tk.Button(window, text="/", padx=47, pady=15, command=lambda: button_click("/"))
button_equal = tk.Button(window, text="=", padx=91, pady=17, command=button_equal)
button_clear = tk.Button(window, text="Clear", padx=36, pady=19, command=button_clear)

#deine the sizes of the buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=2)
button_add.grid(row=4, column=1)
button_equal.grid(row=6, column=0, columnspan=2)
button_subtract.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)

window.mainloop()
