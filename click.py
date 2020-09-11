from tkinter import *

def click():
    print (t1.get())

app = Tk()
app.title('App')

t1 = Entry(app)
t1.grid()

btn = Button(app,text='click',command=click)
btn.grid()



app.mainloop()