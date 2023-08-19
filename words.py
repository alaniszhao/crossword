from board import *
import os
from PyDictionary import PyDictionary
dictionary=PyDictionary()

a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
i=[]
j=[]
k=[]
l=[]
m=[]
n=[]
o=[]
p=[]
q=[]
r=[]
s=[]
t=[]
u=[]
v=[]
w=[]
x=[]
y=[]
z=[]

total = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,z,y,z]

def find_beginning(words, i, d, l, size):
    res=""
    curr=words[i]
    seen = 0
    while(curr!="" and seen<l):
        res+=curr
        seen+=1
        if(d==1):
            i+=1
        else:
            i+=size
        curr=words[i]
    return res

def add_word(words, new, i, d, size):
    for c in new:
        words[i]=c
        if(d==1):
            i+=1
        else:
            i+=size

def init_words(last):
    words = dict()
    for i in range(last):
        words[i]=""
    return words
def fill_crossword(starts, b):
    '''
    starts is in the format [[i,dirs],...]
    where dirs is a list up to length two of the index and the direction
    of the word (down = -1, across = 1)
    the result should be in the format [[i,dir,word]]
    need to somehow keep track of the previous words
    '''
    used=set()
    words = init_words(b.size*b.size)
    for start in starts:
        i=start[0]
        for t in start[1]:
            l=t[1]
            d=t[0]
            beginning = find_beginning(words, i, d,l, b.size)
            new = search_word(beginning, l, used)
            if(new!=None):
                used.add(new)
                add_word(words, new, i, d, b.size)
            else:
                #add this later
                exit(1)
    return words

def get_list(letter):
    if letter=="a":
        return a
    if letter=="b":
        return b
    if letter=="c":
        return c
    if letter=="d":
        return d
    if letter=="e":
        return e
    if letter=="f":
        return f
    if letter=="g":
        return g
    if letter=="h":
        return h
    if letter=="i":
        return i
    if letter=="j":
        return j
    if letter=="k":
        return k
    if letter=="l":
        return l
    if letter=="m":
        return m
    if letter=="n":
        return n
    if letter=="o":
        return o
    if letter=="p":
        return p
    if letter=="q":
        return q
    if letter=="r":
        return r
    if letter=="s":
        return s
    if letter=="t":
        return t
    if letter=="u":
        return u
    if letter=="v":
        return v
    if letter=="w":
        return w
    if letter=="x":
        return x
    if letter=="y":
        return y
    if letter=="z":
        return z
        
def search_word(beginning, l, used):
    invalid = set()
    if beginning == "":
        i = random.randint(0,25)
        curr = total[i]
        for word in curr:
            if len(word)==l:
                return word
        invalid.add(i)
        while(True):
            i = random.randint(0,25)
            while(i in invalid):
                i = random.randint(0,25)
            curr = total[i]
            for word in curr:
                if len(word)==l and word not in used:
                    used.add(word)
                    return word
            invalid.add(i)
    letter = get_list(beginning[0])
    for word in letter:
        if (len(word)==l) and (beginning==word[:len(beginning)]) and (word not in used):
            used.add(word)
            return word
    return None

def find_starts(b):
    starts = []
    for row in range(b.size):
        for col in range(b.size):
            i = row*b.size+col
            dirs = []
            if not b.squares[i].get_fill():
                if row==0:
                    #-1=down
                    l = 0
                    temp_i = i
                    while(temp_i<b.size*b.size):
                        if b.squares[temp_i].get_fill():
                            break
                        l+=1
                        temp_i+=b.size
                    dirs.append(-1,l)
                if col==0:
                    #1=right
                    l = 0
                    temp_i = i
                    while(temp_i<b.size):
                        if b.squares[temp_i].get_fill():
                            break
                        l+=1
                        temp_i+=1
                    dirs.append(1,l)
                if row!=0 and i-b.size>=0 and b.squares[i-b.size].get_fill():
                    l = 0
                    temp_i = i
                    while(temp_i<b.size*b.size):
                        if b.squares[temp_i].get_fill():
                            break
                        l+=1
                        temp_i+=b.size
                    dirs.append(-1,l)
                if col!=0 and i-1>=0 and b.squares[i-1].get_fill():
                    l = 0
                    temp_i = i
                    while(temp_i<b.size):
                        if b.squares[temp_i].get_fill():
                            break
                        l+=1
                        temp_i+=1
                    dirs.append(1,l)
            if len(dirs)!=0:
                starts.append([i,dirs])

def main():
    b = Board(7)
    starts=find_starts(b)
    words = fill_crossword(starts, b)

if __name__ == "__main__":
    main()