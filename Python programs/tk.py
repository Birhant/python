import tkinter as tk
import time


def alert():
    alert=tk.Toplevel(root)
    alert_canvas=tk.Canvas(alert,width=100,height=50)
    alert_canvas.pack()

def lab(i):
    label.config(text='%i' %i)


root=tk.Tk()
canvas=tk.Canvas(root,width=1000,height=500)
canvas.pack()
frame=tk.Frame(root,bg='black')
frame.place(relx=0,rely=0,relwidth=1,relheight=1)

ins="sdsd"
label=tk.Label(root,text='%str' %ins)
label.pack()
for i in range(10):
    label.after(1000,lambda:lab(i))
    label.update()

rbvar = tk.StringVar()
rbvar.set(" ")
rb1 = tk.Radiobutton(root, text="Option 1", variable=rbvar, value='a' ,indicatoron=0 )
rb1.pack()
rb2 = tk.Radiobutton(root, text="Option 2", variable=rbvar, value='b' )
rb2.pack()


entry=tk.Entry(root)
entry.pack()

button=tk.Button(root,text='alert',bg='white',command=(lambda:entry.insert(0,'HaHas')))
button.pack()



root.mainloop()








