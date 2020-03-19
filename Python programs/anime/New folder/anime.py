def add_anime():
    Title=input('Title :')
    Rating=['','','','','','','','','','']
    Rating[0]=input('Fun to watch 1-2-3 :')
    s=True
    while(s):
        try:
            b=int(Rating[0])
            if(b>=1 and b<=3):
                s=False
            else:
                print('try again')
                Rating[0]=input('Fun to watch 1-2-3 :')
                
        except Exception:
            print('try again')
            Rating[0]=input('Fun to watch 1-2-3 :')
    Rating[1]=input('Interesting plots 1-2-3 :')
    s=True
    while(s):
        try:
            b=int(Rating[1])
            if(b>=1 and b<=3):
                s=False
            else:
                print('try again')
                Rating[1]=input('Interesting plots 1-2-3 :')
        except Exception:
            print('try again')
            Rating[1]=input('Interesting plots 1-2-3 :')
    Rating[2]=input('Characters 1-2-3 :')
    s=True
    while(s):
        try:
            b=int(Rating[2])
            if(b>=1 and b<=3):
                s=False
            else:
                print('try again')
                Rating[2]=input('Characters 1-2-3 :')
        except Exception:
            print('try again')
            Rating[2]=input('Characters 1-2-3 :')
    Rating[3]=input('Animation 1-2-3 :')
    s=True
    while(s):
        try:
            b=int(Rating[3])
            if(b>=1 and b<=3):
                s=False
            else:
                print('try again')
                Rating[3]=input('Animation 1-2-3 :')
        except Exception:
            print('try again')
            Rating[3]=input('Animation 1-2-3 :')

    Rating[4]=input('Voice acting 1-2-3 :')
    s=True
    while(s):
        try:
            b=int(Rating[4])
            if(b>=1 and b<=3):
                s=False
            else:
                print('try again')
                Rating[4]=input('Voice acting 1-2-3 :')
        except Exception:
            print('try again')
            Rating[4]=input('Voice acting 1-2-3 :')
    Rating[5]=input('Visuals 1-2-3 :')
    s=True
    while(s):
        try:
            b=int(Rating[5])
            if(b>=1 and b<=3):
                s=False
            else:
                print('try again')
                Rating[5]=input('Visuals 1-2-3 :')
        except Exception:
            print('try again')
            Rating[5]=input('Visuals 1-2-3 :')
    Rating[6]=input('Maturity 1-2-3 :')
    s=True
    while(s):
        try:
            b=int(Rating[6])
            if(b>=1 and b<=3):
                s=False
            else:
                print('try again')
                Rating[6]=input('Maturity 1-2-3 :')
        except Exception:
            print('try again')
            Rating[6]=input('Maturity 1-2-3 :')
    Rating[7]=input('Overall story 1-2-3 :')
    s=True
    while(s):
        try:
            b=int(Rating[7])
            if(b>=1 and b<=3):
                s=False
            else:
                print('try again')
                Rating[7]=input('Overall story 1-2-3 :')
        except Exception:
            print('try again')
            Rating[7]=input('Overall story 1-2-3 :')
    Rating[8]=input('Fan service 1-2-3 :')
    s=True
    while(s):
        try:
            b=int(Rating[8])
            if(b>=1 and b<=3):
                s=False
            else:
                print('try again')
                Rating[8]=input('Fan service 1-2-3 :')
        except Exception:
            print('try again')
            Rating[8]=input('Fan service 1-2-3 :')
    Rating[9]=input('Ending 1-2-3 :')
    s=True
    while(s):
        try:
            b=int(Rating[9])
            if(b>=1 and b<=3):
                s=False
            else:
                print('try again')
                Rating[9]=input('Ending 1-2-3 :')
        except Exception:
            print('try again')
            Rating[9]=input('Ending 1-2-3 :')

    one={}
    one['Title']=Title
    one['Rating']=Rating
    anime=[]
    anime.append(one)
    print('/////////////////////////////////////////////')

    with open('anime.txt','a') as me:
        me.write('\n')
        me.write(anime[0]['Title'])
        me.write('\n')
        me.write(anime[0]['Rating'][0])
        me.write('\t')
        me.write(anime[0]['Rating'][1])
        me.write('\t')
        me.write(anime[0]['Rating'][2])
        me.write('\t')
        me.write(anime[0]['Rating'][3])
        me.write('\t')
        me.write(anime[0]['Rating'][4])
        me.write('\t')
        me.write(anime[0]['Rating'][5])
        me.write('\t')
        me.write(anime[0]['Rating'][6])
        me.write('\t')
        me.write(anime[0]['Rating'][7])
        me.write('\t')
        me.write(anime[0]['Rating'][8])
        me.write('\t')
        me.write(anime[0]['Rating'][9])
    show_anime()

def anime_list(anime):
    detail={}
    with open('anime.txt','r') as me:
        a=me.readlines()
    b=len(a)
    b=int(b/2)
    for i in range(b):
        c=i*2
        d=a[c]
        e=d.split('\n')
        detail['title']=e[0]

        c+=1
        d=a[c]
        e=d.split('\t')
        f=e[9]
        g=f.split('\n')
        e[9]=g[0]
        detail['rating']=e
        animes={}
        animes['Title']=detail['title']
        animes['Rating']=detail['rating']
        anime.append(animes)

def show_anime():
    anime=[]
    anime_list(anime)
    anime_gui=[]
    length=len(anime)
    rating=[]
    title=[]
    for i in range(length):
        x=0
        for j in range(10):
            y=int(anime[i]['Rating'][j])
            x=x+y
        x=x/3
        x=round(x,2)
        rating.append(x)
        title.append(anime[i]['Title'])
    print('{:>10}{:>40}{:>20}'.format('Rank','Title','Rating'))
    for i in range(length):
        j=i+1
        while(j<length):
            if(rating[i]<rating[j]):
                x=rating[i]
                y=title[i]
                rating[i]=rating[j]
                rating[j]=x
                title[i]=title[j]
                title[j]=y
            j+=1
        Title=title[i]
        rate=rating[i]
        gui={}
        gui['Title']=title[i]
        gui['Rating']=rating[i]
        anime_gui.append(gui)
        new_line='{:>10}{:>40}{:>20}'.format(i+1,Title,rate)
        print(new_line)
