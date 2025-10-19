from tkinter import *
parent = Tk()
name = Label(parent, text = "Name").grid(row = 0, column = 0)
e1 = Entry(parent).grid(row = 0, column = 1)
password = Label(parent, text = "Password").grid(row = 1, column = 0)
e2 = Entry(parent).grid(row = 1, column = 1)
submit = Button(parent, text = "Submit").grid(row = 4, column = 0)
parent.mainloop()
"""from tkinter import *
root = Tk()
root.title("Thiet ke giao dien bang Tkinter")
root.resizable(height=True, width=True)
root.minsize(width=300, height=400)
def makecenter(root):
    root.update_idletasks()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    x = (root.winfo_screenwidth() // 2) - (root.width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.height() // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
makecenter(root)
root.mainloop()"""
root = Tk()
root.title("Thiet ke giao dien bang Tkinter")
root.resizable(height=True, width=True)
root.minsize(width=300, height=400)

def makecenter(root):
    root.update_idletasks()
    win_width = root.winfo_width()
    win_height = root.winfo_height()
    scr_width = root.winfo_screenwidth()
    scr_height = root.winfo_screenheight()
    x = (scr_width // 2) - (win_width // 2)
    y = (scr_height // 2) - (win_height // 2)
    root.geometry(f'{win_width}x{win_height}+{x}+{y}')

# Đặt kích thước cửa sổ trước khi căn giữa
root.geometry('300x400')
makecenter(root)
root.mainloop()
