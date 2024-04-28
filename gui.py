import tkinter as tk
from tkinter import *


def convert(e1, l1):
    miles = e1.get()
    final = float(miles) * 1.6
    print(final)

    l1.config(text=final)

def m(root):
    l2 = tk.Label(root, text="Mile Converter")
    l2.pack(pady=10)

    e1 = tk.Entry(root)
    e1.pack(pady=10)

    l1 = tk.Label(root, text="No value converted yet.")
    l1.pack()

    b1 = tk.Button(root, text='Convert', command=lambda:convert(e1,l1))
    b1.pack(pady=10)





def main():
    root = tk.Tk()
    root.title("Mile Converter")
    root.geometry('350x200')
    root.resizable(False, False)
                
    m(root)

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

main()
