from tkinter import *



app = Tk() 
app.title("App") 
app.geometry("400x300")

t = Message(app,text="Este é um texto Message", width=100)
t.pack()

app.mainloop() # loop

