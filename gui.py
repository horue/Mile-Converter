import tkinter as tk


def convert(e1):
    pass


def m(root):
    e1 = tk.Entry(root)
    e1.pack()

    b1 = tk.Button(root, text='Convert', command=lambda:convert(e1))
    b1.pack()


def main():
    root = tk.Tk()
    root.title("Mile Converter")
    root.geometry('250x100')
    root.resizable(False, False)
                
    m(root)

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

main()
