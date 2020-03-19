import tkinter as tk
import json
def add(a,anime):
    length=len(anime)
    aa={}
    aa['Title']=a
    anime['Anime'].append(aa)
    with open('anime.json','w+') as writter:
        json.dump(anime,writter,indent=2)

    
root=tk.Tk()
root.title('Anime')
canvas=tk.Canvas(root,width=1000,height=400)
canvas.pack()
frame=tk.Frame(root,bg='#1f3850')
frame.place(relx=0.25,rely=0.01,relwidth=0.5,relheight=0.9)
anime={}
with open('anime.json','r+') as reader:
    anime=json.load(reader)
length=len(anime['Anime'])
for i in range(length):
    title=tk.Label(frame,text='Title',bg='#1f3850',fg='#63ff6b')
    title.grid(row=1,column=0 )
    rating=tk.Label(frame,text='Rating',bg='#1f3850',fg='#63ff6b')
    rating.grid(row=1,column=1 )
    texts=tk.Label(frame,text=anime['Anime'][i]['Title'],bg='#1f3850',fg='#63ff6b')
    texts.grid(row=i+2,column=0)
    text1=tk.Label(frame,text=str(anime['Anime'][i]['Title']),bg='#1f3850',fg='#63ff6b')
    text1.grid(row=i+2,column=1)
    text2=tk.Label(frame,text='Title :' ,bg='#1f3850',fg='#63ff6b')
    text2.grid(row=0,column=0)
    textbox=tk.Entry(frame)
    textbox.grid(row=0,column=1)
    button1=tk.Button(frame,text='Add',command=(lambda:add(textbox.get(),anime)), fg='#c26a71', bg='#ecc4ff')
    button1.grid(row=0,column=2)

root.mainloop()






