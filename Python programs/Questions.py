def subjects_list(subject):
    with open('subject.txt','r') as w:
        a=w.readlines()
    length=len(a)
    for i in range(length):
        b=a[i]
        c=b.split('\n')
        subject.append(c[0])
        
def select_subject(sub):
    subject=[]
    listed=''
    subjects_list(subject)
    length=len(subject)
    for i in range(length):
        print(i+1,'-',subject[i])
    cho=input('Choose :')
    a=int(cho)
    a-=1
    sub.append('subjects/'+subject[a]+'.txt')


def reading_questions():
    subjects_path=[]
    select_subject(subjects_path)
    reading=[]
    with open(subjects_path[0],'r') as reader:
        a=reader.readlines()
    length=len(a)
    for i in range(length):
        b=a[i]
        c=b.split('\n')
        reading.append(c[0])
    for i in range(length):
        print(i+1,'-',reading[i])
    menu()

def write_questions():
    subjects_path=[]
    questions=[]
    select_subject(subjects_path)
    while(True):
        question=input('Question :')
        questions.append(question)
        cho=input('continue ?1/0')
        if(cho=='0'):
            break
    with open(subjects_path[0],'a') as writter:
        length=len(questions)
        for i in range(length):
            writter.write(questions[i])
            writter.write('\n')
    menu()

def add_subject():
    a=input('Enter subject name :')
    to_file=a+'\n'
    to_create='subjects/'+a+'.txt'
    with open('subject.txt','a') as writter:
        writter.write(to_file)
    with open(to_create,'w') as writer:
        writer.write('')
    menu()
def menu():
    print('-1-Add subject\n-2-Write question\n-3-Read questions')
    cho=input('Choice :')
    if(cho=='1'):
        add_subject()
    elif(cho=='2'):
        write_questions()
    elif(cho=='3'):
        reading_questions()

menu()



