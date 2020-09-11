from tkinter import *
# Funções 
# C = (F-32) * 5/9

def calcular():
    F = float(text_box1.get())
    C = (F-32)*5/9
    final.set (str(round(C,2)) + 'Graus Celsius')


# GUI
app = Tk()
app.title('Fahrenheit / Celsius')
final = StringVar()

# Widgets
label1 = Label(app,text='Fahrenheit:')
text_box1 = Entry(app)
btn_1 = Button(app,text='Calcular',command=calcular)
label_resultado = Label(app,textvariable=final)

# Layout

label1.grid()
text_box1.grid()
btn_1.grid()
label_resultado.grid()


app.mainloop()