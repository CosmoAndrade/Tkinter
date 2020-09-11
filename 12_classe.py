from tkinter import *

# Criação do Widget
class FrameNome(Frame):
  def __init__(self,master):
    super().__init__()
    self['height'] = 150
    self['width'] = 200
    self['bd'] = 2
    self['relief'] = 'solid'


    label_nome = Label(self,text='Nome:')
    text_nome = Entry(self)
    label_nome.grid(row=0,column=0)
    text_nome.grid(row=0,column=1)



app = Tk()
app.title('Widget')

frame1 = FrameNome(app).grid()
frame1 = FrameNome(app).grid()

app.mainloop()