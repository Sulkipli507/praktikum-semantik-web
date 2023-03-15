import tkinter
from tkinter import messagebox
window = tkinter.Tk()
window.title("CobaMessageBox")
window.geometry('600x300')

#Membuat Message Box
def clicked():
    messagebox.showinfo('Coba Message', 'Terima kasih')
btn = tkinter.Button(window, text="tekan", command=clicked).pack()

window.mainloop()