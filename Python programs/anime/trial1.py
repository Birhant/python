from tkinter import *
from anime_offline import anime
from anime_offline import linear_search
root=Tk()
canvas=Canvas(root,width=500,height=400)
canvas.pack()
def searching():
    frame2=Frame(root,bg='red')
    frame2.place(relx=0.05,rely=0.05,relwidth=0.4,relheight=0.4)
    entrys=entry.get()
    result=[]
    linear_search(result,anime,entrys)
    length=len(result)
    scrollbar=Scrollbar(frame2)
    scrollbar.pack(side=RIGHT,fill=Y)
    my_result=Listbox(frame2,yscrollcommand=scrollbar.set)

    length=len(result)

    for line in range(length):
        my_result.insert(END,result[line])
    my_result.pack(side=LEFT,fill=BOTH)

    scrollbar.config(command=my_result.yview)

def sea(entry):
    label=Label(frame2,text=entry,bg='red',fg='white')
    label.pack()
    

frame1=Frame(root,bg='blue')
frame1.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)
entry=Entry(frame1)
entry.pack(side=LEFT)

search=Button(frame1,text='search',command=searching)
search.pack(side=LEFT)



frame=Frame(frame1,bg='yellow')
frame.pack()
label=Label(root,text=anime['data'][1221]['title'])
label.pack()

scrollbar=Scrollbar(frame)
scrollbar.pack(side=RIGHT,fill=Y)

my_list=Listbox(frame,yscrollcommand=scrollbar.set)

length=len(anime['data'])

for line in range(length):
    my_list.insert(END,anime['data'][line]['title'])
my_list.pack(side=LEFT,fill=BOTH)

scrollbar.config(command=my_list.yview)
root.mainloop()
    
