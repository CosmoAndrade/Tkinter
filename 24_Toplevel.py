from tkinter import *

app = Tk()
app.title('App')
app.geometry('300x200')


def abrir_form():
    top = Toplevel()
    top.title('Top')
    top.geometry('200x100')
    lab = Label(top,text='Nova janela')
    lab.pack()

btn = Button(app,text='Novo',command=abrir_form)
btn.pack()


app.mainloop()