"""
The following are measurements used
///////////////////////////////////
Fun to watch 1-2-3
Interesting plots/twist 1-2-3
Characters development 1-2-3
Animation 1-2-3
Voice acting 1-2-3
Visuals or beauty of drawings 1-2-3
Does the story make sense 1-2-3
Setting or world building 1-2-3
Fan service 1-2-3
Ending or season finale 1-2-3
"""
import json


#Checking input
def integer_or_not(value):
    good=True
    try:
        a=int(value)
        if(a<=3 and a>=1):
            good=True
        else:
            good=False
    except Exception:
        good=False
    return good
#Main program
def rating():
    #Rating questions
    Questions=["Fun to watch 1-2-3","Interesting plots/twist 1-2-3","Characters development 1-2-3","Animation 1-2-3","Voice acting 1-2-3","Visuals or beauty of drawings 1-2-3","Does the story make sense 1-2-3","Setting or world building 1-2-3","Fan service 1-2-3","Ending or season finale 1-2-3"]
    #Total rate variable
    rate=0
    #Number of questions
    number=len(Questions)
    #Getting values
    i=0
    while(i<number):
        print(Questions[i])
        rates=input("=>")
        result=integer_or_not(rates)
        if(result):
            rate=rate+int(rates)
            i+=1
        else:
            print('Try again !')
    rate=rate/3
    rate=round(rate,2)
    print(rate)

#rating()


