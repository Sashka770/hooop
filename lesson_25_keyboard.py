
from tkinter import *
from tkinter import ttk


window = Tk()
window.title("lesson 25")
window.geometry("900x500")
window.config(bg="#ffec3f")



lab_text = Label(text="text", font=("" , 15))
lab_text.place(x=10 , y=150)


def fun_press(event):
    # event - получаем информацию о обработчике (клавиша)
    # lab_text.config(text=event)

    # event.keysym - название клавиши
    # lab_text.config(text=event.keysym)

    # event.state - информация о дополнительно зажатых клавиш
    lab_text.config(text=event.state)
    if(event.keysym =="w"):
        window.config(bg="#08cd7b")
    if(event.keysym =="w" and event.state == 12):
        window.config(bg="#cd0808")
    # if(event.keysym =="W" and event.state == 9):
    #     window.config(bg="#af08cd")
    if(event.keysym =="n"):
        window.config(bg="#cd9208")

# обработчик нажатия клавиши клавиатуры 
window.bind("<KeyPress>" , fun_press)


def fun_release(event):
    lab_text.config(text=event)
    if(event.keysym =="w"):
        window.config(bg="#0d5839")
    if(event.keysym =="w" and event.state == 12):
        window.config(bg="#600b0b")

# обработчик отжатия клавиши клавиатуры
window.bind("<KeyRelease>" , fun_release)

window.mainloop()