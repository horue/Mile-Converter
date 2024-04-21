import tkinter as tk


def m(root):
    pass


def main():
    root = tk.Tk()
    root.title("Mile Converter")
    root.resizable(True, True)
                
    m(root)

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

main()
