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







