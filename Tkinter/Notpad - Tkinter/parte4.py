import tkinter

class App:

    def __init__(self):

        self.valor = 20

        self.window = tkinter.Tk()
        self.window.title('Marcador')
        self.window.minsize(width=360,height=640)
        self.window.maxsize(width=360,height=640)

        self.text = tkinter.Label(self.window ,text=20,font='Courier 80 bold',pady=50)
        self.text.pack()

        self.frame = tkinter.Frame(self.window,bg='white')
        self.frame.pack()


        self.button_plus = tkinter.Button(self.frame,text='UP',bg='orange',width=20,command=self.plus)
        self.button_plus.pack(side='left')

        self.button_down = tkinter.Button(self.frame,text='Down',bg='orange',width=20,command=self.down)
        self.button_down.pack(side='left')


        self.window.mainloop()

    def plus(self):
        self.valor +=1
        self.text.config(text='{}'.format(self.valor))

    def down(self):
        self.valor -=1
        self.text.config(text='{}'.format(self.valor))
        

App()