from tkinter import *
root=Tk()
root.title('Hello world')
canvas=Canvas(root,height=200,width=300)
canvas.pack()

frame=Frame(root,bg="black")
frame.place(relx=0.1,rely=0.1,relheight=0.8,relwidth=0.8)

text1=Label(frame,text="Hello" ,fg='red')
text1.pack()
button1=Button(frame,text='new button', bg='purple')
button1.pack()
root.mainloop()





