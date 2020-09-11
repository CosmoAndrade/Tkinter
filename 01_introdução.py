from tkinter import *

app = Tk() # Janela

app.title('App') # Título

app.geometry('500x300+200+200') # Tamanho da janela

app.resizable(False,False) # Janela Fixa

app.iconbitmap("icon.ico")



# app.minsize(500,300) # Tamanho mínimo
# app.maxsize(700,250) # Tamanho Máximo

app.mainloop() # loop da janela