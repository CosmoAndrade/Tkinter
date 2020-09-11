from tkinter import *

def mostrar_nome():
    nome = text_box.get()
    label_final =Label(app,text='O seu nome é:' + nome)
    label_final.grid()

app = Tk()
app.title('App')
app.geometry('200x100')

lab = Label(app,text='Qual é o seu nome: ')
text_box = Entry(app)
btn = Button(app,text='Executar',command=mostrar_nome)

lab.grid()
text_box.grid()
btn.grid()


app.mainloop()