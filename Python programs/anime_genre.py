#Let's get started
anime_details=[]
details={'Title':'Gamers!','Genre':['One sided love','Otaku']}
anime_details.append(details)
details={'Title':'MM!','Genre':['Pervert','High school life']}
anime_details.append(details)
details={'Title':'Science Types Fall in love','Genre':['Romance','Science','Educational']}
anime_details.append(details)
details={'Title':'Scum\'s wish','Genre':['Romance','Science']}
anime_details.append(details)
details={'Title':'Wotakoi','Genre':['Romance','Otaku','Salaryman life']}
anime_details.append(details)
#define functions
def menu(anime_details):
    print('-1- Add anime\n-2- View anime\n-3- Search title by genre')
    choice=input('Enter your choice:')
    if(int(choice)==1):
        add_anime(anime_details)
    elif(int(choice)==2):
        view_anime(anime_details)
    elif(int(choice)==3):
        search_by_genre(anime_details)
    else:
        print('try again')
        menu(anime_details)

def add_anime(anime_details):
    print('Fill the following form')
    title=input('Title: ')
    b=input('Genre number: ')
    genres=[]
    for i in range(int(b)):
        genre=input('genre')
        genres.append(genre)
    details={'Title':title,'Genre':genres}
    anime_details.append(details)
    view_anime(anime_details)

def view_anime(anime_details):
    l=len(anime_details)
    print('title\t\t\tGenre')
    for i in range(l):
        print(anime_details[i]['Title'],'\t',anime_details[i]['Genre'])
    menu(anime_details)

def search_by_genre(anime_details):
    Total_genre=set({})
    l=len(anime_details)
    for i in range(l):
        k=len(anime_details[i]['Genre'])
        for j in range(k):
            Total_genre.add(anime_details[i]['Genre'][j])
    Total_genres=list(Total_genre)

    k=len(Total_genres)
    for i in range(k):
        print(i,'=>',Total_genres[i])
    cho=input('Input search')
    i=int(cho)
    genre=Total_genres[i]
    result=[]
    for i in range(l):
        k=len(anime_details[i]['Genre'])
        for j in range(k):
            if(genre==anime_details[i]['Genre'][j]):
                result.append(anime_details[i]['Title'])
    print(result)
    menu(anime_details)

menu(anime_details)

    




