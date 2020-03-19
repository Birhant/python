from setting import setting
from anime import add_anime
from anime import show_anime
"""
Used Rating measures
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
def upcoming():
    print('-1-Printing outputs in justified manner Completed')
    print('-2-Anime ranking Completed')
    print('-3-Editing title')
    print('-4-Input catching error completed')
    print('-5-Fix settings to synchronize')
    menu()
def menu():
    print('______________________________________________________________________')
    print('-1-Add anime\n-2-View anime\n-3-Setting(trial)\n-4-Exit\n-5-upcoming')
    print('______________________________________________________________________')
    choose=input('Choose :')
    if(choose=='1'):
        add_anime()
        menu()
    elif(choose=='2'):
        show_anime()
        menu()
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
menu()
