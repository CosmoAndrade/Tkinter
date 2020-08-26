import tkinter

class App:

    def __init__(self,title,x,y):

        window = tkinter.Tk()
        window.title(title)
        window.minsize(width=x,height=y)
        window.mainloop()


janela = App('Notepad', 360,640)

