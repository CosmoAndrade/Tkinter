from tkinter import *


app = Tk()
app.geometry('300x200')

def novo():
    print('Novo')

menu_app = Menu(app)

file_menu = Menu(menu_app,tearoff=0)
file_menu.add_command(label='Novo',command=novo)
file_menu.add_command(label='Abrir')
file_menu.add_command(label='Salvar')
menu_app.add_cascade(label='Arquivo',menu=file_menu)

file_edit = Menu(menu_app,tearoff=0)
file_edit.add_command(label='Copiar')
file_edit.add_command(label='Colar')
file_edit.add_command(label='Recortar')
menu_app.add_cascade(label='Editar',menu=file_edit)


app.config(menu=menu_app)


app.mainloop()