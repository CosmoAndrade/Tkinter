from tkinter import *

class MinhaFrame(Frame):
    def __init__(self,janela):
        super().__init__()

        

        self.text1 = StringVar()
        self.lab1 = StringVar()


        self.lab = Label(self,textvariable=self.lab1).grid()

        self.text = Entry(self,textvariable=self.text1).grid()

        btn = Button(self,text='Clique',command=self.Executar).grid()

    def Executar(self):
        self.lab1.set('Olá' + self.text1.get())

app = Tk()
app.geometry('300x150')
fram = MinhaFrame(app).grid()



app.mainloop()