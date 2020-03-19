import time
import os
def comparison():
    return os.path.getsize('trial.txt')>=os.path.getsize('trial1.txt')
    
with open('trial.txt','a+') as writter:
    writter.write('something')

with open('trial.txt','r') as reader:
    a=reader.readlines()

if(not os.path.exists('trial1.txt')):
    with open('trial.txt','r') as reader,open('trial1.txt','w') as writter:
        ab=reader.readlines()
        writter.write(ab[0])

b=comparison()

print('Current file :',a)
print('Comparison to backup :',b)

exception=input('Exception :True/False')
if(exception=='True'):
    exception=True
else:
    exception=False

time.sleep(1)
if(b or exception):
    ##Backing up
    with open('trial.txt','r') as reader,open('trial1.txt','w') as writter:
        ab=reader.readlines()
        writter.write(ab[0])
        print('Backup Updated:',ab[0])
else:
    ##Recovering
    with open('trial1.txt','r') as reader,open('trial.txt','w') as writter:
        ab=reader.readlines()
        writter.write(ab[0])
        print('Recovered :',ab[0])
    


