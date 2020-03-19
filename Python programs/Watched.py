"""
Title
Fun to watch 1-2-3
Interesting plots 1-2-3
Characters 1-2-3
Animation 1-2-3
Voice acting 1-2-3
Visuals 1-2-3
Maturity 1-2-3
Overall story 1-2-3
Fan service 1-2-3
Ending 1-2-3
"""
from for_anime import gui
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
        print(anime_gui)
        new_line='{:>10}{:>40}{:>20}'.format(i+1,Title,rate)
        print(new_line)


    menu()


def upcoming():
    print('-1-Printing outputs in justified manner Completed')
    print('-2-Anime ranking Completed')
    print('-3-Editing title')
    print('-4-Input catching error completed')
    print('-5-Fix settings to synchronize')
    menu()
def add_setting():
    settings={}
    settings['Location']=input('Location')
    settings['Place']=input('Place')
    settings['Time']=input('Time')
    To_file=settings['Location']+'\t'+settings['Place']+'\t'+settings['Time']+'\n'
    with open('settings.txt','a') as writes:
        writes.write(To_file)

def settings_list(settings):
    setting={}
    with open('settings.txt','r') as reader:
        a=reader.readlines()
    length=len(a)
    for i in range(length):
        b=a[i]
        c=b.split('\t')
        d=c[2]
        e=d.split('\n')
        setting['Location']=c[0]
        setting['Place']=c[1]
        setting['Time']=e[0]
        settings.append(setting)
    
def assigned_settings_list(settings):
    setting={}
    with open('anime_settings.txt','r') as reader:
        a=reader.readlines()
    length=len(a)
    for i in range(length):
        b=a[i]
        c=b.split('\t')
        d=c[2]
        e=d.split('\n')
        setting['Location']=c[0]
        setting['Place']=c[1]
        setting['Time']=e[0]
        settings.append(setting)

def assign_setting():
    anime=[]
    anime_list(anime)
    length=len(anime)
    anime_settings=[]
    setting={}
    To_file=''
    assigned=[]
    assigned_settings_list(assigned)
    assign_len=len(assigned)
    i=assign_len
    while (i<length):
        print(anime[i]['Title'])
        setting['Location']=input('Location')
        setting['Place']=input('Place')
        setting['Time']=input('Time')
        anime_settings.append(setting)
        To_file=To_file+setting['Location']+'\t'+setting['Place']+'\t'+setting['Time']+'\n'
        i+=1
        cho=input('Do you want to continue?Y/N')
        if(cho=='N' or cho=='n'):
            break

    settings=[]
    settings_list(settings)
    length1=len(anime_settings)
    length2=len(settings)

    Location=True
    Place=True
    Time=True
    To_setting=''
    for i in range(length1):
        for j in range(length2):
            if(anime_settings[i]['Location']==settings[j]['Location']):
                Location=False
            if(anime_settings[i]['Place']==settings[j]['Place']):
                Place=False
            if(anime_settings[i]['Time']==settings[j]['Time']):
                Time=False


        if(Location and Place and Time):
            To_setting=To_setting+anime_settings[i]['Location']+'\t'+anime_settings[i]['Place']+'\t'+anime_settings[i]['Time']+'\n'
        elif(Location and Place and not Time):
            To_setting=To_setting+anime_settings[i]['Location']+'\t'+anime_settings[i]['Place']+'\t'+'_'+'\n'
        elif(Location and not Place and Time):
            To_setting=To_setting+anime_settings[i]['Location']+'\t'+'_'+'\t'+anime_settings[i]['Time']+'\n'
        elif(not Location and Place and Time):
            To_setting=To_setting+'_'+'\t'+anime_settings[i]['Place']+'\t'+anime_settings[i]['Time']+'\n'
        elif(Location and not Place and not Time):
            To_setting=To_setting+anime_settings[i]['Location']+'\t'+'_'+'\t'+'_'+'\n'
        elif(not Location and Place and not Time):
            To_setting=To_setting+'_'+'\t'+anime_settings[i]['Place']+'\t'+'_'+'\n'
        elif(not Location and not Place and Time):
            To_setting=To_setting+'_'+'\t'+'_'+'\t'+anime_settings[i]['Time']+'\n'
        
    with open('settings.txt','a') as writter:
        writter.write(To_setting)
    
    with open('anime_settings.txt','a') as writter:
        writter.write(To_file)


    
def setting():
    print('-1-Add setting \n-2-Assign setting to anime \n')
    cho=input('Choose :')
    if(cho=='1'):
        add_setting()
    elif(cho=='2'):
        assign_setting()
    menu()

def menu():
    print('______________________________________________________________________')
    print('Welcome to anime rating simple code')
    print('______________________________________________________________________')
    print('29/2/2020 All rights reserved by Birhan Tesfaye v0001.2')
    print('______________________________________________________________________')
    print('\        /\        /\        /\   e    /\        /\        /\  w     /')
    print(' \      /  \   n  /  \      /  \      /  \ o    /  \      / e\      / ')
    print('  \ a  /    \    /    \    /  m \    /    \    /    \ s  /    \    /  ')
    print('   \  /      \  /      \ m/      \  /      \  /      \  /      \  /   ')
    print('    \/        \/   e    \/        \/        \/        \/        \/ a  ')
    print('______________________________________________________________________')
    print('Welcome to anime rating simple code')
    print('______________________________________________________________________')
    print('-1-Add anime\n-2-View anime\n-3-Setting(trial)\n-4-Exit\n-5-upcoming')
    print('______________________________________________________________________')
    choose=input('Choose :')
    if(choose=='1'):
        add_anime()
    elif(choose=='2'):
        show_anime()
    elif(choose=='3'):
        setting()
    elif(choose=='4'):
        cho=input('Are you sure Y/N')
        if(cho=='Y' or cho=='y'):
            exit()
        else:
            menu()
    elif(choose=='5'):
        upcoming()
    
    else:
        menu()
menu()















