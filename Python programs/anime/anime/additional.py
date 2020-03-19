import json
import os

#Checking for similar content
def checking_before_saving(genre,description):
    good=True
    
    if(os.path.isfile('genre.json')):
        with open('genre.json') as reader:
            genres=json.load(reader)
            
        #Number of lines
        if(len(genres['genre'])>0):
            for i in genres['genre']:
                if(i['name']==genre or i['description']==description):
                    good=False
        
    return good

def add_genre():
    if(not os.path.isfile('genre.json')):
        new={'genre':[]}
        with open('genre.json','w') as writter:
            json.dump(new,writter,indent=2)
            
    with open('genre.json') as reader:
        genres=json.load(reader)

    #genre Accepting
    genre=input('Genre name :')
    description=input('Description :')
    
    check=checking_before_saving(genre,description)
    #Writting back to genre
    if(check):
        new={'name':genre,'description':description}
        genres['genre'].append(new)
        with open('genre.json','w') as writter:
            json.dump(genres,writter,indent=2)
    else:
        print('try again')
        add_genre()

def selecting_genre():
    #Selected genre name is returned
    with open('genre.json') as reader:
        genres=json.load(reader)
    lines=len(genres['genre'])
    for i in range(lines):
        print(i,' ',genres['genre'][i]['name'])

    genre=input('Genre :')
    genre=genres['genre'][int(genre)]['name']
    return genre

def assigning_genre():
    #Connecting genre with anime
    with open('anime.json') as reader:
        anime=json.load(reader)
    i=0
    length=len(anime['Anime'])
    #Filling them with blank
    while(i<length):
        try:
            null=anime['Anime'][i]['Genre']==None
        except Exception:
            anime['Anime'][i]['Genre']=[]
        i+=1
    #Giving choice for anime to receive genre
    for i in range(length):
        print(i,' ',anime['Anime'][i]['Title'])

    Title=input('Title :')
    rank=int(Title)
    print(anime['Anime'][rank]['Title'],' :')
    genre=selecting_genre()
    anime['Anime'][rank]['Genre'].append(genre)

    with open('anime.json','w') as writter:
        json.dump(anime,writter,indent=2)

