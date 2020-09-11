from tkinter import *

def ver_valor(v):
    print (v)

def ver_valor():
    print (slide.get())

app = Tk() 
app.title("App") 
app.geometry(300x200)

slide = Scale(app,from_=0,to=100,orient=HORIZONTAL,resolution=0.5,command=ver_valor)
slide.pack()


app.mainloop() # loop

