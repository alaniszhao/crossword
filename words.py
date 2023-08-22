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
        print(start)
        i=start[0]
        for t in start[1]:
            l=t[1]
            d=t[0]
            beginning = find_beginning(words, i, d,l, b.size)
            new = search_word(beginning, l, used)
            if(new!=None):
                print(new)
                used.add(new)
                add_word(words, new, i, d, b.size)
            else:
                #add this later
                exit(1)
    return words

def get_list(letter):
    if letter=="a":
        if(a==[]):
            f = open("A.txt", "r")
            data = f.read()
            a = data.split("\n")
            f.close()
        return a
    if letter=="b":
        if(b==[]):
            f = open("B.txt", "r")
            data = f.read()
            b = data.split("\n")
            f.close()
        return b
    if letter=="c":
        if(c==[]):
            f = open("C.txt", "r")
            data = f.read()
            c = data.split("\n")
            f.close()
        return c
    if letter=="d":
        if(d==[]):
            f = open("D.txt", "r")
            data = f.read()
            d = data.split("\n")
            f.close()
        return d
    if letter=="e":
        if(e==[]):
            f = open("E.txt", "r")
            data = f.read()
            e = data.split("\n")
            f.close()
        return e
    if letter=="f":
        if(f==[]):
            fi = open("F.txt", "r")
            data = fi.read()
            f = data.split("\n")
            fi.close()
        return f
    if letter=="g":
        if(g==[]):
            f = open("G.txt", "r")
            data = f.read()
            g = data.split("\n")
            f.close()
        return g
    if letter=="h":
        if(h==[]):
            f = open("H.txt", "r")
            data = f.read()
            h = data.split("\n")
            f.close()
        return h
    if letter=="i":
        if(i==[]):
            f = open("I.txt", "r")
            data = f.read()
            i = data.split("\n")
            f.close()
        return i
    if letter=="j":
        if(j==[]):
            f = open("J.txt", "r")
            data = f.read()
            j = data.split("\n")
            f.close()
        return j
    if letter=="k":
        if(k==[]):
            f = open("K.txt", "r")
            data = f.read()
            k = data.split("\n")
            f.close()
        return k
    if letter=="l":
        if(l==[]):
            f = open("L.txt", "r")
            data = f.read()
            l = data.split("\n")
            f.close()
        return l
    if letter=="m":
        if(m==[]):
            f = open("M.txt", "r")
            data = f.read()
            m = data.split("\n")
            f.close()
        return m
    if letter=="n":
        if(n==[]):
            f = open("N.txt", "r")
            data = f.read()
            n = data.split("\n")
            f.close()
        return n
    if letter=="o":
        if(o==[]):
            f = open("O.txt", "r")
            data = f.read()
            o = data.split("\n")
            f.close()
        return o
    if letter=="p":
        if(p==[]):
            f = open("P.txt", "r")
            data = f.read()
            p = data.split("\n")
            f.close()
        return p
    if letter=="q":
        if(q==[]):
            f = open("Q.txt", "r")
            data = f.read()
            q = data.split("\n")
            f.close()
        return q
    if letter=="r":
        if(r==[]):
            f = open("R.txt", "r")
            data = f.read()
            r = data.split("\n")
            f.close()
        return r
    if letter=="s":
        if(s==[]):
            f = open("S.txt", "r")
            data = f.read()
            s = data.split("\n")
            f.close()
        return s
    if letter=="t":
        if(t==[]):
            f = open("T.txt", "r")
            data = f.read()
            t = data.split("\n")
            f.close()
        return t
    if letter=="u":
        if(u==[]):
            f = open("U.txt", "r")
            data = f.read()
            u = data.split("\n")
            f.close()
        return u
    if letter=="v":
        if(v==[]):
            f = open("V.txt", "r")
            data = f.read()
            v = data.split("\n")
            f.close()
        return v
    if letter=="w":
        if(w==[]):
            f = open("W.txt", "r")
            data = f.read()
            w = data.split("\n")
            f.close()
        return w
    if letter=="x":
        if(x==[]):
            f = open("X.txt", "r")
            data = f.read()
            x = data.split("\n")
            f.close()
        return x
    if letter=="y":
        if(y==[]):
            f = open("Y.txt", "r")
            data = f.read()
            y = data.split("\n")
            f.close()
        return y
    if letter=="z":
        if(z==[]):
            f = open("Z.txt", "r")
            data = f.read()
            z = data.split("\n")
            f.close()
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
    b = Board(9)
    print("DONE")
    starts=find_starts(b)
    words = fill_crossword(starts, b)
    print(words)

if __name__ == "__main__":
    main()