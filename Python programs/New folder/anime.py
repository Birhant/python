import json

with open('anime.json','r') as reader:
    a=json.load(reader)
print(a)
length=len(a['Anime'])
for i in range(length):
    try:
        aa=a['Anime'][i]['Episode']
        continue
    except Exception:
        aa='a'
    print(a['Anime'][i]['Title'])
    episodes=input('Episodes :')
    a['Anime'][i]['Episode']=episodes
    cho=input('want to exit Y/N :')
    if(cho=='Y' or cho=='y'):
        break

with open('anime.json','w') as writter:
    json.dump(a,writter,indent=2)



