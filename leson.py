from tkinter import *


window = Tk()
window.title("lesson 18")
window.geometry("600x500")
window.config(bg="#ffec3f")

# зафиксировать размер окна
# window.resizable(False,False)

# минимальный размер окна
window.minsize(300,250)

# максимальный размер окна
window.maxsize(800,650)



# anchor позиционирование относительно окна
lab_text_1 = Label(text="текст" , font=("Arial Black" , 15) , fg="#83568d" , bg="#eaae2c")
lab_text_1.place(anchor="center" , relx=0.5 , rely=0.5)


lab_text_2 = Label(text="текст22" , font=("Arial Black" , 15) , fg="#fffb0a" , bg="#3c2cea")
lab_text_2.place(anchor="center" , relx=0.5 , rely=0.41)



def fun():
    # получаем ширину, высоту и координаты окна
    print(window.geometry())
    lab_text_2.config(text = window.geometry())
but_1 = Button(text="run" , command=fun ,  font=("Arial Black" , 15))
but_1.place(x=30 , y=80)






window.mainloop()