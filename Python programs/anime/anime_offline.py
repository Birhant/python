#Linear search in total number of anime(Japan animation)
import json
from PIL import Image,ImageTk
from tkinter import *
import urllib.request
import urllib.parse
import re

def comparison(leng,current_list,search_list):
    b=True
    length=len(current_list)
    if(length<leng):
        b=False
    else:
        for j in range(leng):
            if(current_list[j]!=search_list[j]):
                b=False
    return b

def linear_search(l,anime,search_anime):
    length=len(anime["data"])
    for i in range(length):
        search_list=[]
        search_anime=search_anime.lower()
        search_list=list(search_anime)
        leng=len(search_list)

        current=anime["data"][i]['title']
        current=current.lower()
        current_list=[]
        current_list=list(current)
        b=comparison(leng,current_list,search_list)
        
        synonyms=anime['data'][i]['synonyms']
        lengths=len(synonyms)
        d=False
        for j in range(lengths):
            e=synonyms[j]
            try:
                e=e.lower()
            except Exception:
                e=synonyms[j]
            synonym_list=list(e)
            f=comparison(leng,synonym_list,search_list)
            d=d or f
            
        if(b or d):
            current=current.capitalize()
            l.append(current)
            
        

def menu(anime):
    search_anime=input('Title :')
    l=[]
    linear_search(l,anime,search_anime)
    print(l)
    menu(anime)
def anime():
    with open('anime-offline-database.json',encoding="utf-8") as reader:
        anime=json.load(reader)
    return anime
    
    

with open('anime-offline-database.json',encoding="utf-8") as reader:
    anime=json.load(reader)

picture=anime['data'][124]['picture']
url=picture
req=urllib.request.Request(url)
resp=urllib.request.urlopen(req)
respData=resp.read()
print(respData)




root=Tk()
img=ImageTk.PhotoImage(Image.open(picture))
label=Label(root,image=img)
label.pack()
root.mainloop()


"""
abc=set({})
length=len(anime['data'])
for i in range(length):
    abc=abc.union(anime['data'][i]['status'])
print(abc)
"""


