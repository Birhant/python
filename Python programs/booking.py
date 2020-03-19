def book():
    bed=input('Input number beds :')
    bed=int(bed)
    booked=set()
    print('-1-Single bed\n-2-Double bed\n-3-Grand bed\nFamily bed')
    for i in range(bed):
        print(i+1)
        added=input('')
        if added=='':
            continue;
        booked.add(added)
        print(booked)
#    facility
#level Bed
book()






