
shonen=['HunterxHunter','Naruto','Bleach','Fairy tail','One piece','Black clover','Soul eater','Dragon Ball Z','Yu-gi-oh!']
favorite={}
choices=[]

def sort_favorite(shonen,favorite):
    number=1
    for i in shonen:
        print(number,i)
        number+=1
    for k in shonen:
        favorite[k]=0
    print("Enter your choice in order:")
    length=len(shonen)
    i=1
    for j in favorite:
        if i<=9:
            print(i,'place')
            choice=input('')
            favorite[j]=choice
            i+=1
    return favorite
    
def main():
    print("-1-sort by favorite")
    print("-2-exit")
    choice=input('Enter your choice\n')
    if choice=='1' or choice=='2':
        choice=int(choice)
    else:
        print('try again  ')
        main()
    

    if choice==1:
        print(sort_favorite(shonen,favorite))
        main()
    elif choice==2:
        cho=input('Are you sure?Y/N')
        if cho=='Y' or cho=='y':
            exit()
        else:
            main()
    

print("_____________________________________________________________\n",
      "_____________________________________________________________\n",
      '\tMy favorite anime\t\n',
      "____________________________________________________________\n",
      "____________________________________________________________\n")


main()



















