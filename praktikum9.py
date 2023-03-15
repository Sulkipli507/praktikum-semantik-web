import tkinter

window = tkinter.Tk()
window.title("CobaEntry")
window.title('600x300')

#Membuat Entry
Entry1 = tkinter.Entry(window, bg="green", fg="white").pack()
Entry2 = tkinter.Entry(window).pack

window.mainloop()
