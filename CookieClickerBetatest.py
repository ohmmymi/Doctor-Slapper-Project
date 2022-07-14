from tkinter import *
from playsound import playsound
from PIL import Image,ImageTk
import sys
from tkinter import Tk, simpledialog, messagebox

window = Tk()

point = 100

spoint = str(point)

#ฟังก์ชันปุ่มดอกเตอร์
def click():
    button.config(image=photo2)
    playsound('slap.mp3')
    global point
    point+=1
    label2.config(text=point)
    if point %2 ==0:
        button.config(image=photo)
    else:
        button.config(image=photo2)

icon = PhotoImage(file = r"slapico.png")
window.title("DoctorSlapper")

window.geometry('1000x800')
window.resizable(0,0) #ล็อกขนาด window
load = Image.open('bg.png')
render = ImageTk.PhotoImage(load)
img = Label(window, image = render)
img.place(x=0,y=0)

#bgimg= PhotoImage(file = "bg.png")
#limg= Label(window, i=bgimg)
#limg.pack()


#ปุ่ม
photo = PhotoImage(file = r"bgndoctor.png")
photo2 = PhotoImage(file = r"bgsdoctor.png")
button = Button(window, text='Click me',bd=0)
button.config(command=click, image=photo)
button.pack()

#label
label = Label(window, text="Your score")
label.config(font=('Monospace',25),bg="#e86c39")
label.pack()
#label คะแนน
label2 = Label(window, text=point)
label2.config(font=('Monospace',100),bg="#e86c39")
label2.pack()
    
def read_from_file():
    with open('userdata.txt', 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            user, score = line.split('/')
            user = user.capitalize()
            score = score.capitalize()
            userscore[user] = score

def write_to_file(user_name, score_name):
    with open('userdata.txt', 'a') as file:
        file.write('\n')
        file.write(user_name + '/' + score_name)
        file.close()

        
###############################################################################
        
root = Tk()
root.withdraw()
userscore = {}


while True:
    read_from_file()
    simpledialog.askstring
    user_name_score = ''
    
    user_name_score = simpledialog.askstring('name', 'What is your name : ')
    user_name_score = user_name_score.capitalize()
    if user_name_score in userscore:
        result = userscore[user_name_score]
        messagebox.showinfo('doctor slapper','Your old score : ' + user_name_score + ' is ' + result + '!')
        messagebox.showinfo(f'Your new score is : {point}' )
        new_score = spoint
        write_to_file(user_name_score, new_score)
    else:
        messagebox.showinfo('doctor slapper', 'You are a new player. '+ user_name_score )
        messagebox.showinfo('doctor slapper','Thanks you playing game. You create new user!')
        messagebox.showinfo(f'Your score is : {point} ' )
        new_score = spoint
        write_to_file(user_name_score, new_score)
    answer = simpledialog.askstring('docter slapper', 'Do you want to play again? y/n: ')
    if answer == 'n':
        messagebox.showinfo('docter slapper','Thanks you for playing game!')
        root.destroy()
        sys.exit()
window.mainloop()

