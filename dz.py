from tkinter import *
from tkinter import ttk


window = Tk()
window.title("lesson 25")
window.geometry("900x500")
window.config(bg="#ffec3f")



lab_text = Label(text="text", font=("" , 15))
lab_text.place(x=10 , y=150)



def fun_press(event):
   
    
    window.title(f"{event.x} , {event.y}")
window.bind("<Motion>" , fun_press)




def fun_1(event):
   
    lab_text.config(text=event)
window.bind ("<Button-4>",fun_1)


def fun_press(event):
    
    lab_text.config(text=event.state)
    if(event.keysym =="w"):
        window.config(bg="#08c6cd")
    if(event.keysym =="w" and "<Button-4>" event.state == 12):
        window.config(bg="#cd0808")
   
    if(event.keysym =="w"  and event.state == 12):
        window.config(bg="#cd9208")


window.bind("<KeyPress>" , fun_press)







window.mainloop()