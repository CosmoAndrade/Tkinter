from tkinter import *

class MinhaFrame(Frame):
    def __init__(self,janela):
        super().__init__()
        self['height'] = 200
        self['width'] = 400
        self['bg'] = 'gold'


app = Tk()

fram1 = MinhaFrame(app).pack()

app.mainloop()
