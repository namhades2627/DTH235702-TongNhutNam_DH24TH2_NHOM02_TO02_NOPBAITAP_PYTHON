from tkinter import *
from tkinter.ttk import *

window = Tk()
 
window.title('Lap trinh Tkinter')
window.geometry('350x200')

chk_state = BooleanVar()
chk_state.set(True)
check = Checkbutton(window, text = 'Chọn', var = chk_state)

check.grid(column=0, row=0)

window.mainloop()