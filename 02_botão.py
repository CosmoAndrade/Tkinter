from tkinter import *

# Botão

def btn_click():
    print ('Olá Mundo')

# def btn_click(msg):
#     print (msg)

app = Tk()
app.title('App')
app.geometry('500x300')
app ['bg'] = 'magenta'

# Botão

btn = Button(app,text='Executar',command=btn_click)
btn.pack()
                                           
# btn = Button(app,text='Executar',command=lambda: btn_click('Nova Mensagem'))
# btn.pack()

app.mainloop()