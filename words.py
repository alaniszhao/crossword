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

total = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def find_beginning(words, i, d, l, size):
    res=""
    additional=[]
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
    if seen==l:
        i_new=0
        for r in res:
            additional.append((i_new,r))
            i_new+=1
        return res,additional
    while(seen<l-1):
        if curr!="":
            additional.append((seen, curr))
        seen+=1
        if(d==1):
            i+=1
        else:
            i+=size
        curr=words[i]
    r=""
    for i in range(0, 49, 7):
        for j in range(i, i+7):
            if words[j]!="":
                r+=words[j]+" "
            else:
                r+="# "
        r+="\n"
    return res,additional

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

def fill_crossword(starts, b, used):
    '''
    starts is in the format [[i,dirs],...]
    where dirs is a list up to length two of the index and the direction
    of the word (down = -1, across = 1)
    the result should be in the format [[i,dir,word]]
    need to somehow keep track of the previous words
    '''
    words = init_words(b.size*b.size)
    last = None
    tried = []
    for start in starts:
        i=start[0]
        i_t = 0
        while(i_t<len(start[1])):
            t=start[1][i_t]
            l=t[1]
            d=t[0]
            beginning, additional = find_beginning(words, i, d,l, b.size)
            new = search_word(beginning, l, used, additional)
            if(new!=None):
                used.add(new)
                tried.append(words)
                add_word(words, new, i, d, b.size)
                i_t+=1
            else:
                words = tried.pop()
        print(start)
        res=""
        for i in range(0, 49, 7):
            for j in range(i, i+7):
                if words[j]!="":
                    res+=words[j]+" "
                else:
                    res+="# "
            res+="\n"
        print(res)
    return words

def check_word(additional, word):
    for curr in additional:
        if word[curr[0]]!=curr[1]:
            return False
    return True

def get_list(letter):
    global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
    if letter=="a":
        if(a==[]):
            fi = open("poss_words/A.txt", "r")
            data = fi.read()
            a = data.split("\n")
            fi.close()
        return a
    if letter=="b":
        if(b==[]):
            fi = open("poss_words/B.txt", "r")
            data = fi.read()
            b = data.split("\n")
            fi.close()
        return b
    if letter=="c":
        if(c==[]):
            fi = open("poss_words/C.txt", "r")
            data = fi.read()
            c = data.split("\n")
            fi.close()
        return c
    if letter=="d":
        if(d==[]):
            fi = open("poss_words/D.txt", "r")
            data = fi.read()
            d = data.split("\n")
            fi.close()
        return d
    if letter=="e":
        if(e==[]):
            fi = open("poss_words/E.txt", "r")
            data = fi.read()
            e = data.split("\n")
            fi.close()
        return e
    if letter=="f":
        if(f==[]):
            fi = open("poss_words/f.txt", "r")
            data = fi.read()
            f = data.split("\n")
            fi.close()
        return f
    if letter=="g":
        if(g==[]):
            fi = open("poss_words/G.txt", "r")
            data = fi.read()
            g = data.split("\n")
            fi.close()
        return g
    if letter=="h":
        if(h==[]):
            fi = open("poss_words/H.txt", "r")
            data = fi.read()
            h = data.split("\n")
            fi.close()
        return h
    if letter=="i":
        if(i==[]):
            fi = open("poss_words/I.txt", "r")
            data = fi.read()
            i = data.split("\n")
            fi.close()
        return i
    if letter=="j":
        if(j==[]):
            fi = open("poss_words/J.txt", "r")
            data = fi.read()
            j = data.split("\n")
            fi.close()
        return j
    if letter=="k":
        if(k==[]):
            fi = open("poss_words/K.txt", "r")
            data = fi.read()
            k = data.split("\n")
            fi.close()
        return k
    if letter=="l":
        if(l==[]):
            fi = open("poss_words/L.txt", "r")
            data = fi.read()
            l = data.split("\n")
            fi.close()
        return l
    if letter=="m":
        if(m==[]):
            fi = open("poss_words/M.txt", "r")
            data = fi.read()
            m = data.split("\n")
            fi.close()
        return m
    if letter=="n":
        if(n==[]):
            fi = open("poss_words/N.txt", "r")
            data = fi.read()
            n = data.split("\n")
            fi.close()
        return n
    if letter=="o":
        if(o==[]):
            fi = open("poss_words/O.txt", "r")
            data = fi.read()
            o = data.split("\n")
            fi.close()
        return o
    if letter=="p":
        if(p==[]):
            fi = open("poss_words/P.txt", "r")
            data = fi.read()
            p = data.split("\n")
            fi.close()
        return p
    if letter=="q":
        if(q==[]):
            fi = open("poss_words/Q.txt", "r")
            data = fi.read()
            q = data.split("\n")
            fi.close()
        return q
    if letter=="r":
        if(r==[]):
            fi = open("poss_words/R.txt", "r")
            data = fi.read()
            r = data.split("\n")
            fi.close()
        return r
    if letter=="s":
        if(s==[]):
            fi = open("poss_words/S.txt", "r")
            data = fi.read()
            s = data.split("\n")
            fi.close()
        return s
    if letter=="t":
        if(t==[]):
            fi = open("poss_words/T.txt", "r")
            data = fi.read()
            t = data.split("\n")
            fi.close()
        return t
    if letter=="u":
        if(u==[]):
            fi = open("poss_words/U.txt", "r")
            data = fi.read()
            u = data.split("\n")
            fi.close()
        return u
    if letter=="v":
        if(v==[]):
            fi = open("poss_words/V.txt", "r")
            data = fi.read()
            v = data.split("\n")
            fi.close()
        return v
    if letter=="w":
        if(w==[]):
            fi = open("poss_words/W.txt", "r")
            data = fi.read()
            w = data.split("\n")
            fi.close()
        return w
    if letter=="x":
        if(x==[]):
            fi = open("poss_words/X.txt", "r")
            data = fi.read()
            x = data.split("\n")
            fi.close()
        return x
    if letter=="y":
        if(y==[]):
            fi = open("poss_words/Y.txt", "r")
            data = fi.read()
            y = data.split("\n")
            fi.close()
        return y
    if letter=="z":
        if(z==[]):
            fi = open("poss_words/Z.txt", "r")
            data = fi.read()
            z = data.split("\n")
            fi.close()
        return z
        
