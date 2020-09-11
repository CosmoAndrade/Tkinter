from tkinter import *

app = Tk()
app.title('Login')

Label(app,text='Usuário:').grid(row=0,sticky=W)# sticky -> posição
Label(app,text='Senha:').grid(row=1,sticky=W)

tex_usuario = Entry(app).grid(row=0,column=1)
tex_senha = Entry(app).grid(row=1,column=1)

btn_login = Button (app,text='Login').grid(row=2,column=1,sticky=E)

app.mainloop()

