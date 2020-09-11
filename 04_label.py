from tkinter import *

app = Tk()
app.title('Label')
app.geometry('500x300')

# lab1 = Label(app,text='Label 1',bg='gold',fg='red',font='Courier')
# lab1.pack()

# lab2 = Label(app,text='Label 2',bg='blue',fg='white',font='Arial 20 bold italic')
# lab2.pack()

# lab3 = Label(app,text='Label 3',bg='green',fg='black',font='Verdana 42 bold ')
# lab3.pack()

# lab4 = Label(app,text='Label 4',bg='magenta',font='Helvetica',width=20,height=40)
# lab4.pack()

# Bordas
# lab5 = Label(app,text='solid',bg='#636e72',font='Consolas 30',bd=5,relief='solid')
# lab5.pack()

# lab6 = Label(app,text='flat',bg='#636e72',font='Consolas 30',bd=5,relief='flat')
# lab6.pack()

# lab7 = Label(app,text='raised',bg='#636e72',font='Consolas 30',bd=5,relief='raised')
# lab7.pack()

# lab8 = Label(app,text='sunken',bg='#636e72',font='Consolas 30',bd=5,relief='sunken')
# lab8.pack()

# lab9 = Label(app,text='ridge',bg='#636e72',font='Consolas 30',bd=5,relief='ridge')
# lab9.pack()

# lab10 = Label(app,text='groove',bg='#636e72',font='Consolas 30',bd=5,relief='groove')
# lab10.pack()
# Fim Bordas

# anchor --> N-Norte , S-Sul , E-Leste , W-Oeste , CENTER-Centro
# lab11 = Label(app,text='123456789',font='Courier 20',width=25,height=4,bd=3,relief='solid',anchor=W,)
# lab11.pack()

# Padding
# lab12 = Label(app,text='Padding',font='Courier 20',padx=50,pady=50 ,bd=3,relief='solid')
# lab12.pack()

# Definir e alterar propriedades
lab13 = Label(app,text='Frase Teste',font='Arial 20',bd=2,relief='solid')
lab13.pack()

lab14 = Label(app)
lab14['text'] = 'Texto da lab'
lab14['font'] = 'Courier'
lab14['bd'] = 3
lab14['relief'] = 'solid'
lab14.pack()



app.mainloop()