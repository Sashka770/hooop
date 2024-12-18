from tkinter import *


window = Tk()
window.title("calkylator")
window.geometry("600x500")
window.config(bg="#dcff3f")



ent_inp = Entry(font=("Arial Black" , 10) ,bg="#0a008f" ,fg="#faa8a8" , width=20 )
ent_inp.place(x=30 , y=30)



def fun():
    print(ent_inp.get())

    ent_inp.delete
but_1 = Button(text="-" , command=fun ,  font=("Arial Black" , 15))
but_1.place(x=30 , y=140)

lab_text = Label(text="число" , font=("Arial Black" , 15) , fg="#0afff3" , bg="#ea2c65")
lab_text.place(x=40 , y=100)




def fun_2():
    ent_inp.delete()
but_2 = Button(text="+" , command=fun_2 ,  font=("Arial Black" , 15))
but_2.place(x=40 , y=200)



def fun_3():
    ent_inp.delete()
but_3 = Button(text="=" , command=fun_3 ,  font=("Arial Black" , 15))
but_3.place(x=40 , y=300)


window.mainloop()