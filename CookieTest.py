from tkinter import *
from playsound import playsound
window = Tk()

point = 0

#ฟังก์ชันปุ่มดอกเตอร์
def click():
    button.config(image=photo2)
    playsound('slap.mp3')
    global point
    point+=1
    label.config(text=point)
    if point %2 ==0:
        button.config(image=photo)
    else:
        button.config(image=photo2)

        


window.geometry('1000x800')
window.resizable(0,0) #ล็อกขนาด window

#ปุ่ม
photo = PhotoImage(file = r"ndoctor.png")
photo2 = PhotoImage(file = r"hdoctor.png")
button = Button(window, text='Click me')
button.config(command=click, image=photo)
button.pack()

#label คะแนน
label = Label(window, text=point)
label.config(font=('Monospace',50))
label.pack()
    

window.mainloop()



