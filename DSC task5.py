#create a stack
s1=[]
def push(num):
    s1.append(num)
    print(s1)

def popit():
    for i in range(len(s1)):
        if len(s1)>=1:
            p=s1.pop()
        else:
            print("empty stack")
    print(p)  

def peek():
    if len(s1)>=1:
           print(s1[-1])
    else:
        print("empty stack")
num=int(input("enter number"))
push(num)
peek()
popit()
                   
