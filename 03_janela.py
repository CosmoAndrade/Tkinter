# Posicionar a janela no centro

from tkinter import *

app = Tk()
app.title('Formulário')

# Dimensões da janela

largura = 500
altura = 300

# resolução do sistema

largura_janela = app.winfo_screenwidth()
altura_janela = app.winfo_screenheight()
print (largura_janela,altura_janela)

# Posição da janela

pos_x = largura_janela/2 - largura/2
pos_y = altura_janela/2 - altura/2

# Geometry

# Janela no centro
app.geometry('%dx%d+%d+%d' % (largura,altura,pos_x,pos_y))

app.mainloop()

