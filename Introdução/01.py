from tkinter import *


app = Tk() # Criação da janela

app.title('App Tela') #  Titulo da janela

app.geometry('500x300') # Tamanho da janela

app.configure (bg='magenta') # cor da janela

# Label --> Caixa , bg -> Cor de fundo , fg -> cor do texto
txt1 = Label(app,text='Curso de Python',bg='gold',fg='black')
txt1.place(x=10,y=10,width=150,height=30)

texto = 'Curso de Python'
cor_de_fundo = 'orange'
cor_do_texto = 'black'
largura = 150
altura = 30

txt2 = Label(app,text = texto , bg=cor_de_fundo , fg=cor_do_texto)
txt2.place(x=50,y=50, width=largura,height=altura)



app.mainloop()

