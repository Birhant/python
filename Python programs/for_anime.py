from tkinter import *
def gui(lists):
    root=Tk()
    root.title('Anime Ranking')
    length=len(lists)
    texts=''
    i=0
    intro='{:>50}{:>10}'.format('Anime','Ranking')
    while(i<length):
        a=lists[i]['Title']
        c=lists[i]['Rating']
        d='{:<40}{:>10}'.format(a,c)
        texts=texts+d+'\n'
        i+=1
    Writter=Label(root,text=intro)
    Writter.pack()
    Written=Label(root,text=texts)
    Written.pack()
    root.mainloop()
    
anime=[{'Title': 'Full metal Alchemist brotherhood ', 'Rating': 9.33}, {'Title': 'Assassination classroom', 'Rating': 8.67}, {'Title': 'Attack on titans', 'Rating': 8.67}, {'Title': 'Daily life of high school boys', 'Rating': 8.67}, {'Title': 'Kimetsu no yaiba', 'Rating': 8.67}, {'Title': 'HunterxHunter', 'Rating': 8.67}, {'Title': 'Dan machi', 'Rating': 8.33}, {'Title': 'Danganronpa', 'Rating': 8.33}, {'Title': 'Naruto', 'Rating': 8.33}, {'Title': 'Akame ga kill', 'Rating': 8.33}, {'Title': 'Kurugehime', 'Rating': 8.0}, {'Title': 'clannad', 'Rating': 8.0}, {'Title': 'Youjo Senki', 'Rating': 8.0}, {'Title': 'Skip Beat!', 'Rating': 8.0}, {'Title': 'Gurren laggan', 'Rating': 8.0}, {'Title': 'Dororo', 'Rating': 7.67}, {'Title': 'Erased', 'Rating': 7.67}, {'Title': 'Overlord', 'Rating': 7.67}, {'Title': 'My Hero Academia', 'Rating': 7.33}, {'Title': 'One punch man', 'Rating': 7.33}, {'Title': 'The pet girl of Sakurasou', 'Rating': 7.33}, {'Title': 'Mob psycho 100', 'Rating': 7.33}, {'Title': 'Death parade', 'Rating': 7.0}, {'Title': 'Devil is partimer!', 'Rating': 6.67}, {'Title': 'Classroom of the elit', 'Rating': 6.33}, {'Title': 'Death march', 'Rating': 5.67}, {'Title': 'Arifureta', 'Rating': 5.67}, {'Title': 'Maou-sama retry!', 'Rating': 5.33}, {'Title': "Assassin's pride", 'Rating': 5.33}]
gui(anime)
