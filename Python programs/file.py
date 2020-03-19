"""
with open('file.txt','w') as fileobj:
    fileobj.write('something')




with open('anime.txt','w') as anime:
    anime.write('anime is awesome\na\nb\nc')


with open('anime.txt','r') as anime:
    lines=anime.readlines()
a=len(lines)
print(a)
print(lines[2])



with open('waifu.txt','w') as otaku:
    otaku.write('Rem is the best\nRoswal is also good')

with open('waifu.txt','r') as otaku:
    a=otaku.read()
    lines=a.split('\n')
print(lines)



with open('SAO.txt','w') as myself:
    myself.write('season 1\tThis is my favourite one\nseason 2\tThis is meddium one\nseason 3\tSimply the worst one')
"""
with open('SAO.txt','a') as myself:
    myself.write('additional')