def search_word(beginning, l, used, additional):
    invalid = set()
    if beginning == "":
        i = random.randint(0,25)
        curr = get_list(total[i])
        for word in curr:
            if len(word)==l and check_word(additional, word):
                return word
        invalid.add(i)
        while(True):
            i = random.randint(0,25)
            while(i in invalid):
                i = random.randint(0,25)
            curr = get_list(total[i])
            for word in curr:
                if len(word)==l and word not in used and check_word(additional, word):
                    used.add(word)
                    return word
            invalid.add(i)
            if len(invalid)==26:
                return None
    letter = get_list(beginning[0])
    if len(additional)==l:
        w = ""
        for a in additional:
            w+=a[1]
        if w in letter:
            return w
        return None
    for word in letter:
        if (len(word)==l) and (beginning==word[:len(beginning)]) and (word not in used) and check_word(additional, word):
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
                    dirs.append([-1,l])
                if col==0:
                    #1=right
                    l = 0
                    temp_i = i
                    lim = ((i+b.size)//b.size)*b.size
                    while(temp_i<lim and temp_i<b.size*b.size):
                        if b.squares[temp_i].get_fill():
                            break
                        l+=1
                        temp_i+=1
                    dirs.append([1,l])
                if row!=0 and i-b.size>=0 and b.squares[i-b.size].get_fill():
                    l = 0
                    temp_i = i
                    while(temp_i<b.size*b.size):
                        if b.squares[temp_i].get_fill():
                            break
                        l+=1
                        temp_i+=b.size
                    dirs.append([-1,l])
                if col!=0 and i-1>=0 and b.squares[i-1].get_fill():
                    l = 0
                    temp_i = i
                    lim = ((i+b.size)//b.size)*b.size
                    while(temp_i<lim and temp_i<b.size*b.size):
                        if b.squares[temp_i].get_fill():
                            break
                        l+=1
                        temp_i+=1
                    dirs.append([1,l])
            if len(dirs)!=0:
                starts.append([i,dirs])
    print(starts)
    return starts

def main():
    b = Board(7)
    starts=find_starts(b)
    used=set()
    words = fill_crossword(starts, b, used)
    while(words==None):
        words = fill_crossword(starts, b, used)
    print(words)
    res=""
    for i in range(0, 49, 7):
        for j in range(i, i+7):
            if words[j]!="":
                res+=words[j]+" "
            else:
                res+="# "
        res+="\n"
    print(res)


if __name__ == "__main__":
    main()