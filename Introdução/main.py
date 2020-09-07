# https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956
from tkinter import *
import os

caminho = os.path.dirname(__file__)
nome_arquivo = caminho+"\\nomes.txt"

def gravar_dados():
    arquivo = open(nome_arquivo,'a')
    arquivo.write(f'Nome: {nome.get()}')
    arquivo.write(f'\nTelefone: {telefone.get()}')
    arquivo.write(f'\nE-mail: {email.get()}')
    arquivo.write(f'\nOBS: {obs.get("1.0",END)}')
    arquivo.write('\n\n')
    arquivo.close()

app = Tk() 

# Configuração da janela
app.title('Curso de Tkinter')
app.geometry('500x300')
app.configure(bg='#dde')
# Fim da janela

# Componentes

# anchor --> N=Norte , S=Sul , E=Leste , W=Oeste
Label(app,text='Nome',bg='#dde',fg='#009',anchor=W).place(x=10,y=10,width=100,height=20)

nome = Entry(app) # Entry --> caixa de texto
nome.place(x=10,y=30,width=200,height=20)

Label(app,text='Telefone',bg='#dde',fg='#009',anchor=W).place(x=10,y=60,width=100,height=20)
telefone = Entry(app)
telefone.place(x=10,y=80,width=100,height=20)

Label(app,text='E-mail',bg='#dde',fg='#009',anchor=W).place(x=10,y=110,width=100,height=20)
email = Entry(app)
email.place(x=10,y=130,width=300,height=20)

Label(app,text='OBS',bg='#dde',fg='#009',anchor=W).place(x=10,y=160,width=100,height=20)
obs = Text(app) #  Text  --> Caixa de texto de várias linhas
obs.place(x=10,y=180,width=300,height=80)

# Botão
Button(app,text='Imprimir Dados',command=gravar_dados).place(x=10,y=270,width=100,height=20)


app.mainloop()

