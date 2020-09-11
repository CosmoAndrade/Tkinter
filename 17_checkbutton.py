from tkinter import *

def Executar():
    print (valor_check.get())

app = Tk() 
app.title("App") 

valor_check = IntVar()
check = Checkbutton(app,text="CheckBox", variable=valor_check, command="Executar")
check.pack()




app.mainloop() # loop

