from tkinter import *
from tkinter import ttk


window = Tk()
window.title("lesson 18")
window.geometry("600x500")
window.config(bg="#ffec3f")



lab_text = Label()
lab_text.place(x=30 , y=150)

def fun_s(event):
    lab_text.config(text=event)



scale_n1 = ttk. Scale(orient=HORIZONTAL ,   command=fun_s , length=200 , from_=0 , to=10 )
scale_n1.place(x=220 , y=140)



scale_n2 = ttk.Scale(orient= VERTICAL, command=fun_s , length=200 , from_=0 , to=10 , value=3)
scale_n2.place(x=310 , y=50)



def fun_b():
       but.config(text= scale_n1.get())
but = Button(text="ровно", command=fun_b)
but.place(x=40,y=10)








window.mainloop()