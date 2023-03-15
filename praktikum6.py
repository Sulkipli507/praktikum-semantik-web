import tkinter

window = tkinter.Tk()
window.title("Cobalabel")
window.geometry('600x100')

#Membuat label
label1 = tkinter.Label(window, text="My frist text", font=15, bg="green", fg="white").pack()
label2 = tkinter.Label(window, text="Universitas sulawesi barat", font=15).pack()

window.mainloop()
