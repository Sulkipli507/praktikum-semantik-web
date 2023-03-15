import tkinter
window = tkinter.Tk()
window.title("CobaButton")
window.geometry('600x300')

#Membuat button
tombol1 = tkinter.Button(window, text="Home").pack()
tombol2 = tkinter.Button(window, text="Informasi").pack()

window.mainloop()