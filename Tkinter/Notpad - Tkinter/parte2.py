import tkinter


def NewFile():
    text_area.delete(1.0,"end")
   
   

def Save():
    container = text_area.get(1.0,"end")
    file = open("notepad.txt", "w")
    file.write(container)
    file.close()
    

def Abrir():
    file = open("notepad.txt")
    container = file.read()
    text_area.insert(1.0,container)
    
def UpdateFont():
    size = sping_size.get()
    font = spin_font.get()

    text_area.config(font='{} {}'.format(font,size))



window = tkinter.Tk()
window.title("Tk Notepad")
window.geometry("1280x720")
window.minsize(width=1280, height=720)


frame = tkinter.Frame(window,height=30)
frame.pack(fill="x")


font_text = tkinter.Label(frame ,text="  Font: ")
font_text.pack(side="left")

spin_font= tkinter.Spinbox(frame,values=("Arial" , "Verdana", "Consolas"))
spin_font.pack(side="left")

font_size = tkinter.Label(frame,text=" Font size:  ")
font_size.pack(side="left")

sping_size = tkinter.Spinbox(frame,from_=0,to=60)
sping_size.pack(side="left")

button_update = tkinter.Button(frame,text="UP", command=UpdateFont)
button_update.pack(side='left')



text_area = tkinter.Text(window, font="Verdana 20 ", width=1280,height=720 )
text_area.pack()

main_menu = tkinter.Menu(window)

file_menu = tkinter.Menu(main_menu,tearoff=0)
file_menu.add_command(label="New", command=NewFile)
file_menu.add_command(label="Abrir", command=Abrir)
file_menu.add_command(label="Salve", command=Save)
file_menu.add_command(label="Exit", command=window.quit)

main_menu.add_cascade(label="File", menu=file_menu)
window.configure(menu=main_menu)

window.mainloop()
