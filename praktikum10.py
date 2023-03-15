import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("CobaRadioButton")
window.geometry('600x300')

#Membuat Radio Button
Radiob1 = Radiobutton(window, text="Teknik informatika", value=1).pack()
Radiob2 = Radiobutton(window, text="Sistem informasi", value=2).pack()

window.mainloop()
