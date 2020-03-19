from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title('Image')
root.iconbitmap('icon.ico')

def display():
    check_value=check_control.get()
    value_label.config(text=str(check_value))

img=ImageTk.PhotoImage(Image.open("a.PNG"))
label=Label(image=img)
label.place(x=1,y=1,width=500,height=500)

check_control=IntVar()
Checkbutton(root,text="Click",variable=check_control,command=display).pack()

value_label=Label(root)
value_label.pack()

button=Button(root,text="Quit",command=root.quit)
button.pack()
root.mainloop()
