import tkinter as tk


def m(root):
    pass


def main():
    root = tk.Tk()
    root.title("Mile Converter")
    root.geometry('400x300')
    root.resizable(False, False)
                
    m(root)

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

main()
