from tkinter import *

def Executar():
    print (s3.get())

app = Tk()
app.geometry('300x200')


s1 = Spinbox(app,from_=0,to=10)
s1.pack()

s2 = Spinbox(app,values=(10,20,30,40,50), wrap=True)
s2.pack()

s3 = Spinbox(app,values=('João','Felipe','Lucas'))
s3.pack()

btn = Button(app,text='Clique',command=Executar)
btn.pack()



app.mainloop()