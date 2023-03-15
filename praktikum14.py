import tkinter
from tkinter import Scale

window = tkinter.Tk()
window.title("CobaScale")
window.geometry('600x300')

#Membuat Scale
Scale = Scale(length=100, from_=0, to=10)
Scale.get()
Scale.pack()

window.mainloop()
