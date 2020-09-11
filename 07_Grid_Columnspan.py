from tkinter import *


app = Tk()

Label (app,width=20,bg='gold').grid(column=0)
Label (app,width=20,bg= 'magenta').grid(column=1)
Label (app,width=20,bg= 'orange').grid(columnspan=2,sticky='we')


app.mainloop()