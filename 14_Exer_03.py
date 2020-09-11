from tkinter import *

app = Tk()
app.title('App')

frame_nome = Frame(app)
frame_morada = Frame(app)
frame_nome.grid(row=0,column=0)
frame_morada.grid(row=0,column=1)

label_nome = Label(frame_nome,text='Nome: ')
label_apelido = Label(frame_nome,text='Apelido:')
label_rua = Label(frame_morada,text='Rua: ')
label_cidade = Label(frame_morada,text='Cidade: ')

text_nome = Entry(frame_nome)
text_apelido = Entry(frame_nome)
text_rua = Entry(frame_morada)
text_cidade = Entry(frame_morada)

btn_salvar = Button(app,text='Salvar')

label_nome.grid(row=0,column=0)
label_apelido.grid(row=1,column=1)
text_nome.grid(row=0,column=1)
text_apelido.grid(row=1,column=1)

label_rua.grid(row=0,column=0)
label_cidade.grid(row=1,column=0)
text_rua.grid(row=0,column=1)
text_cidade.grid(row=1,column=1)

btn_salvar.grid()



app.mainloop()