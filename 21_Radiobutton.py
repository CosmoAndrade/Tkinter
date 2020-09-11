from tkinter import *



app = Tk()

valor_a  = IntVar()

def radio_1():
    print ('Opção 1')

rad_1 = Radiobutton(app,text='Opção A 1',variable=valor_a,value=1,indicatoron=0,command=radio_1)
rad_2 = Radiobutton(app,text='Opção A 2',variable=valor_a,value=2)
rad_3 = Radiobutton(app,text='Opção A 3',variable=valor_a,value=3)

rad_1.pack()
rad_2.pack()
rad_3.pack()

rad_1.select()


def ver_radio():
    print (valor_a.get())

btn = Button(app,text='Executar',command=ver_radio)
btn.pack()    

app.mainloop()