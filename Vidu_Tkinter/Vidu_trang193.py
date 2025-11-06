from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Lap trinh Tkinter')
window.geometry('400x400')

def clicked():
    messagebox.showinfo('Hien thi thong bao', 'Xin chao ban')

btn = Button(window, text = 'Click here', command = clicked)
btn.grid(column=0, row=0)

window.mainloop()