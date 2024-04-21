import tkinter as tk


def convert(e1):
    miles = e1.get()
    final = float(miles) * 1.6
    print(final)


def m(root):
    e1 = tk.Entry(root)
    e1.pack()

    b1 = tk.Button(root, text='Convert', command=lambda:convert(e1))
    b1.pack()

    l1 = tk.Label(root)
    l1.pack()


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
