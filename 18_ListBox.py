from tkinter import *

def Executar():
    print(lista.get(ACTIVE))
    

app = Tk() 
app.title("App") 

lista = Listbox(app)
lista.pack()

# inserir um item de cada vez
#lista.insert(0,"Primeiro")
#lista.insert(1,"Segundo")

# END - sempre coloca no fim da lista
lista.insert(END,"Primeiro")
lista.insert(END,"Segundo")

# varios itens

nomes = ["Davi", "Felipe","Lucas"]

for nome in nomes:
    lista.insert(END,nome)


btn = Button(app,text="Clique",command=Executar).pack()


app.mainloop() # loop

