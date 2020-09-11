from tkinter import *

app = Tk() 
app.title("App") 
app.geometry("500x300")  

# Grid 

lab1 = Label(app,text= 'Label 1', bg='gold',font='Courier 20')

lab2 = Label(app,text= 'Label 2', bg='Magenta',font='Courier 20')

lab3 = Label(app,text= 'Label 3', bg='Magenta',font='Courier 20')


#lab1.pack()
#lab2.pack()

# row - linha , column - colunas
lab1.grid(row=0,column=0)
lab2.grid(row=0,column=1)
lab3.grid(row=0,column=2)

btn1 = Button(app,text='Click')
btn2 = Button(app,text='Click')
btn3 = Button(app,text='Click')

btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)


app.mainloop() # loop

