from tkinter import *

# GUI
app = Tk()
app.title('Frame')

# Widgets

frame_login = Frame(app)

label_usuario = Label(frame_login,text='Usuário: ')
label_password = Label(frame_login,text='Password: ')
text_usuario = Entry(frame_login)
text_password = Entry(frame_login)
btn_entrar = Button(frame_login,text='Entrar')


# Layout

label_usuario.grid(row=0,column=0)
label_password.grid(row=1,column=0)
text_usuario.grid(row=0 ,column=1)
text_password.grid(row=1 ,column=1)
btn_entrar.grid(row=2 ,column=1)

frame_login.grid()



app.mainloop()


