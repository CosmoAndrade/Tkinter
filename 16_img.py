from tkinter import *



app = Tk() 
app.title("App") 

img = PhotoImage(file="img.png")

label_img = Label(app,image=img).pack()






app.mainloop() # loop

